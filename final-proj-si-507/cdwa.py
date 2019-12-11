class Item:

    CDWA = "February 28, 2019"

    def __init__(self):
        # 1. OBJECT/WORK
        # 1.1. Catalog Level
        self.catalogLevel = 'item'
        # 1.2. Object/Work Type
        self.workType = 'No Work Type'
        # 1.3. Object/Work Type Date
        # 1.3.1. Earliest Date
        # 1.3.2. Latest Date
        # 1.4. Components/Parts
        # 1.4.1 Components Quantity
        # 1.4.2 Components Type
        # 1.5. Remarks
        # 1.6. Citations
        # 1.6.1. Page
        #
        # 2. CLASSIFICATION
        # 2.1. Classification Term
        self.classificationTerm = 'No Classification Term'
        # 2.2. Remarks
        # 2.3. Citations
        # 2.3.1. Page
        #
        # 3. TITLES OR NAMES
        # 3.1. Title Text
        self.titleText = 'No Title Text'
        # 3.2. Title Type
        # 3.3. Preference
        # 3.4. Title Language
        # 3.5. Title Date
        # 3.5.1. Earliest Date
        # 3.5.2. Latest Date
        # 3.6. Remarks
        # 3.7. Citations
        # 3.7.1. Page
        #
        # 4. CREATION
        # 4.1. Creator Description
        self.creatorDescription = 'No Creator Description'
        # 4.1.1. Creator Extent
        # 4.1.2. Qualifier
        # 4.1.3. Creator Identity
        self.creatorIdentity = 'No Creator Identity'
        # 4.1.4. Creator Role
        self.creatorRole = 'No Creator Role'
        # 4.1.5. Creator Statement
        # 4.2. Creation Date
        self.creationDate = 'No Creation Date'
        # 4.2.1. Earliest Date
        self.earliestDate = 'No Earliest Date'
        # 4.2.2. Latest Date
        self.latestDate = 'No Latest Date'
        # 4.2.3. Date Qualifier
        # 4.3. Creation Place/Original Location
        # 4.3.1. Place Qualifier
        # 4.4. Object/Work Culture
        # 4.5. Commissioner
        # 4.5.1. Commissioner Role
        # 4.5.2. Commission Date
        # 4.5.2.1. Earliest Date
        # 4.5.2.2. Latest Date
        # 4.5.3. Commission Place
        # 4.5.4. Commission Cost
        # 4.6. Creation Numbers
        # 4.6.1. Number Type
        # 4.7. Remarks
        # 4.8. Citations
        # 4.8.1. Page
        #
        # 5. STYLES/PERIODS/GROUPS/ MOVEMENTS
        # 5.1. Styles/Periods Description
        # 5.2. Styles/Periods Indexing Terms
        # 5.2.1. Term Qualifier
        # 5.3. Remarks
        # 5.4. Citations
        # 5.4.1. Page
        #
        # 6. MEASUREMENTS
        # 6.1. Dimensions Description
        self.dimensionsDescription = 'No Dimensions Description'
        # 6.2. Dimensions Type
        # 6.3. Dimensions Value
        # 6.4. Dimensions Unit
        # 6.5. Dimensions Extent
        # 6.6. Scale Type
        # 6.7. Dimensions Qualifier
        # 6.8. Dimensions Date
        # 6.8.1. Earliest Date
        # 6.8.2. Latest Date
        # 6.9. Shape
        # 6.10. Format/Size
        # 6.11. Remarks
        # 6.12. Citations
        # 6.12.1. Page
        #
        # 7. MATERIALS/TECHNIQUES
        # 7.1. Materials/Techniques Description
        self.materialsTechniquesDescription = 'No Materials/Techniques Description'
        # 7.2. Materials/Techniques Flag
        # 7.3. Materials/Techniques Extent
        # 7.4. Materials/Techniques Role
        # 7.5. Materials/Techniques Name
        # 7.6. Material Color
        # 7.7. Material Source Place
        # 7.8. Watermarks
        # 7.8.1. Watermark Identification
        # 7.8.2. Watermark Date
        # 7.8.2.1. Earliest Date
        # 7.8.2.2. Latest Date
        # 7.9. Performance Actions
        # 7.10. Remarks
        # 7.11. Citations
        # 7.11.1. Page
        #
        # 8. INSCRIPTIONS/MARKS
        # 8.1. Inscription Transcription or Description
        # 8.2. Inscription Type
        # 8.3. Inscription Author
        # 8.4. Inscription Location
        # 8.5. Inscription Language
        # 8.6. Typeface/ Letterform
        # 8.7. Mark Identification
        # 8.8. Inscription Date
        # 8.8.1. Earliest Date
        # 8.8.2. Latest Date
        # 8.9. Remarks
        # 8.10. Citations
        # 8.10.1. Page
        #
        # 9. STATE
        # 9.1. State Description
        # 9.2. State Identification
        # 9.3. Known States
        # 9.4. Remarks
        # 9.5. Citations
        # 9.5.1. Page
        #
        # 10. EDITION
        # 10.1. Edition Description
        # 10.2. Edition Number or Name
        # 10.3. Impression Number
        # 10.4. Edition Size
        # 10.5. Remarks
        # 10.6. Citations
        # 10.6.1. Page
        #
        # 11. FACTURE
        # 11.1. Facture Description
        # 11.2. Remarks
        # 11.3. Citations
        # 11.3.1. Page
        #
        # 12. ORIENTATION/ARRANGEMENT
        # 12.1. Orientation/Arrangement Description
        # 12.2. Orientation Indexing Terms
        # 12.3. Remarks
        # 12.4. Citations
        # 12.4.1. Page
        #
        # 13. PHYSICAL DESCRIPTION
        # 13.1. Physical Appearance
        # 13.2. Physical Description Indexing Terms
        # 13.3. Remarks
        # 13.4. Citations
        # 13.4.1. Page
        #
        # 14. CONDITION/EXAMINATION HISTORY
        # 14.1. Condition/Examination Description
        # 14.2. Examination Type
        # 14.3. Examination Agent
        # 14.4. Examination Date
        # 14.4.1. Earliest Date
        # 14.4.2. Latest Date
        # 14.5. Examination Place
        # 14.6. Remarks
        # 14.7. Citations
        # 14.7.1. Page
        #
        # 15. CONSERVATION/TREATMENT HISTORY
        # 15.1. Conservation/Treatment Description
        # 15.2. Treatment Type
        # 15.3. Treatment Agent
        # 15.4. Treatment Date
        # 15.4.1. Earliest Date
        # 15.4.2. Latest Date
        # 15.5. Treatment Place
        # 15.6. Remarks
        # 15.7. Citations
        # 15.7.1. Page
        #
        # 16. SUBJECT MATTER
        # 16.1. Subject Display
        # 16.2. General Subject Terms
        self.generalSubjectTerms = 'No General Subject Terms'
        # 16.2.1.General Subject Type
        # 16.2.2. General Subject Extent
        # 16.2. Specific Subject Terms
        # 16.3.1.Specific Subject Type
        # 16.3.2. Specific Subject Extent
        # 16.4. Outside Iconography Term
        # 16.4.1.Outside Iconography Code
        # 16.4.1.Outside Iconography Source
        # 16.5. Subject Interpretive History
        # 16.6. Remarks
        # 16.7. Citations
        # 16.7.1. Page
        #
        # 17. CONTEXT
        # 17.1. Historical/Cultural Events
        # 17.1.1. Event Type
        # 17.1.2. Event Identification
        # 17.1.3. Event Date
        # 17.1.3.1. Earliest Date
        # 17.1.3.2. Latest Date
        # 17.1.4. Event Place
        # 17.1.5. Event Agent
        # 17.1.5.1. Agent Role
        # 17.1.6. Contextual Cost or Value
        # 17.2. Architectural Context
        # 17.2.1. Building/Site Context
        # 17.2.2. Part/Placement Context
        # 17.2.3. Architectural Context Date
        # 17.2.3.1. Earliest Date
        # 17.2.3.2. Latest Date
        # 17.3. Archeological Context
        # 17.3.1. Discovery/Excavation Place
        # 17.3.2. Excavation Site Sector
        # 17.3.3. Excavator
        # 17.3.4. Discovery/Excavation Date
        # 17.3.4.1. Earliest Date
        # 17.3.4.2. Latest Date
        # 17.4. Historical Location Context
        # 17.4.1. Historical Location Place
        # 17.4.2. Historial Location Date
        # 17.4.2.1. Earliest Date
        # 17.4.2.2. Latest Date
        # 17.5. Remarks
        # 17.6. Citations
        # 17.6.1. Page
        #
        # 18. DESCRIPTIVE NOTE
        # 18.1. Descriptive Note Text
        # 18.1.1. Abstract Description
        # 18.1.2. Pagination Description
        # 18.1.3. Foliation Description
        # 18.1.4. Extent Description
        # 18.1.5. Arrangement Description
        # 18.2. Remarks
        # 18.3. Citations
        # 18.3.1. Page
        #
        # 19. CRITICAL RESPONSES
        # 19.1. Critical Comment
        # 19.2. Comment Document Type
        # 19.3. Comment Author
        # 19.4. Comment Date
        # 19.4.1. Earliest Date
        # 19.4.2. Latest Date
        # 19.5. Comment Circumstances
        # 19.6. Remarks
        # 19.7. Citations
        # 19.7.1. Page
        #
        # 20. RELATED WORKS
        # 20.1. Related Work Label/Identification
        # 20.1.1. Work Relationship Type
        # 20.1.2. Work Relationship Date
        # 20.1.2.1. Earliest Date
        # 20.1.2.2. Latest Date
        # 20.2. Work Broader Context
        # 20.2.1. Historical Flag
        # 20.2.2. Broader Context Date
        # 20.2.2.1. Earliest Date
        # 20.2.2.2. Latest Date
        # 20.2.3. Hierarchical Relationship Type
        # 20.3. Relationship Number
        # 20.4. Remarks
        # 20.5. Citations
        # 20.5.1. Page
        #
        # 21. CURRENT LOCATION
        # 21.1. Current Location Description
        # 21.2. Repository/Geographic Location
        self.currentRepositoryGeographicLocation = 'No Current Repository / Geographic Location'
        # 21.2.1. Current Flag
        # 21.2.2. Location Type
        # 21.2.3. Repository Numbers
        self.repositoryNumbers = 'No Repository Numbers'
        # 21.2.3.1. Number Type
        # 21.2.4. Gallery/Specific Location
        # 21.2.5. Coordinates
        # 21.2.6. Credit Line
        # 21.3. Object/Work Label/Identification
        # 21.4. Remarks
        # 21.5. Citations
        # 21.5.1. Page
        #
        # 22. COPYRIGHT/RESTRICTIONS
        # 22.1. Copyright Statement
        # 22.2. Copyright Holder Name
        # 22.3. Copyright Place
        # 22.4. Copyright Date
        # 22.4.1. Earliest Date
        # 22.4.2. Latest Date
        # 22.5. Remarks
        # 22.6. Citations
        # 22.6.1. Page
        #
        # 23. OWNERSHIP/COLLECTING HISTORY
        # 23.1. Provenance Description
        # 23.1.1. Acquisition Description
        # 23.2. Transfer Mode
        # 23.3. Cost or Value
        # 23.3.1. Valuation
        # 23.3.1.1. Valuation Amount
        # 23.3.1.2. Currency Unit
        # 23.4. Legal Status
        # 23.5. Owner/Agent
        # 23.5.1. Owner/Agent Role
        # 23.6. Ownership Place
        # 23.7. Ownership Date
        # 23.7.1. Earliest Date
        # 23.7.2. Latest Date
        # 23.8. Owner's Numbers
        # 23.8.1. Number Type
        # 23.9. Owner's Credit Line
        # 23.10. Remarks
        # 23.11. Citations
        # 23.11.1. Page
        #
        # 24. EXHIBITION/LOAN HISTORY
        # 24.1. Exhibition/Loan Description
        # 24.2. Exhibition Title or Name
        # 24.3. Exhibition Type
        # 24.4. Exhibition Curator
        # 24.5. Exhibition Organizer
        # 24.6. Exhibition Sponsor
        # 24.7. Exhibition Venue
        # 24.7.1. Venue Name/Place
        # 24.7.2. Venue Date
        # 24.7.2.1. Earliest Date
        # 24.7.2.2. Latest Date
        # 24.8. Exhibition Object Number
        # 24.8.1. Number Type
        # 24.9. Exhibition Object/Work Label/Identification
        # 24.10. Remarks
        # 24.11. Citations
        # 24.11.1. Page
        #
        # 25. CATALOGING HISTORY
        # 25.1. Cataloging Institution
        # 25.2. Cataloger Name
        # 25.3. Cataloger Action
        # 25.4. Area of Record Affected
        # 25.5. Cataloging Date
        # 25.5.1. Earliest Date
        # 25.5.2. Latest Date
        # 25.6. Remarks
        # 25.7. Object/Work Record ID
        # 25.8. Cataloging Language

        # 26. RELATED VISUAL DOCUMENTATION
        # [references to Object/Work]
        # 26.1. Image References
        self.imageReferences = 'No Image References'
        # 26.1.1. Image to Work Relationship Type

        # 27. RELATED TEXTUAL REFERENCES
        self.textualReferences = {}
        # 27.1. Citations for Sources
        # 27.1.1. Page
        # 27.1.2. Work Cited or Illustrated
        # 27.1.3. Cited Object/Work Number
        # 27.1.3.1. Number Type
        #
        # [Citations Authority information]
        # 27.2. Source Brief Citation
        self.sourceBriefCitation = 'No Source Brief Citation'
        # 27.2.1. Source Type
        # 27.2.2. Source Full Citation
        self.sourceFullCitation = 'No SourceFullCitation'
        # 27.2.2.1. Source Title
        # 27.2.2.2. Source Broader Title
        # 27.2.2.3. Source Author
        # 27.2.2.4. Source Editor/Compiler
        # 27.2.2.5. Source Publication Place
        # 27.2.2.6. Source Publisher
        # 27.2.2.7. Source Publication Year
        # 27.2.2.8. Source Edition Statement
        # 27.2.3. Remarks
        # 27.2.4. Citations Authority Record ID

    def __str__(self):
        return self.titleText

