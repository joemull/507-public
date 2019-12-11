import requests
import json
from bs4 import BeautifulSoup
from diskcache import Cache
from formats import JSON, XML
from museums import met, rijks, harvard, europeana, rmn, walters, vkc, vkc_oai
import api_keys
import debug
import datetime
import os
import time
import asyncio
import aiohttp


class API:
    def __init__(self):
        self.description = "An API"
        self.retrieves = True
        self.params = {}
        self.headers = {}
        self.headers['User-Agent'] = "jhmuller@umich.edu"
        self.limit = 20
        self.resumptionListSize = 0
        self.resumptionExpiresIn = datetime.timedelta(hours=48)

    def __str__(self):
        return self.name

    def cache_key(self):
        res = []
        for k in sorted(self.params.keys()):
            if str(self.params[k]) not in self.api_key:
                res.append("{}-{}".format(k, self.params[k]))
        return self.base + "_" + "_".join(res)

    def add_param(self,k,v):
        self.params[k] = v

    def save_sample_file(self,data):

        sample_dir = "sample_responses"
        if not os.path.exists(sample_dir):
            os.mkdir(sample_dir)

        extension = self.MIMEType().split('/')[-1]
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        fileref = sample_dir + "/" + self.museum + "_" + timestamp + "." + extension

        with open(fileref,'w') as sample:
            sample.write(self.cast(data))

    async def get(self,session):
        async with session.get(self.base,params=self.params,
            headers=self.headers) as response:
                # self.ids = self.list_ids(self.hits)
                # self.count = self.count_results(self.hits)
            # print('\n')
            # print(self.name)
            # print(response.status)
            if response.status != 200:
                print(self.museum,response.status)
                print(self.base,self.params)
            return self, (await response.text())


class OAI_PMH:
    def extract_resumption(self):
        try:
            return self.hits.find('resumptionToken').string.strip()
        except:
            return 'expired'

    def prepare(self):
        if self.resumption != 'expired':
            return {
                'resumptionToken' : self.resumption,
                'verb' : "ListRecords",
            }
        else:
            return {
                'metadataPrefix' : "europeana_edm",
                'verb' : "ListRecords",
            }


# class Search(API):
#     def do_the_thing(self):
#         pass
#
# class Retrieve(API):
#     def respond(self):
#         pass
    # def respond(self,ref,id='436155'): # Not being called in current program?
        # self.params = self.prepare(id)
        # if self.cache_key() in ref:
        #     # print('Returning cached record for',self.name)
        #     return self.get_from_cache(ref,self.cache_key())
        # else:
        #     # print('Getting record from',self.name)
        #     record = self.format(requests.get(self.base,self.params))
        #     self.save_to_cache(ref,record)
        #     return record

# class Harvest(API):
#     def respond(self,ref=None,id=None):
#         return self.format(requests.get(self.base).text)

# class SPARQL(API):
#     def respond(self,ref):
#         if self.cache_key() in ref:
#             print('Returning cached data for',self.name)
#             return self.get_from_cache(ref,self.cache_key())
#         else:
#             print('Getting new data from',self.name)
#             response = requests.get(self.base,
#                 params=self.params,headers=self.headers)
#             results = self.format(response)
#             self.save_to_cache(ref,results)
#             return results


##### Europeana #####

##### Le Louvre / Grand-Palais / Images d'Art #####
class ImagesdArt(API,JSON):
    def __init__(self):
        super().__init__()
        self.name = "Réunion des Musées Nationaux"
        self.website = "https://api.art.rmngp.fr/?locale=en"
        self.base = "https://api.art.rmngp.fr/v1/works"
        self.api_key = api_keys.ks()['Grand-Palais']
        self.headers['ApiKey'] = self.api_key
        self.museum = 'RMN'

    def item(self,record,relevance):
        return rmn.RMNItem(record,relevance)

    def list_ids(self):
        ids = []
        for rec in self.hits['hits']['hits']:
            ids.append(rec['_id'])
        return ids

    def list_records(self):
        return self.hits['hits']['hits']

    def count_results(self,results):
        return int(results['hits']['total'])

    def prepare(self,q):
        self.add_param('q',q)

# class ImagesdArtHarvest(ImagesdArt):
#     def __init__(self):
#         super().__init__()
#         self.base = 'https://api.art.rmngp.fr:443/v1/works'
#
#     def prepare(self):
#         pass
#
#     def check_list_size(self):
#         pass

##### Het Rijksmuseum #####
class Rijks(API,XML):
    def __init__(self):
        super().__init__()
        self.website = "http://rijksmuseum.github.io/"
        self.api_key = api_keys.ks()['Rijks']
        self.museum = "Rijksmuseum"

    def item(self,record,relevance):
        return rijks.RijksItem(record,relevance)

    def count_results(self,results):
        count = results.find('Count')
        return int(count.string.strip())

    def retriever(self):
        return RijksRetrieve()

