from cdwa import Item, Image, PersonOrCorporateBody, PlaceOrLocation, GenericConcept, Subject
from formats import JSON, XML

class MetItem(Item,JSON):
    def __init__(self,rec,relevance):

        # Imago Mundi administrative metadata
        self.pid = u"-".join(['Met',str(rec['objectID']),"item"])
        self.relevance = relevance
        self.originalRecord = self.cast(rec)


        # 3.1. Title Text
        self.titleText = rec['title']

        # 4. CREATION
        # 4.1. Creator Description
        try:
            self.creatorDescription = rec['artistDisplayName']
        except:
            self.creatorDescription = "Creator Unspecified"

        # 21.2. Repository/Geographic Location
        try:
            self.currentRepo = rec['repository'].split(',')[0]
        except:
            self.currentRepo = "Location Unspecified"

        # 21.3. Object/Work Label/Identification
        # self.objectLabel = {}
        # self.objectLabel['objectID'] = rec['objectID']
        # self.objectLabel['accessionNumber'] = rec['accessionNumber']

        # 22.1. Copyright Statement
        if rec['isPublicDomain'] == True:
            self.copyrightStatement = "Public Domain"
        else:
            self.copyrightStatement = "Not Public Domain"


        # 26. RELATED VISUAL DOCUMENTATION
        # [references to Object/Work]
        # 26.1. Image References
        # 26.1.1. Image to Work Relationship Type
        self.imageReferences = {}
        try:
            self.imageReferences['primaryImage'] = rec['primaryImage']
            self.imageReferences['primaryImageSmall'] = rec['primaryImageSmall']
        except:
            self.imageReferences['primaryImage'] = "No Image"
            self.imageReferences['primaryImageSmall'] = "No Image"
        # self.imageReferences['additionalImages'] = rec['additionalImages']

        # 27. RELATED TEXTUAL REFERENCES
        self.textualReferences = {}
        self.textualReferences['referenceURL'] = rec['objectURL']

    def attach_images(self):
        # create instances of Image class
        pass

class MetImage(Image):
    def __init__(self,o):
        pass



# Keys of JSON response
# objectID
# isHighlight
# accessionNumber
# isPublicDomain
# primaryImage
# primaryImageSmall
# additionalImages
# constituents
# department
# objectName
# title
# culture
# period
# dynasty
# reign
# portfolio
# artistRole
# artistPrefix
# artistDisplayName
# artistDisplayBio
# artistSuffix
# artistAlphaSort
# artistNationality
# artistBeginDate
# artistEndDate
# objectDate
# objectBeginDate
# objectEndDate
# medium
# dimensions
# creditLine
# geographyType
# city
# state
# county
# country
# region
# subregion
# locale
# locus
# excavation
# river
# classification
# rightsAndReproduction
# linkResource
# metadataDate
# repository
# objectURL
# tags
