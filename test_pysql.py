import json
from db_connector import DB_TEST

db = DB_TEST('127.0.0.1', 'db_sensor_data', 'root', 'root')
print(db)


_query = 'select * from tbl_sensor5 where status is null'
data = db.execute(_query)
db.commit()
d
print(data)
bbb=1



db.close()
