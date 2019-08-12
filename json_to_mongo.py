import json
import pymongo

#read json
with open('temandoraemon.json') as y:
    data = json.load(y)
print (data)

# write mongo
x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['doraemon']
col = db['komplotan']
for i in data:
    col.insert_one(i)