import pymongo
import json

x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['marvel']
col = db['avengers']
data = list(col.find())
# print(data)

keys = []
vals = []
for key in data:
    keys.append(dict(key.keys()))
for val in data:
    vals.append(dict(val.values()))
# print(vals)
for key,val in zip(keys,vals):
    querydb = f''' insert into avengers {str(key).replace("'",'')} values{str(val)[9:].replace(')','')}) '''
    print(querydb)

with open ('avenger.json', 'w') as y:
    y.write (str(querydb).replace("'",'"'))
    print(y)