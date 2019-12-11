from cdwa import Item, Image, PersonOrCorporateBody, PlaceOrLocation, GenericConcept, Subject
from formats import JSON, XML

class VKCItem(Item,XML):
    def __init__(self,rec,relevance,museum):

        # Imago Mundi administrative metadata
        id = rec.find("lidoRecID",attrs={"lido:type":"urn"}).string.strip()
        self.pid = u"-".join([museum,str(id),"item"])
        self.relevance = relevance
        self.originalRecord = self.cast(rec)

        # 3.1. Title Text
        try:
            titleSet = rec.find('titleSet')
            self.titleText = titleSet.find('lido:appellationValue').string.strip()
        except:
            self.titleText = "Unspecified Title"

        # 4. CREATION
        # 4.1. Creator Description
        try:
            actor = rec.find('lido:actor')
            self.creatorDescription = actor.find('appellationValue').string.strip()
        except:
            self.creatorDescription = "Unspecified Creator"

        # 21.2. Repository/Geographic Location
        try:
            repName = rec.find('repositoryName')
            self.currentRepo = repName.find('lido:appellationValue').string.strip()
        except:
            self.currentRepo = "Unspecified Repository"

        # 22.1. Copyright Statement
        self.copyrightStatement = "Possibly under copyright"

        # 26. RELATED VISUAL DOCUMENTATION
        # [references to Object/Work]
        # 26.1. Image References
        # 26.1.1. Image to Work Relationship Type
        self.imageReferences = {}
        try:
            resourceRep = rec.find('lido:resourceRepresentation')
            self.imageReferences['primaryImage'] = resourceRep.find('lido:linkResource').string.strip()
        except:
            self.imageReferences['primaryImage'] = "No Image"
        self.imageReferences['primaryImageSmall'] = self.imageReferences['primaryImage']

        # 27. RELATED TEXTUAL REFERENCES
        self.textualReferences = {}
        try:
            self.textualReferences['referenceURL'] = rec.find('lido:recordID').string.strip()
        except:
            try:
                self.textualReferences['referenceURL'] = rec.find('lido:legalBodyWeblink').string.strip()
            except:
                self.textualReferences['referenceURL'] = "None Record URL"
