import sqlite3
import pandas as pd

class Query:
    """" Class for using SQLite3 with Python """
    
    data_source  = 'tmp/my_database.db'
    conn = None
    crs = None
    
    def __init__(self):
        """ Initializing:
                - connection to db
                - setting row factory
                - getting current db cursor
        """
        self.conn = sqlite3.connect(self.data_source)
        self.conn.row_factory = sqlite3.Row
        self.crs = self.conn.cursor()
        
    def exc(self, sql:str, data:dict={}):
        """ Executing given SQL 

        Args:
            sql (str): Query in SQL syntax

        Returns:
            _type_: self
        """
        self.crs.execute(sql, data)
        return self
    
    def f_all(self, as_df:bool=False):
        """ Fetching complete result set - "all rows"

        Args:
            as_df (bool, optional): Returning result set optionally as pandas DataFrame (pd.df). Defaults to False.

        Returns:
            _type_: Result set of last executed query
        """
        if as_df:
            tmp = self.crs.fetchall()
            pd.DataFrame(columns=tmp[0].keys(), data=tmp) # looks too complicated, let's see l8er
        else: 
            return self.crs.fetchall()
    
    
