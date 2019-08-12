import csv
import mysql.connector

list1=[]
with open('doraemon.csv','r') as x:
    reader = csv.DictReader(x)
    for x in reader:
        list1.append(dict(x))
print(list1)

### ganti <host>,<user>,<password> sesuai mysql masing-masing ###
dbku = mysql.connector.connect(
    host = '<host>',
    port = 3306,
    user = '<user>',
    passwd = '<password>',
    database = 'doraemon'
)
kursor = dbku.cursor()
keys = []
for loop in range(len(list1)):
    for key in list1[loop].keys():
        keys.append(key)
keyx = sorted(list(set(keys)))
print(keyx)

kursor.execute('create table karakter1( {} varchar(50))'.format(keyx[0]))
for item in range(len(keyx)-1):
    kursor.execute('alter table karakter1 add column {} varchar(50)'.format(keyx[item+1]))
    dbku.commit()

keys = []
vals = []
for key in list1:
    keys.append(tuple(key.keys()))
for val in list1:
    vals.append(tuple(val.values()))
print(vals)

for key,val in zip(keys,vals):
    querydb = f'''insert into karakter1 {str(key).replace("'",'')} values{str(val).replace(')','')})'''
    print(querydb)
    kursor.execute(querydb)
    dbku.commit()