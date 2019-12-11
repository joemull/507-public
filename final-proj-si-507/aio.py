import asyncio
import time
import aiohttp
import json
import apis
import api_keys
from diskcache import Cache
import webbrowser as wb
# from safeprint import print

# FORM REQUEST URLS
active_apis = [
    apis.MetSearch(),
    apis.RijksSearch(),
    apis.EuSearch(),
    apis.FlemishSearch(),
    # apis.Walters(),
    apis.ImagesdArt(),
    apis.Harvard(),
]

# CREATE PAGE
def present(artworks,all_created):
    page = u'\n\nPage One'
    if len(artworks) > 0:
        num = 1
        for work in sorted(artworks, key = lambda work:work.relevance,reverse=True):
            page += u'\n\n{}. {}\n      {} (relevance {})'.format(
                num,work.titleText,
                work.currentRepositoryGeographicLocation,
                work.relevance,
            )
            num += 1

        if all_created == False:
            page += u'\n\nNote: some results could not be loaded'
        page += u'\n'
    return page

# MANAGE SEARCHES
async def manage_requests(requesters):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = []
        for requester in requesters:
            task = asyncio.create_task(requester.get(session))
            tasks.append(task)
        return await asyncio.gather(*tasks, return_exceptions=False)

def make_search_requests(active_apis,searchers,q,cache_dir):
    requesters = []

    with Cache(cache_dir) as ref:
        for api in active_apis:
            api.prepare(q)
            if api.cache_key() in ref:
                api.hits = api.format(ref.get(api.cache_key()))
                api.check_resumption()
                searchers.append(api)
            else:
                requesters.append(api)

    # MAKE NEEDED SEARCH REQUESTS
    req_resp_tuples = asyncio.run(manage_requests(requesters))

    # SET HARVESTER RESUMPTION
    # ENTER NEW REQUESTS INTO CACHE
    active_apis = []
    with Cache(cache_dir) as ref:
        for requester, response in req_resp_tuples:
            requester.hits = requester.format(response)
            requester.check_resumption()
            searchers.append(requester)
            ref.set(requester.cache_key(),response)
    return active_apis, searchers


def revolve(active_apis=active_apis,q=''):

    # CACHE DIRECTORY
    cache_dir = u'harvest2'

    start = time.time()

    # SET UP SEARCH REQUESTS FOR UNCACHED SEARCHES
    searchers = []

    active_apis, searchers = make_search_requests(active_apis,searchers,q,cache_dir)

    maxResumptionListSize = 0
    for api in active_apis:
        if api.resumptionListSize > maxResumptionListSize:
            maxResumptionListSize = api.resumptionListSize
    maxResumptionListSize = round(maxResumptionListSize/20)

    print('Without control, the max resumption list size would be',str(maxResumptionListSize))

    # CONTROL
    maxResumptionListSize = 5

    for resumption in range(0,maxResumptionListSize):
        if len(active_apis) > 0:
            active_apis, searchers = make_search_requests(active_apis,searchers,q,cache_dir)

    search_duration = round((time.time() - start),2)

    # SET UP RETRIEVAL REQUESTS FOR UNCACHED RETRIEVALS
    with Cache(cache_dir) as ref:
        requesters = []
        for searcher in searchers:
            if searcher.retrieves == True:
                searcher.retrievals = searcher.list_records()[:searcher.limit]
            else:
                searcher.retrievers = []
                searcher.retrievals = []
                searcher.ids = searcher.list_ids()
                for id in searcher.ids:
                    retriever = searcher.retriever()
                    retriever.base = retriever.format_base(id)
                    retriever.params = retriever.format_params(id)
                    searcher.retrievers.append(retriever)
                for retriever in searcher.retrievers[:searcher.limit]:
                    if retriever.cache_key() in ref:
                        searcher.retrievals.append(
                            retriever.format(ref.get(retriever.cache_key())))
                    else:
                        requesters.append(retriever)

    # MAKE NEEDED RETRIEVAL REQUESTS
    req_resp_tuples = asyncio.run(manage_requests(requesters))

    # ENTER NEW REQUESTS INTO CACHE AND DATABASE
    with Cache(cache_dir) as ref:
        for searcher in searchers:
            if searcher.retrieves == False:
                for requester, response in req_resp_tuples:
                    if searcher.museum == requester.museum:
                        searcher.retrievals.append(requester.format(response))
                        ref.set(requester.cache_key(),response)

    # BENCHMARKING SEARCH
    print(u'\nSEARCH')
    if len(requesters) > 0:
        print(f"{len(requesters)} calls")
    if (len(searchers)-len(requesters)) > 0:
        print(f"{len(searchers)-len(requesters)} cached responses")
    print(f'{search_duration} seconds')


    # BENCHMARKING RETRIEVAL
    count = 0
    for searcher in searchers:
        count += len(searcher.retrievals)

    print(u'\nRETRIEVAL')
    if len(requesters) > 0:
        print(f"{len(requesters)} calls")
    print(f'{count} retrievals')
    retrieval_duration = round((time.time() - start),2)
    print(f'{retrieval_duration-search_duration} seconds')

    # CREATE ART OBJECTS
    artworks = []
    all_created = True
    for searcher in searchers:
        for retrieval in searcher.retrievals:
            try:
                artworks.append(searcher.item(retrieval,relevance=1))
            except:
                all_created = False
                searcher.save_sample_file(retrieval)
                print('Instance could not be created for',searcher.museum,'object--sample file created')

    # CREATE PAGE
    # page = present(artworks,all_created)
    # print(page)

    return artworks

def celer():

    # GET SEARCH INPUT
    prompt = u'\nWelcome to Imago Mundi\nYou can enter...\n- a search term\n- "exit" to quit'
    artworks = []
    print(prompt)
    while True:
        q = input(u'> ')
        try:
            n = int(q)
            item = sorted(artworks, key = lambda work:work.relevance,
                reverse=True)[n-1]
            url = item.imageReferences['primaryImage']
            wb.open(url)
        except:
            if q == u"exit":
                print(u"\nBye!\n")
                break
            else:
                print(u'\n')
                artworks = revolve(active_apis=active_apis,q=q)
                prompt = u'\nYou can enter...\n- a search term\n- "exit" to quit\n- the number of an item to view in browser'
                print(prompt)

if __name__ == "__main__":
    celer()