class RijksSearch(Rijks):
    def __init__(self):
        super().__init__()
        self.name = "the Rijksmuseum Search API"
        self.retrieves = False
        self.params['q'] = ''
        self.params['key'] = self.api_key
        self.params['format'] = 'xml'
        self.base = "https://www.rijksmuseum.nl/api/en/collection"

    def list_ids(self):
        ids = []
        objs = self.hits.find_all('ArtObjects')
        for obj in objs:
            ids.append(obj.ObjectNumber.string.strip())
        # print(ids)
        return ids

class RijksRetrieve(Rijks):
    def __init__(self):
        super().__init__()
        self.name = "the Rijksmuseum Retrieval API"

    def format_base(self,id):
        return "https://www.rijksmuseum.nl/api/oai/" + self.api_key

    def format_params(self,id):
        params = {}
        params['verb'] = "GetRecord"
        params['metadataPrefix'] = "europeana_edm"
        params['identifier'] = 'oai:rijksmuseum.nl:' + str(id)
        return params

class RijksHarvest(Rijks,OAI_PMH):
    def __init__(self):
        super().__init__()
        self.name = "the Rijksmuseum Harvest Endpoint"
        self.retrieves = True
        self.base = "https://www.rijksmuseum.nl/api/oai/" + self.api_key
        self.params = {}
        self.params['metadataPrefix'] = "europeana_edm"
        self.resumption = 'expired'
        self.listSize = 0
        self.resumptionExpiresIn = datetime.timedelta(minutes=14)

    def list_records(self):
        return self.hits.find_all("record")

    def list_ids(self):
        ids = []
        for rec in self.list_records():
            ids.append(rec.find("oai:identifier").string.split(':')[-1].strip())
        return ids

    def count_results(self,results):
        pass


    def check_list_size(self):
        self.listSize = int(self.hits.find('resumptionToken')['completeListSize'])

# LIDO https://www.rijksmuseum.nl/api/oai2/2MNHREj3/?verb=GetRecord&identifier=oai:rijksmuseum.nl:sk-c-5&metadataPrefix=lido
# DC JSON https://www.rijksmuseum.nl/api/oai2/2MNHREj3/?verb=GetRecord&identifier=oai:rijksmuseum.nl:sk-c-5&metadataPrefix=oai_dc

##### The Metropolitan Museum of Art #####

class Met(API,JSON):
    def __init__(self):
        super().__init__()
        self.website = "https://metmuseum.github.io/"
        self.api_key = ''
        self.museum = "Met"
        self.resumptionExpiresIn = datetime.timedelta(days=365)
        self.resumption = 'expired'

    def item(self,record,relevance):
        return met.MetItem(record,relevance)

    def list_ids(self):
        return self.hits['objectIDs']

    def count_results(self,results):
        return int(results['total'])

    def retriever(self):
        return MetRetrieve()

class MetSearch(Met):
    def __init__(self):
        super().__init__()
        self.name = "the Met Search API"
        self.retrieves = False
        self.base = "https://collectionapi.metmuseum.org/public/collection/v1/search"
        self.params['q'] = ''

class MetRetrieve(Met):
    def __init__(self):
        super().__init__()
        self.name = "the Met Retrieval API"

    def format_base(self,id):
        return "https://collectionapi.metmuseum.org/public/collection/v1/objects/" + str(id)

    def format_params(self,id):
        return {}

    def prepare(self):
        pass

class MetHarvest(Met):
    def __init__(self):
        super().__init__()
        self.name = "The Met Harvest API"
        self.base =  "https://collectionapi.metmuseum.org/public/collection/v1/objects"
        self.retrieves = False

    def prepare(self):
        return {}

    def check_list_size(self):
        self.listSize = len(self.list_ids())
        print(self.listSize)

##### Harvard Art Museums #####

class Harvard(API,JSON):
    def __init__(self):
        super().__init__()
        self.museum = 'Harvard'
        self.name = 'the Harvard Art Museums API'
        self.base = 'https://api.harvardartmuseums.org/object'
        self.api_key = api_keys.ks()['Harvard']
        self.params['apikey'] = self.api_key
        self.params['q'] = ''
        self.params['size'] = 20

    def item(self,record,relevance):
        return harvard.HarvardItem(record,relevance)

    def list_ids(self):
        ids = []
        for rec in self.hits['records']:
            ids.append(rec['objectnumber'])
        return ids

    def list_records(self):
        return self.hits['records']

    def count_results(self,results):
        return int(results['info']['totalrecords'])

##### EUROPEANA #####

class Europeana(API):
    def __init__(self):
        super().__init__()
        self.museum = 'Europeana'

