import mysql.connector
import json

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

with open ('doraemon.json', 'w') as x:
    x.write (str(d).replace("'",'"'))
    print(x)