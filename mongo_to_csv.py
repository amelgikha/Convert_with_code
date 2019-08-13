import pymongo
import csv

# read mongo
x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['doraemon']
col = db['karakter']
data = list(col.find())
# print(data)

# write csv
with open('doraemon.csv','w', newline='')as x:
    kolom = list(['id','nama','usia'])
    writer = csv.DictWriter(x, fieldnames = kolom)
    writer.writeheader()
    writer.writerows(data)