class Image:
    def __init__(self):
        self.imageLabel = "No Label / Identification"
        # [Image Authority information]
        # 26.2. Image Label/Identification
        # 26.2.1. Image Catalog Level
        # 26.2.2. Image Type
        # 26.2.3. Image Title/Name
        # 26.2.3.1 Image Title Type
        # 26.2.4. Image Measurements
        # 26.2.4.1. Dimensions Type
        # 26.2.4.2. Dimensions Value
        # 26.2.4.3. Dimensions Unit
        # 26.2.5. Image Format
        # 26.2.6. Image Date
        # 26.2.6.1. Earliest Date
        # 26.2.6.2. Latest Date
        # 26.2.7. Image Color
        # 26.2.8. Works Depicted
        # 26.2.9. Image View Description
        # 26.2.9.1. View Type
        # 26.2.9.2. View Subject
        # 26.2.9.2.1. View Subject Indexing Terms
        # 26.2.9.3. View Date
        # 26.2.9.3.1. Earliest Date
        # 26.2.9.3.2. Latest Date
        # 26.2.10. Image Maker/Agent
        # 26.2.10.1. Image Maker Role
        # 26.2.10.2. Image Maker Extent
        # 26.2.11. Image Repository
        # 26.2.11.1. Image Repository Numbers
        # 26.2.11.1.1. Number Type
        # 26.2.12. Image Copyright/Restrictions
        # 26.2.12.1. Image Copyright Holder
        # 26.2.12.1.1. Image Copyright Holder's Numbers
        # 26.2.12.1.1.1. Number Type
        # 26.2.12.2. Image Copyright Date
        # 26.2.12.2.1. Earliest Date
        # 26.2.12.2.2. Latest Date
        # 26.2.13. Image Source
        # 26.2.13.1. Image Source Number
        # 26.2.13.1.1. Number Type
        # 26.2.14. Related Image
        # 26.2.14.1. Image Relationship Type
        # 26.2.14.2. Image Relationship Number
        # 26.2.14.3. Image Relationship Date
        # 26.2.14.3.1. Earliest Date
        # 26.2.14.3.2. Latest Date
        # 26.2.15. Image Broader Context
        # 26.2.16. Remarks
        # 26.2.17. Citations
        # 26.2.17.1. Page
        # 26.2.18. Image Authority Record ID

    def __str__(self):
        return self.imageLabel