class EuSearch(Europeana,JSON):
    def __init__(self):
        super().__init__()
        self.name = 'the Europeana API'
        self.base = 'https://api.europeana.eu/api/v2/search.json'
        self.api_key = api_keys.ks()['Europeana']
        self.params['thumbnail'] = 'True'
        self.params['media'] = 'True'
        self.params['wskey'] = self.api_key
        # "https://api.europeana.eu/api/v2/search.json?profile=standard&query=degas&rows=12&start=1&wskey=hHkunfvCe"

    def item(self,record,relevance):
        return europeana.EuropeanaItem(record,relevance)

    def list_ids(self):
        ids = []
        for rec in self.hits['items']:
            ids.append(rec['id'])
        return ids

    def list_records(self):
        return self.hits['items']

    def count_results(self,results):
        return int(results['totalResults'])

    def prepare(self,q):
        self.add_param('query',q)


# class EuSPARQL(SPARQL,Europeana,JSON):
#     def __init__(self):
#         super().__init__()
#         self.name = "The Europeana SPARQL API"
#         self.params['format'] = 'application/json'
#         self.params['query'] = ''
#         self.base = 'http://sparql.europeana.eu/'


##### Digital Public Library of America #####

class DPLA(API,JSON):
    def __init__(self):
        super().__init__()
        self.base = "https://api.dp.la/v2"


##### The Walters Art Museum, Baltimore #####

class Walters(API,JSON):
    def __init__(self):
        super().__init__()
        self.name = "The Walters Art Museum"
        self.museum = "Walters"
        self.base = "http://api.thewalters.org/v1/objects"
        self.api_key = api_keys.ks()['Walters']
        self.params['apikey'] = self.api_key
        self.params['keyword'] = 'degas'
        self.headers['Accept'] = 'JSON'

    def item(self,record,relevance):
        return walters.WaltersItem(record,relevance,self.museum)

    def list_ids(self):
        ids = []
        if 'Items' in self.hits:
            for rec in self.hits['Items']:
                ids.append(rec['ObjectID'])
        return ids

    def list_records(self):
        return self.hits['Items']

    def count_results(self,results):
        return len(results['Items'])

    def prepare(self,q):
        self.add_param('keyword',q)



##### The Flemish Art Collection ######

# https://arthub.vlaamsekunstcollectie.be/nl/handleiding
class VKC(API):
    def __init__(self):
        super().__init__()
        self.name = "De Vlaamse Kunst Collectie"
        self.museum = "Flemish"
        self.api_key = ''

    def item(self,record,relevance):
        return vkc.VKCItem(record,relevance,self.museum)

    def list_ids(self):
        ids = []
        if 'docs' in self.hits:
            for rec in self.hits['docs']:
                ids.append(rec['id'])
        return ids

    def list_records(self):
        return self.hits['docs']

    def count_results(self,results):
        return int(results['response']['pages']['total_count'])

class FlemishSearch(VKC,JSON):
    def __init__(self):
        super().__init__()
        self.retrieves = False
        self.base = 'https://arthub.vlaamsekunstcollectie.be/nl/catalog.json'
        self.params['q'] = 'bosch'

    def retriever(self):
        return FlemishRetrieve()

    def follow(self):
        return FlemishRetrieve()

class FlemishRetrieve(VKC,XML):

    def format_base(self,id):
        return 'https://arthub.vlaamsekunstcollectie.be/nl/catalog/{}.xml'.format(str(id))

    def format_params(self,id):
        return {}

class FlemishHarvest(VKC,XML,OAI_PMH):
    def __init__(self):
        super().__init__()
        self.retrieves = True
        self.base = "https://datahub.vlaamsekunstcollectie.be/oai/"
        self.listSize = 0
        self.resumption = 'expired'

    def list_records(self):
        return self.hits.find_all("record")

    def check_list_size(self):
        self.listSize = int(self.hits.find('resumptionToken')['completeListSize'])

    def item(self,record,relevance):
        return vkc_oai.VKCItem(record,relevance,self.museum)

    def prepare(self):
        if self.resumption != 'expired':
            return {
                'resumptionToken' : self.resumption,
                'verb' : "ListRecords",
            }
        else:
            return {
                'metadataPrefix' : "oai_lido",
                'verb' : "ListRecords",
            }

class GooglePlaces(API,JSON):
    def __init__(self):
        super().__init__()
        self.api_key = api_keys.ks()['googlePlaces']
        self.base = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
        self.params = {}
        self.params['key'] = self.api_key
        self.params['inputtype'] = 'textquery'
        self.params['fields'] = 'geometry'

    def prepare(self,museumNameAndLoc):
        self.params['input'] = museumNameAndLoc

    def list_records(self):
        return self.hits['candidates']


### OTHERS
# http://www.vlaamsekunstcollectie.be/nl/page_8F847B37-D5A8-4F7F-8426-4A250C10AC43_nl.aspx
# https://www.vam.ac.uk/api/
