from cdwa import Item, Image, PersonOrCorporateBody, PlaceOrLocation, GenericConcept, Subject

class RMNItem(Item):
    def __init__(self,rec,relevance):

        # Imago Mundi administrative metadata
        self.pid = u"-".join(['RMN',str(rec["_id"]),"item"])
        self.relevance = relevance

        # 3.1. Title Text
        self.titleText = rec['_source']['title']['fr']

        # 21.2. Repository/Geographic Location
        try:
            self.currentRepositoryGeographicLocation = rec['_source']['location']['name']['en'] + ', ' + rec['_source']['location']['city']['en']
        except:
            self.currentRepositoryGeographicLocation = rec['_source']['location']['name']['fr'] + ', ' + rec['_source']['location']['city']['fr']

        # 26. RELATED VISUAL DOCUMENTATION
        # [references to Object/Work]
        # 26.1. Image References
        # 26.1.1. Image to Work Relationship Type
        self.imageReferences = {}
        try:
            self.imageReferences['primaryImage'] = rec['_source']['images'][0]['urls']['original']
        except:
            self.imageReferences['primaryImage'] = rec['_source']['images'][0]['urls']['huge']['url']
        # print(self.imageReferences['primaryImage'])
