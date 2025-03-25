#import sys
#sys.path += ['../sqlearn']
 
import unittest
from sqlearn.core.query import Query
from sqlearn.core.entity import Entity


class TestEntity(unittest.TestCase):

    def test_foo(self):
        query = Query()
        dta = query.exc('SELECT * FROM Customer').f_all()
    
        for item in dta:
            ety = Entity(item)
            self.assertTrue(ety.get_by_key('FirstName') == ety.FirstName)
    

if __name__ == '__main__':
    unittest.main()
    #print(', '.join(sys.path), sep='\n')
    
    
