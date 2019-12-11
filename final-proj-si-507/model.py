import sqlite3
import refresher
import nltk
from tqdm import tqdm
import datetime
import apis
import aio
from diskcache import Cache
import asyncio

testing = 'test-db-507.db'
production = 'aby02-507.db'

def init_db(DBNAME):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    statement = '''
        DROP TABLE IF EXISTS 'Works';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'DataSources';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Resumptions';
    '''
    cur.execute(statement)

    conn.commit()


    statement = '''
        CREATE TABLE "Works" (
        	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        	"pid"	TEXT NOT NULL,
        	"relevance"	INTEGER,
        	"catalogLevel"	TEXT,
        	"workType"	TEXT,
        	"classificationTerm"	TEXT,
        	"titleText"	TEXT NOT NULL,
        	"creatorDescription"	TEXT,
        	"creatorIdentity"	TEXT,
        	"creatorRole"	TEXT,
        	"creationDate"	TEXT,
        	"earliestDate"	TEXT,
        	"latestDate"	TEXT,
        	"dimensionsDescription"	TEXT,
        	"materialsTechniquesDescription"	TEXT,
        	"generalSubjectTerms"	TEXT,
        	"currentRepo"	TEXT NOT NULL,
            "copyrightStatement"   TEXT,
        	"repositoryNumbers"	TEXT,
        	"primaryImage"	TEXT,
            "primaryImageSmall" TEXT,
            "resourceURL"   TEXT,
        	"sourceBriefCitation"	TEXT,
        	"sourceFullCitation"	TEXT
        );
    '''

#                       ,
# "originalRecord"    TEXT

    cur.execute(statement)


    statement = '''
        CREATE TABLE "DataSources" (
        	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        	"sourceName"	INTEGER,
        	"resumptionToken"	TEXT NOT NULL,
        	"timeStamp"	TEXT
        );
    '''
    cur.execute(statement)

    conn.commit()
    conn.close()


def add_works(artworks,DBNAME=production):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    for work in artworks:
        insertion = (
        	None, #0 "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        	work.pid, #1 "pid"	TEXT NOT NULL UNIQUE,
        	work.relevance, #2 "relevance"	INTEGER,
        	None, #3 "catalogLevel"	TEXT,
        	None, #4 "workType"	TEXT,
        	None, #5 "classificationTerm"	TEXT,
        	work.titleText, #6 "titleText"	TEXT NOT NULL,
        	work.creatorDescription, #7 "creatorDescription"	TEXT,
        	None, #8 "creatorIdentity"	TEXT,
        	None, #9 "creatorRole"	TEXT,
        	None, #10 "creationDate"	TEXT,
        	None, #11 "earliestDate"	TEXT,
        	None, #12 "latestDate"	TEXT,
        	None, #13 "dimensionsDescription"	TEXT,
        	None, #14 "materialsTechniquesDescription"	TEXT,
        	None, #15 "generalSubjectTerms"	TEXT,
        	work.currentRepo, #16 "currentRepositoryGeographicLocation"	TEXT NOT NULL,
        	None, #17 "repositoryNumbers"	TEXT,
            work.copyrightStatement, #18 "copyrightStatement"   TEXT,
        	work.imageReferences['primaryImage'], #19 "primaryImage"	TEXT,
        	work.imageReferences['primaryImageSmall'], #20 "primaryImageSmall"	TEXT,
            work.textualReferences['referenceURL'],        #21    "resourceURL"   TEXT,
        	None, #22 "sourceBriefCitation"	TEXT,
        	None, #23 "sourceFullCitation"	TEXT,
            # work.originalRecord, #24    "originalRecord"    TEXT,
        )

        statement = '''
            INSERT INTO Works
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
        '''
        if check_db('pid',work.pid) == False:
            cur.execute(statement, insertion)

    conn.commit()
    conn.close()

def check_db(colname,val,DBNAME=production):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    insertion = ("%"+str(val)+"%",)

    statement = f'''
        SELECT COUNT(*)
        FROM Works WHERE {colname} LIKE ?
    '''

    cur.execute(statement, insertion)
    found = int(cur.fetchone()[0])
    conn.close()
    if found > 0:
        return True
    else:
        return False

def save_resumption(sourceName,resumptionToken,DBNAME=production):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    # desired time format "YYYY-MM-DD HH:MM:SS.SSS"
    timeStamp = datetime.datetime.now().isoformat(timespec='milliseconds')
    print(timeStamp)

    insertion = (
        None, #id
        sourceName,
        resumptionToken,
        timeStamp,
        )

    statement = f'''
        INSERT INTO DataSources
        VALUES (?,?,?,?)
    '''

    cur.execute(statement, insertion)
    conn.commit()
    conn.close()

def get_resumption(sourceName,resumptionExpiresIn,DBNAME=production):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    insertion = (sourceName,)

    statement = f'''
        SELECT resumptionToken, timeStamp
        FROM DataSources
        WHERE DataSources.sourceName = ?
        ORDER BY timeStamp DESC
    '''

    cur.execute(statement, insertion)
    row = cur.fetchone()
    try:
        token = row[0]
        timeStampDT = datetime.datetime.fromisoformat(row[1])
    except:
        token = 'expired'
        timeStampDT = datetime.datetime.now() - datetime.timedelta(days=366)

    if timeStampDT + resumptionExpiresIn < datetime.datetime.now():
        token = 'expired'

    # print(token)

    conn.close()

    return token

def query_title(q,DBNAME=production):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    insertion = ("%"+str(q)+"%",)

    statement = '''
        SELECT *
        FROM Works WHERE titleText LIKE ?
    '''

    cur.execute(statement, insertion)
    results = cur.fetchall()
    artworks = [refresher.Item(rec) for rec in results]
    conn.close()
    return artworks

