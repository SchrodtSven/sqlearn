import sqlite3

class Query:
    """" Class for using SQLite3 with Python """
    
    data_source  = 'data/my_first.db'
    conn = None
    crs = None
    
    def __init__(self):
        self.conn = sqlite3.connect(self.data_source)
        self.conn.row_factory = sqlite3.Row
        self.crs = self.conn.cursor()
        
        
        #print('Query meint: ' + __name__)
        
    def exc(self, sql:str):
        self.crs.execute(sql)
        return self
    
    def f_all(self):
        return self.crs.fetchall()
    
    
        