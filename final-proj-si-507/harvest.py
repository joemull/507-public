from tqdm import tqdm
import sys
import apis
import aio
import asyncio
import model
from diskcache import Cache
import relevance
from safeprint import print

testing = 'test-db-507.db'
production = 'aby02-507.db'

def request_with_aio(apis):
    for api in apis:
        api.params = api.prepare()
        # print(api.base,api.params)
    return asyncio.run(aio.manage_requests(apis))

def run():

    initial_harvesters = [
        apis.RijksHarvest(),
        apis.MetHarvest(),
        apis.FlemishHarvest(),
    ]

    # initial_harvesters = []
    # for har in harvesters:
    #     token = model.get_resumption(har.museum)
    #     if token != None:
    #         har.resume(token)
    #     else:
    #         initial_harvesters.append(har)

    for har in initial_harvesters:
        if har.retrieves == True:
            har.resumption = model.get_resumption(har.museum,har.resumptionExpiresIn)

    req_resp_tuples = request_with_aio(initial_harvesters)


    artworks = []
    for har, first_response in req_resp_tuples:
        har.hits = har.format(first_response)
        # har.save_sample_file(har.hits)

        # if har.museum == "Flemish":
            # print(first_response)
            # print(har.resumption)

        if har.retrieves == False:
            har.stable_id_list = har.list_ids()
            har.resumption = model.get_resumption(har.museum,har.resumptionExpiresIn)

        # har.check_list_size()
        har.listSize = 600000
        if har.retrieves == True:
            for rec in har.list_records():
                artworks.append(har.item(rec,relevance=1))

    model.add_works(artworks)

    maxList = 0
    for har in initial_harvesters:
        if har.listSize > maxList:
            maxList = har.listSize + 1
    maxRounds = maxList

    # CONTROL
    print('Without control, the number of rounds would be',str(maxRounds))
    maxRounds = 3

    for rnd in tqdm(range(0,maxRounds)):
        artworks = []
        continuing_harvesters = []
        retriever_set = []
        for har in initial_harvesters:
            if har.retrieves == True:
                har.resumption = har.extract_resumption()
            if har.resumption != 'expired':
                continuing_harvesters.append(har)
                model.save_resumption(har.museum,har.resumption)
            if har.retrieves == False:
                setSize = 5
                for ea in range(0, setSize):
                    ret = har.retriever()
                    this_id = 100000000
                    # print('testing',this_id)
                    if har.resumption == 'expired':
                        this_id = har.stable_id_list.pop()
                    else:
                        while this_id > int(har.resumption):
                            this_id = har.stable_id_list.pop()

                    # print('settled on',this_id)
                    model.save_resumption(har.museum,this_id)
                    new_id = this_id
                    if model.check_db('pid',new_id) == False:
                        ret.base = ret.format_base(new_id)
                        ret.params = ret.format_params(new_id)
                        retriever_set.append(ret)

        for har, resp in request_with_aio(continuing_harvesters):
            if har.retrieves == True:
                har.hits = har.format(resp)
                for rec in har.list_records():
                    artworks.append(har.item(rec,relevance=1))
                print(artworks[-1].titleText,"- last in set from ",har.museum)

        for retriever, response in request_with_aio(retriever_set):
            artworks.append(retriever.item(retriever.format(response),relevance=1))
        print(artworks[-1].titleText,"- last in set from ",retriever.museum)

        model.add_works(artworks)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == '--init':
        confirmation = input('About to delete database"',production,'". Continue? Y/N')
        if confirmation == 'Y':
            print('Deleting database and starting over from scratch.')
            model.init_db(production)
        else:
            print('Leaving database alone.')
    else:
        print("Leaving database alone. Append '--init' to delete database and reinitiate.")

    if len(sys.argv) > 1 and sys.argv[1] == '--resume':
        run()
    else:
        print("Not resuming yet. Append '--resume' to resume harvest.")

    if len(sys.argv) > 1 and sys.argv[1] == '--index':
        print("Rebuilding index...")
        abyIndex = relevance.get_standard_index()
        model.rebuild_index(abyIndex)
    else:
        print("Not indexing yet. Append '--index' to index.")
