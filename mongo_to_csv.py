import mysql.connector
import csv

dbku = mysql.connector.connect(
    host =  '<host>',
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
# print (d)

with open('doraemon.csv','w', newline='')as x:
    kolom = list(['id','nama','usia'])
    writer = csv.DictWriter(x, fieldnames = kolom)
    writer.writeheader()
    writer.writerows(d)