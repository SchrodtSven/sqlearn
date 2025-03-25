#import sys
#sys.path += ['../sqlearn']
 
import unittest
from sqlearn.core.query import Query
from sqlearn.core.entity import Entity


class TestEntity(unittest.TestCase):

    def test_basix(self):
        query = Query()
        dta = query.exc('SELECT * FROM Customer').f_all()
        
        for item in dta:
            ety = Entity(item)
            self.assertTrue(ety.get_by_key('first_name') == ety.first_name)
            self.assertTrue(ety.get_by_key('gender') == ety.gender)
            
if __name__ == '__main__':
    unittest.main()
    #print(', '.join(sys.path), sep='\n')
    
    