class PersonOrCorporateBody:
    def __init__(self):
        # 28. PERSON/CORPORATE BODY AUTHORITY
        # 28.1. Person Authority Record Type
        # 28.2. Person/Corporate Body Name
        self.personCorporateBodyName = 'No Person / Corporate Body Name'
        # 28.2.1. Preference
        # 28.2.2. Name Type
        # 28.2.3. Name Qualifier
        # 28.2.4. Name Language
        # 28.2.5. Historical Flag
        # 28.2.6. Display Name Flag
        # 28.2.7. Other Name Flags
        # 28.2.8. Name Source
        self.NameSource = 'No Name Source'
        # 28.2.8.1. Page
        # 28.2.9. Name Date
        # 28.2.9.1. Earliest Date
        # 28.2.9.2. Latest Date
        # 28.3. Display Biography
        self.displayBiography = 'No Display Biography'
        # 28.4. Birth Date
        self.birthDate = 'No Birth Date'
        # 28.5. Death Date
        self.deathDate = 'No Death Date'
        # 28.6. Birth Place
        # 28.7. Death Place
        # 28.8. Person Nationality/Culture/Race
        self.personNationalityCultureRace = 'No Person Nationality / Culture / Race'
        # 28.8.1. Preference
        # 28.8.2. Nationality/Culture Type
        # 28.9. Gender
        # 28.10. Life Roles
        self.lifeRoles = 'No Life Roles'
        # 28.10.1. Preference
        # 28.10.2. Role Date
        # 28.10.2.1. Earliest Date
        # 28.10.2.2. Latest Date
        # 28.11. Person/Corporate Body Event
        # 28.11.1. Event Date
        # 28.11.1.1. Earliest Date
        # 28.11.1.2. Latest Date
        # 28.11.2. Event Place
        # 28.12. Related Person/Corporate Body
        # 28.12.1. Person Relationship Type
        # 28.12.2. Person Relationship Date
        # 28.12.2.1. Earliest Date
        # 28.12.2.2. Latest Date
        # 28.13. Person/Corporate Body Broader Context
        # 28.13.1. Broader Context Date
        # 28.13.1.1. Earliest Date
        # 28.13.1.2. Latest Date
        # 28.14. Person/Corporate Body Label/Identification
        # 28.15. Person/Corporate Body Descriptive Note
        # 28.15.1. Note Source
        # 28.15.1.1. Page
        # 28.16. Remarks
        # 28.17. Citations
        # 28.17.1. Page
        # 28.18. Person Authority Record ID

    def __str__(self):
        return self.personCorporateBodyName


