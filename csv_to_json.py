import json
import csv

# read csv
# gunakan file csv yang kalian miliki
list1=[]
with open('doraemon.csv','r') as x:
    reader = csv.DictReader(x)
    for x in reader:
        list1.append(dict(x))
print(list1)

# write json
# tidak perlu membuat file json karena akan otomatis terbuat jika menggunakan kode di bawah ini
with open ('temandoraemon.json', 'w') as x:
    x.write (str(list1).replace("'",'"'))
print(x)
