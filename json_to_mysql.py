import json
import mysql.connector

#read json
with open('temandoraemon.json') as x:
    data = json.load(x)
print (data)

# write mysql
### ganti <host>,<user>,<password> sesuai mysql masing-masing ###
dbku = mysql.connector.connect(
    host = '<host>',
    port = 3306,
    user = '<user>',
    passwd = '<password>',
    database = 'marvel'
)
kursor = dbku.cursor()
keys = []
for loop in range(len(data)):
    for key in data[loop].keys():
        keys.append(key)
keyx = sorted(list(set(keys)))
print(keyx)

kursor.execute('create table superhero( {} varchar(50))'.format(keyx[0]))
for item in range(len(keyx)-1):
    kursor.execute('alter table superhero add column {} varchar(50)'.format(keyx[item+1]))
    dbku.commit()

keys = []
vals = []
for key in data:
    keys.append(tuple(key.keys()))
for val in data:
    vals.append(tuple(val.values()))
print(vals)

for key,val in zip(keys,vals):
    querydb = f'''insert into superhero {str(key).replace("'",'')} values{str(val).replace(')','')})'''
    print(querydb)
    kursor.execute(querydb)
    dbku.commit()