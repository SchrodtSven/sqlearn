import sqlite3

class Entity:
    """ Generic class for entity instance   """
    
    keys = None
    data = None
    primary = None
    
    def __init__(self, data):
        self.data = data
        self._keys = self.data.keys()
        
        
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
    