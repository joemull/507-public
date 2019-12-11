from cdwa import Item, Image, PersonOrCorporateBody, PlaceOrLocation, GenericConcept, Subject

class EuropeanaItem(Item):
    def __init__(self,rec,relevance):

        # Imago Mundi administrative metadata
        self.pid = u"-".join(['Europeana',str(rec['id']),"item"])
        self.relevance = relevance

        # 3.1. Title Text
        self.titleText = rec['title'][0]

        # 21.2. Repository/Geographic Location
        self.currentRepositoryGeographicLocation = rec['dataProvider'][0] + ', ' + rec['country'][0]

        # 26. RELATED VISUAL DOCUMENTATION
        # [references to Object/Work]
        # 26.1. Image References
        # 26.1.1. Image to Work Relationship Type
        self.imageReferences = {}
        try:
            self.imageReferences['primaryImage'] = rec['edmIsShownBy'][0]
        except:
            self.imageReferences['primaryImage'] = rec['edmPreview'][0]
