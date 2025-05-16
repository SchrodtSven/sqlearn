import numpy as np
import pandas as pd
import sqlite3




def split_full(fullname:str)->tuple:
    """ DEPRECATED """
    (first, last) = fullname.split(' ')
    return first, last
    

def get_mail_prf(fullname:str, mode:int=5):
    tmp = fullname.split(' ')
    if fullname.find(' ') == -1:
        raise IndexError('Foo')
    first, last = fullname.split(' ')
    
    if mode == 5: #S.Schrodt
        return first[0:1] + '.' + last
    elif mode == 4: #schrodt.Sven
        return last + '.' + first
    elif mode == 3: #svenschrodt
        return first + last
    elif mode == 2: #sschrodt
        return first[0:1] + first
    elif mode == 1: #schrodtsven
        return last + first
    else: #sven.s
        return first + '.' + last[0:1]
    

# df = pd.read_json('customers_database.json')
# print(df.head())

# df['fullname'] = df['first_name'] + ' ' + df['last_name']

# print(df)

for x in range(6):
    print(x, get_mail_prf('Sven Schrodt', x))

