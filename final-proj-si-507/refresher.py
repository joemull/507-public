
class Item:
    def __init__(self,rec):

        # Imago Mundi administrative metadata
        self.pid = rec[1]
        self.relevance = rec[2]

        # 3.1. Title Text
        self.titleText = rec[6]

        # 4. CREATION
        # 4.1. Creator Description
        self.creatorDescription = rec[7]

        # 21.2. Repository/Geographic Location
        self.currentRepo = rec[16]

        # 22.1. Copyright Statement
        self.copyrightStatement = rec[18]

        # 26. RELATED VISUAL DOCUMENTATION
        # [references to Object/Work]
        # 26.1. Image References
        # 26.1.1. Image to Work Relationship Type
        self.imageReferences = {}
        self.imageReferences['primaryImage'] = rec[19]
        self.imageReferences['primaryImageSmall'] = rec[20]

        # 27. RELATED TEXTUAL REFERENCES
        self.textualReferences = {}
        self.textualReferences['referenceURL'] = rec[21]

        self.weight = rec[28]
        # print(self.weight,self.titleText)
