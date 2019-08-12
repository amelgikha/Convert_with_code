import csv
import pymongo

# read csv
list1=[]
with open('doraemon.csv','r') as x:
    reader = csv.DictReader(x)
    for x in reader:
        list1.append(dict(x))
print(list1)

# write mongo
x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['doraemon']
col = db['teman']
for i in list1:
    col.insert_one(i)