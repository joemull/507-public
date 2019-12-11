from cdwa import Item, Image, PersonOrCorporateBody, PlaceOrLocation, GenericConcept, Subject
from formats import JSON, XML

class RijksItem(Item,XML):
    def __init__(self,rec,relevance):

        # Imago Mundi administrative metadata
        id = rec.find('identifier').string.split(':')[-1].strip()
        self.pid = u"-".join(['Rijks',str(id),"item"])
        self.relevance = relevance
        self.originalRecord = self.cast(rec)

        # 3.1. Title Text
        try:
            self.titleText = rec.find('title').string.strip()
        except:
            self.titleText = rec.find_all('title')[1].string.strip()

        # 4. CREATION
        # 4.1. Creator Description
        try:
            self.creatorDescription = rec.find("dc:creator").string.strip()
        except:
            self.creatorDescription = "Unspecified Creator"

        # 21.2. Repository/Geographic Location
        try:
            self.currentRepo = rec.find('dataProvider').string.strip()
        except:
            self.currentRepo = "Location Unspecified"

        # 22.1. Copyright Statement
        try:
            self.copyrightStatement = rec.find("dc:rights").string.strip()
        except:
            self.copyrightStatement = "Copyright Unspecified"

        # 26. RELATED VISUAL DOCUMENTATION
        # [references to Object/Work]
        # 26.1. Image References
        # 26.1.1. Image to Work Relationship Type
        self.imageReferences = {}
        try:
            self.imageReferences['primaryImage'] = rec.find('WebResource')['rdf:about']
        except:
            self.imageReferences['primaryImage'] = "None"
        self.imageReferences['primaryImageSmall'] = self.imageReferences['primaryImage']

        # 27. RELATED TEXTUAL REFERENCES
        self.textualReferences = {}
        try:
            self.textualReferences['referenceURL'] = rec.find('dc:identifier').string.strip()
        except:
            try:
                self.textualReferences['referenceURL'] = rec.find('edm:isShownAt').attrs['rdf:resource']
            except:
                self.textualReferences['referenceURL'] = "No Record URL"
