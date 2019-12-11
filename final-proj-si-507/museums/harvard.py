from cdwa import Item, Image, PersonOrCorporateBody, PlaceOrLocation, GenericConcept, Subject

class HarvardItem(Item):
    def __init__(self,rec,relevance):

        # Imago Mundi administrative metadata
        self.pid = u"-".join(['Harvard',str(rec['objectnumber']),"item"])
        self.relevance = relevance

        # 3.1. Title Text
        self.titleText = rec['title']

        # 21.2. Repository/Geographic Location
        self.currentRepositoryGeographicLocation = rec['creditline'].split('/')[0]

        # 26. RELATED VISUAL DOCUMENTATION
        # [references to Object/Work]
        # 26.1. Image References
        # 26.1.1. Image to Work Relationship Type
        self.imageReferences = {}
        try:
            self.imageReferences['primaryImage'] = rec['primaryimageurl']
        except:
            self.imageReferences['primaryImage'] = rec['url']
