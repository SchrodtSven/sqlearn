from cappy.core.query import Query
from cappy.core.qb import QueryBuilder
from cappy.app.entity import Entity





qb = QueryBuilder('event')
#print(qb.delete('id=2'))


#'id=2', ['foo', 'bar', 'ca']

#exit()

to_be_inserted = {'id':23, 'title': 'Adding title', 'loc_id': 2, 'e_from': '2025-07-01 02:03:11', 'e_until': '2025-07-01 23:42:22', 'cat_id': 1, 'comment': 'NOWay to PyMania', 'status_id':1}
print(to_be_inserted.keys())

q = Query()
for item in q.select('event'):
    e = Entity(item)
    print(str(e.id))
#q.update('event', to_be_inserted)
#print(lid)
#q = QueryBuilder('event')
# print(q.update(to_be_inserted))
#

#print(q.insert(to_be_inserted))