class PlaceOrLocation:
    def __init__(self):
        # 29. PLACE/LOCATION AUTHORITY
        # 29.1. Place/Location Authority Record Type
        # 29.2. Place Name
        self.placeName = 'No Place Name'
        # 29.2.1. Preference
        # 29.2.2. Name Type
        # 29.2.3. Name Qualifier
        # 29.2.4. Name Language
        # 29.2.5. Historical Flag
        # 29.2.6. Display Name Flag
        # 29.2.7. Other Name Flags
        # 29.2.8. Name Source
        self.nameSource = 'No Name Source'
        # 29.2.8.1. Page
        # 29.2.9. Name Date
        # 29.2.9.1. Earliest Date
        # 29.2.9.2. Latest Date
        # 29.3. Geographic Coordinates
        # 29.4. Place Types
        self.placeTypes = 'No Place Types'
        # 29.4.1. Preference
        # 29.4.2. Place Type Date
        # 29.4.2.1. Earliest Date
        # 29.4.2.2. Latest Date
        # 29.5. Related Places
        # 29.5.1. Place Relationship Type
        # 29.5.2. Place Relationship Date
        # 29.5.2.1. Earliest Date
        # 29.5.2.2. Latest Date
        # 29.6. Place Broader Context
        self.placeBroaderContext = 'No Place Broader Context'
        # 29.6.1. Broader Context Date
        # 29.6.1.1. Earliest Date
        # 29.6.1.2. Latest Date
        # 29.7. Place/Location Label/Identification
        # 29.8. Place/Location Descriptive Note
        # 29.8.1. Note Source
        # 29.8.1.1. Page
        # 29.9. Remarks
        # 29.10. Citations
        # 29.10.1. Page
        # 29.11. Place Authority Record ID

    def __str__(self):
        return self.placeName

