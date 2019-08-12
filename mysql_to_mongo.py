import mysql.connector
import pymongo

dbku = mysql.connector.connect(
    host = '<host>',
    port = 3306,
    user = '<user>',
    passwd = '<password>',
    database = 'doraemon'
)

kursor = dbku.cursor()
querydb = '''select * from karakter'''
kursor.execute(querydb)
# print(kursor.fetchall())
b = kursor.fetchall()
d = [{'id': item [0],'nama':item[1],'usia':item[2]}for item in b]

x = pymongo.MongoClient('mongodb://localhost:27017')
db = x['doraemon']
col = db['karakter']

for i in d:
    y = col.insert_one(i)