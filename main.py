import sqlite3
from sqlearn.core.query import Query
from sqlearn.core.entity import Entity

if __name__ == '__main__':
    query = Query()
    dta = query.exc('SELECT * FROM Customer').f_all()
    
    for item in dta:
        ety = Entity(item)
        
        for k in ety.get_keys():
             print(f'{k} :: {ety.get_by_key(k)}')
             
        exit()