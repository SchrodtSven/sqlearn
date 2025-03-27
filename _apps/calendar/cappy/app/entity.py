# SINCE: 2025-03-27
# SUBJECT: Classes representing entities 
import sqlite3

class Entity:
    """ Generic class for entity instance   """
    
    keys = None
    data = None
    primary = ('id') # pk by default (convention used here))
    query = None
    
    def __init__(self, data, query=None):
        self.data = data
        self._keys = self.data.keys()
        self.query = query
        
    def __getattr__(self, key):
        self.__sanitize_key(key)
        return self.data[key]
        
         
    def get_keys(self):
        return self._keys
    
    
    def get_by_key(self, key:str):
        self.__sanitize_key(key)
        return self.data[key]
    
    def __sanitize_key(self, key:str):
        if key not in self._keys:
            raise IndexError(f'Key {key} does not exist')
        
    def save():
        # implement INSERT || UPDATE depending on existing primary key ('id')
        pass

