import unittest
import apis
import harvest
import relevance
import model
from bs4 import BeautifulSoup
from museums import met, rijks, harvard, europeana, rmn, walters, vkc, vkc_oai

class TestAPIs(unittest.TestCase):
    def testURL(self):

        met = apis.MetHarvest()
        met.prepare()
        self.assertEqual(met.base,"https://collectionapi.metmuseum.org/public/collection/v1/objects")

        rijks = apis.RijksHarvest()
        rijks.resumption = "s3275832094dfs0jasf09ajf0qw9fjqw0ef9jqefqf923h29382"
        rijks.prepare()
        with self.assertRaises(Exception):
            should_be_gone = met.params['metadataPrefix']

        goog = apis.GooglePlaces()
        goog.prepare('museum')
        self.assertEqual(goog.params['input'],'museum')

    def testCategory(self):

        met = apis.MetHarvest()
        self.assertEqual(met.retrieves,False)

        flem = apis.FlemishHarvest()
        self.assertEqual(flem.retrieves,True)

        goog = apis.GooglePlaces()
        self.assertEqual(goog.MIMEType(),"application/json")

    def testGooglePlaces(self):
        work = rijks.RijksItem(BeautifulSoup('<identifier>0123:r45</identifier><title>An artwork</title>','html.parser'),relevance=1)
        work.currentRepo = 'Walters Art Museum'
        locWorks = model.locate([work])
        self.assertEqual(round(locWorks[0].lat),39)

class TestHarvesting(unittest.TestCase):
    def testResponding(self):

        api_list = [
            apis.MetHarvest(),
            apis.RijksHarvest(),
            apis.FlemishHarvest(),
        ]

        req_resp_tuples = harvest.request_with_aio(api_list)

        met, metResponse = req_resp_tuples[0]
        met.hits = met.format(metResponse)
        self.assertGreater(len(met.list_ids()),100000)

        rijks, rijksResponse = req_resp_tuples[1]
        rijks.hits = rijks.format(rijksResponse)
        self.assertGreater(len(rijks.list_records()),15)

        flem, flemResponse = req_resp_tuples[2]
        flem.hits = flem.format(flemResponse)
        self.assertGreater(len(flem.list_records()),15)
        flem.resumption = flem.extract_resumption()
        self.assertGreater(len(flem.resumption),10)


class TestDataBase(unittest.TestCase):
    def testInitAndAdd(self):
        testing_db = 'testing01.db'
        model.init_db(testing_db)
        with self.assertRaises(Exception):
            artworks = model.query_title('tree')

        item = rijks.RijksItem(BeautifulSoup('<identifier>0123:r45</identifier><title>An artwork</title>','html.parser'),relevance=1)
        self.assertEqual(model.check_db('titleText','An artwork',testing_db),False)

        model.add_works([item],testing_db)
        self.assertEqual(model.check_db('titleText','An artwork',testing_db),True)

    def testIndexing(self):
        testing_db = 'testing01.db'
        model.init_db(testing_db)
        item = rijks.RijksItem(BeautifulSoup('<identifier>0123:r45</identifier><title>An painting of an aardvark</title>','html.parser'),relevance=1)
        model.add_works([item],testing_db)

        new_index = relevance.get_standard_index(testing_db)
        model.rebuild_index(new_index,testing_db)
        works = model.search_index('aardvark',testing_db)
        self.assertGreater(len(works),0)


unittest.main()
