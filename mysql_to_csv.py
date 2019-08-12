import mysql.connector
import csv

### ganti <host>,<user>,<password> sesuai mysql masing-masing ###
dbku = mysql.connector.connect(
    host =  '<host>',
    port = 3306,
    user = '<user>',
    passwd = '<password>',
    database = 'marvel'
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