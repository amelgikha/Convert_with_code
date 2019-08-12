import json
import csv

# read csv
list1=[]
with open('doraemon.csv','r') as x:
    reader = csv.DictReader(x)
    for x in reader:
        list1.append(dict(x))
print(list1)

# write json
with open ('temandoraemon.json', 'w') as x:
    x.write (str(list1).replace("'",'"'))
print(x)