import sqlite3
import nltk
from safeprint import print
import json

testing = 'test-db-507.db'
production = 'aby02-507.db'

class AbyIndex():
    def __init__(self):
        self.contents = {}

    def __str__(self):
        return "\n".join(list(self.contents.keys()))

    def weigh(self,facetIndex,facetName,DBNAME):
        conn = sqlite3.connect(DBNAME)
        cur = conn.cursor()
        cur.execute('SELECT * FROM Works')

        # titleText

        row = cur.fetchone()
        while row is not None:
            self.add_tokens(row,facetIndex=facetIndex,facetName=facetName)
            # print(row)
            row = cur.fetchone()

        # # This will be redundant once words are properly stemmed, but for now helps improve frequency counts.
        #
        # for token in list(self.contents.keys()):
        #     statement = f'SELECT COUNT(*) FROM Works WHERE {facetName} LIKE ?'
        #     insertion = (
        #         '%'+str(token)+'%',
        #     )
        #     cur.execute(statement,insertion)
        #     num = int(cur.fetchone()[0])
        #     print(token)
        #     print(num)
        #     print(self.contents[token].frequencies[facetName])

        conn.close()

    def add_tokens(self,row,facetIndex,facetName):
        tokens = nltk.word_tokenize(row[facetIndex])
        i=0
        for token in tokens:
            if token not in self.contents:
                self.contents[token] = {
                    'locations': [],
                    'frequencies': {},
                }

            if facetName not in self.contents[token]['frequencies']:
                self.contents[token]['frequencies'][facetName] = 0
            locator = (row[0],facetName,i)
            self.contents[token]['locations'].append(locator)
            self.contents[token]['frequencies'][facetName] += 1
            i += 1

    def save_sample_index(self):
        with open('sample_index.json','w') as fileRef:
            fileRef.write(json.dumps(self.contents))

def get_standard_index(db):
    abyIndex = AbyIndex()
    abyIndex.weigh(facetIndex=6,facetName='titleText',DBNAME=db)
    abyIndex.weigh(facetIndex=16,facetName='currentRepo',DBNAME=db)
    # abyIndex.save_sample_index()
    return(abyIndex)

if __name__ == '__main__':
    abyIndex = get_standard_index()