class GenericConcept:
    def __init__(self):
        # 30. GENERIC CONCEPT AUTHORITY
        # 30.1. Concept Authority Record Type
        # 30.2. Generic Concept Term
        self.genericConceptTerm = 'No Generic Concept Term'
        # 30.2.1. Preference
        # 30.2.2. Term Type
        # 30.2.3. Term Qualifier
        # 30.2.4. Term Language
        # 30.2.5. Historical Flag
        # 30.2.6. Display Term Flag
        # 30.2.7. Other Term Flags
        # 30.2.8. Term Source
        self.termSource = 'No Term Source'
        # 30.2.8.1. Page
        # 30.2.9. Term Date
        # 30.2.9.1. Earliest Date
        # 30.2.9.2. Latest Date
        # 30.3. Related Generic Concepts
        # 30.3.1. Concept Relationship Type
        # 30.3.2. Concept Relationship Date
        # 30.3.2.1. Earliest Date
        # 30.3.2.2. Latest Date
        # 30.4. Concept Broader Context
        self.conceptBroaderContext = 'No Concept Broader Context'
        # 30.4.1. Broader Context Date
        # 30.4.1.1. Earliest Date
        # 30.4.1.2. Latest Date
        # 30.5. Generic Concept Label/Identification
        # 30.6. Concept Scope Note
        self.conceptScopeNote = 'No Concept Scope Note'
        # 30.6.1. Note Source
        self.noteSource = 'No Note Source'
        # 30.6.1.1. Page
        # 30.7. Remarks
        # 30.8. Citations
        # 30.8.1. Page
        # 30.9. Concept Authority Record ID

    def __str__(self):
        return self.genericConceptTerm

