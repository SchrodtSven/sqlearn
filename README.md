# SQLearn

## Motivation

- Learning usage of SQL with Python step-by-step in more depth

- Combining with formerly learned Python lessons (e.G: Pandas, Numpy, GUI stuff)
    && existing SQL skillz

## Example code

```python
from cappy.core.query import Query
from cappy.core.qb import QueryBuilder
from cappy.app.entity import Entity
import sqlite3


q = Query()

qb = QueryBuilder("event")
to_be_inserted = {
    "title": "Foo-Fighterz",
    "loc_id": 3,
    "evt_start": "2025-12-09 00:03:11",
    "evt_end": "2025-12-09 23:42:23",
    "cat_id": 22,
    "comment": "1st of May party",
    "sts_id": 33,
}

new_id = q.insert(tbl="event", dta=to_be_inserted)
print(new_id)
```


## To do

- [x] using correct (invalid/test/fake) mail SLDs for mocked data acc. 2 RFC ...
- [ ] Removing parts from `_apps` to separate repos
- [ ] Wipe& clean

### Installing SQLite DB from schema definitions
<pre>

<code>sven@thanos data %</code> <kbd> sqlite3 my_database.db < ../.schema/customer.sql </kbd>
<code>sven@thanos data %</code> <kbd> ls</kbd>
<code>my_database.db</code>

</pre>