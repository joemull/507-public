from cdwa import Item, Image, PersonOrCorporateBody, PlaceOrLocation, GenericConcept, Subject
from formats import JSON, XML

class WaltersItem(Item,XML):
    def __init__(self,rec,relevance,museum):

        # Imago Mundi administrative metadata
        self.pid = u"-".join([museum,str(rec["ObjectID"]),"item"])
        self.relevance = relevance

        # 3.1. Title Text
        self.titleText = rec['Title']

        # 21.2. Repository/Geographic Location
        self.currentRepositoryGeographicLocation = 'Walters Art Museum, Baltimore'

        # 26. RELATED VISUAL DOCUMENTATION
        # [references to Object/Work]
        # 26.1. Image References
        # 26.1.1. Image to Work Relationship Type
        self.imageReferences = {}
        try:
            self.imageReferences['primaryImage'] = rec['PrimaryImage']['Large']
        except:
            self.imageReferences['primaryImage'] = rec['PrimaryImage']['Raw']
        # print(self.imageReferences['primaryImage'])