class Subject:
    def __init__(self):
        # 31. SUBJECT AUTHORITY
        # 31.1. Subject Authority Record Type
        # 31.2. Subject Name
        self.subjectName = 'No Subject Name'
        # 31.2.1. Preference
        # 31.2.2. Name Type
        # 31.2.3. Name Qualifier
        # 31.2.4. Name Language
        # 31.2.5. Historical Flag
        # 31.2.6. Display Name Flag
        # 31.2.7. Other Name Flags
        # 31.2.8. Name Source
        self.nameSource = 'No Name Source'
        # 31.2.8.1. Page
        # 31.2.9. Name Date
        # 31.2.9.1. Earliest Date
        # 31.2.9.2. Latest Date
        # 31.3. Subject Date
        # 31.3.1. Earliest Date
        # 31.3.2. Latest Date
        # 31.4. Subject Roles/Attributes
        # 31.4.1. Preference
        # 31.4.2. Role Date
        # 31.4.2.1. Earliest Date
        # 31.4.2.2. Latest Date
        # 31.5. Related Subject
        # 31.5.1. Subject Relationship Type
        # 31.5.2. Subject Relationship Date
        # 31.5.2.1. Earliest Date
        # 31.5.2.2. Latest Date
        # 31.6. Subject Broader Context
        self.subjectBroaderContext = 'No Subject Broader Context'
        # 31.6.1. Broader Context Date
        # 31.6.1.1. Earliest Date
        # 31.6.1.2. Latest Date
        # 31.7. Related Place/Location
        # 31.7.1. Place Relationship Type
        # 31.8. Related Person/Corporate Body
        # 31.8.1. Person Relationship Type
        # 31.9. Related Generic Concept
        # 31.9.1. Concept Relationship Type
        # 31.10. Subject Label/Identification
        # 31.11. Subject Descriptive Note
        # 31.11.1. Note Source
        # 31.11.1.1. Page
        # 31.12. Remarks
        # 31.13. Citations
        # 31.13.1. Page
        # 31.14. Subject Authority Record ID

    def __str__(self):
        return self.subjectName
