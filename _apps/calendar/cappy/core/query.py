# SINCE: 2025-03-21
# Wrapper for SQLIte operations (CREATE, SELECT, INSERT ...)

import sqlite3
from cappy.core.qb import QueryBuilder

class Query:
    """" Class for using SQLite3 with Python """
    
    data_source  = 'db/main.db'
    conn = None
    crs = None
    
    def __init__(self, ds:str = ''):
        """ Initializing:
                - connection to db
                - setting row factory
                - getting current db cursor
        Args:
            ds (str, optional): _description_. Defaults to ''.
        """
        if ds != '':
            self.data_source = ds
            # TODO check: file exists
        self.conn = sqlite3.connect(self.data_source)
        self.conn.row_factory = sqlite3.Row
        self.crs = self.conn.cursor()
        
        
        
    def exc(self, sql:str, dta:dict={}):
        """ Executing given SQL 

        Args:
            sql (str): Query in SQL syntax
            dta (dict, optional): Values to be used when executoig query

        Returns:
            _type_: self
        """
        self.crs.execute(sql, dta)
        return self
    
    def f_all(self):
        """ Fetching complete result set - "all rows"

        Args:
           

        Returns:
            _type_: Result set of last executed query
        """
        return self.crs.fetchall()
    
    def insert(self, tbl:str, dta:dict={}):
        """ Executing INSERT stmt on entity('table') tbl with data

        Args:
            tbl (str): Name of entity
            dta (dict): data to be inserted

        Returns:
            _type_: self
        """
        sql  = 'fii'
        self.qb = QueryBuilder(tbl)
        
        #print( dta.values(), type(dta.values()))
        #print(type(self.qb.insert(dta) ), self.qb.insert(dta) )
        
        #exit()
        
        self.crs.execute(self.qb.insert(dta) , list(dta.values()))
        self.conn.commit()
        return self.crs.lastrowid
 
    def update(self, tbl:str, dta:dict={}):
        self.qb = QueryBuilder(tbl)
        self.crs.execute(self.qb.update(dta) , dta)
        self.conn.commit()
        return self
 
    
    