def get_work_by_pid(pid,DBNAME=production):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    insertion = (pid,)

    statement = '''
        SELECT *
        	FROM Works
        		JOIN TokenLocations
        			ON Works.id = TokenLocations.workId
        				JOIN AbyIndex
        					ON TokenLocations.id = AbyIndex.locationId
        						JOIN Tokens
        							ON AbyIndex.tokenId = Tokens.id
        WHERE pid = ?
    '''

    cur.execute(statement, insertion)
    work = refresher.Item(cur.fetchone())
    conn.close()
    return work

def countworks(DBNAME=production):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    cur.execute('SELECT COUNT (*) FROM Works')
    work = refresher.Item(cur.fetchone())
    conn.close()
    return work


def rebuild_index(abyIndex,DBNAME=production):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    statement = '''
        DROP TABLE IF EXISTS 'AbyIndex';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'TokenLocations';
    '''
    cur.execute(statement)

    statement = '''
        DROP TABLE IF EXISTS 'Tokens';
    '''
    cur.execute(statement)

    conn.commit()

    statement = '''
        CREATE TABLE "Tokens" (
        	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        	"token"	TEXT NOT NULL UNIQUE,
        	"titleTextFrequency"	INTEGER,
        	"currentRepoFrequency"	INTEGER
        );
    '''

    cur.execute(statement)

    statement = '''
        CREATE TABLE "TokenLocations" (
        	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        	"workId"	INTEGER,
        	"workFacetName"	TEXT,
        	"tokenIndexInString"	INTEGER,
        	"weight"	INTEGER,
        	FOREIGN KEY("workId") REFERENCES "Works"("id")
        );
    '''
    cur.execute(statement)

    statement = '''
        CREATE TABLE "AbyIndex" (
        	"id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        	"tokenId"	INTEGER,
        	"locationId"	INTEGER,
        	FOREIGN KEY("tokenId") REFERENCES "Tokens"("id"),
        	FOREIGN KEY("locationId") REFERENCES "TokenLocations"("id")
        );
    '''
    cur.execute(statement)


    for token in tqdm(list(abyIndex.contents.keys())):

        try:
            titleTextFrequency = abyIndex.contents[token]['frequencies']['titleText']
        except:
            titleTextFrequency = 0

        try:
            currentRepoFrequency = abyIndex.contents[token]['frequencies']['currentRepo']
        except:
            currentRepoFrequency = 0

        statement = '''
            INSERT INTO Tokens
            VALUES (?,?,?,?)
        '''

        insertion = (
            None,
            token,
            titleTextFrequency,
            currentRepoFrequency,
        )

        cur.execute(statement, insertion)

        last_token_id = cur.lastrowid

        for location in abyIndex.contents[token]['locations']:

            statement = '''
                INSERT INTO TokenLocations
                VALUES (?,?,?,?,?)
            '''

            if location[1] == 'titleText':
                freq = titleTextFrequency
            elif location[1] == 'currentRepo':
                freq = currentRepoFrequency

            insertion = (
                None,
                location[0], #
                location[1],
                location[2],
                100/freq, # TODO: Add field weight, record occurrences
            )

            cur.execute(statement, insertion)
            last_location_id = cur.lastrowid

            statement = '''
                INSERT INTO AbyIndex
                VALUES (?,?,?)
            '''

            insertion = (
                None,
                last_token_id,
                last_location_id,
            )

            cur.execute(statement, insertion)

        conn.commit()

    conn.close()

def search_index(q,DBNAME=production):
    conn = sqlite3.connect(DBNAME)
    cur = conn.cursor()

    artworks = []

    for token in nltk.word_tokenize(q):
        # print(token)
        insertion = (
            "%"+str(token)+"%",
            "%"+str(token)+"%",
        )

        statement = '''
            SELECT *
            	FROM Works
            		JOIN TokenLocations
            			ON Works.id = TokenLocations.workId
            				JOIN AbyIndex
            					ON TokenLocations.id = AbyIndex.locationId
            						JOIN Tokens
            							ON AbyIndex.tokenId = Tokens.id
            WHERE Tokens.token LIKE ? AND Tokens.token LIKE ?
            ORDER BY TokenLocations.weight DESC
            LIMIT 10
        '''

        cur.execute(statement, insertion)
        # print(cur.fetchone())
        results = cur.fetchall()
        artworks.extend([refresher.Item(rec) for rec in results])

    conn.close()
    sorted_artworks = sorted(artworks, key = lambda work:work.weight,reverse=True)
    # for each in sorted_artworks:
        # print(each.weight)
    return sorted_artworks

def locate(artworks):

    locators = []
    presenters = []
    with Cache('map_cache') as ref:
        for work in artworks:
            # print(work.currentRepo)
            api = apis.GooglePlaces()
            api.workLocating = work
            api.prepare(work.currentRepo)
            if api.cache_key() in ref:
                api.hits = api.format(ref.get(api.cache_key()))
                presenters.append(api)
                # print('Cache found for',api.params['input'])
            else:
                locators.append(api)
                # print('Getting new data for',api.params['input'])

    req_resp_tuples = asyncio.run(aio.manage_requests(locators))

    with Cache('map_cache') as ref:
        for locator, response in req_resp_tuples:
            locator.hits = locator.format(response)
            ref.set(locator.cache_key(),response)
            presenters.append(locator)

    locatedWorks = []

    for presenter in presenters:
        if len(presenter.list_records()) > 0:
            locationRecord = presenter.list_records()[0]
            locatedWork = presenter.workLocating
            locatedWork.lat = locationRecord['geometry']['location']['lat']
            locatedWork.lng = locationRecord['geometry']['location']['lng']
            locatedWorks.append(locatedWork)

    return locatedWorks
