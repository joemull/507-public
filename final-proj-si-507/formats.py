import json
from bs4 import BeautifulSoup

class JSON:
    def MIMEType(self):
        return "application/json"

    def format(self,s):
        return json.loads(s)

    def get_from_cache(self,ref,key):
        return ref.get(key)

    def save_to_cache(self,ref,data):
        ref.set(self.cache_key(),data)

    def cast(self,data):
        return json.dumps(data)

class XML:
    def MIMEType(self):
        return "application/xml"

    def format(self,s):
        return BeautifulSoup(s,'lxml-xml')

    def get_from_cache(self,ref,key):
        return BeautifulSoup(ref.get(key),'lxml-xml')

    def save_to_cache(self,ref,data):
        ref.set(self.cache_key(),data.prettify())

    def cast(self,data):
        return data.prettify()
