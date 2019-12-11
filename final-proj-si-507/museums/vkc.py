from cdwa import Item, Image, PersonOrCorporateBody, PlaceOrLocation, GenericConcept, Subject

class VKCItem(Item):
    def __init__(self,rec,relevance,museum):

        # Imago Mundi administrative metadata
        id = rec.find("lidoRecID",attrs={"lido:type":"urn"}).string.strip()
        self.pid = u"-".join([museum,str(id),"item"])
        self.relevance = relevance

        # 21.2. Repository/Geographic Location
        self.currentRepositoryGeographicLocation = rec.find('repositoryName').string.strip()

        # 3.1. Title Text
        self.titleText = rec.find('title').string.strip()

        # 26. RELATED VISUAL DOCUMENTATION
        # [references to Object/Work]
        # 26.1. Image References
        # 26.1.1. Image to Work Relationship Type
        self.imageReferences = {}
        self.imageReferences['primaryImage'] = rec.find('WebResource')['rdf:about']
