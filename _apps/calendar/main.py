from cappy.core.query import Query
from cappy.core.qb import QueryBuilder





#q = QueryBuilder('event')
#print(q.exc('SELECT * FROM status').f_all())
#dta = {'id'}

to_be_inserted = {'id':23, 'title': 'Adding title', 'loc_id': 2, 'e_from': '2025-07-01 02:03:11', 'e_until': '2025-07-01 23:42:22', 'cat_id': 1, 'comment': 'NOWay to PyMania', 'status_id':1}


q = Query()
q.update('event', to_be_inserted)
#print(lid)
#q = QueryBuilder('event')
# print(q.update(to_be_inserted))
#

#print(q.insert(to_be_inserted))