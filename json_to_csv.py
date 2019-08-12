import json
import csv

#read json
with open('data.json') as x:
    data = json.load(x)
print (data)

# write csv
with open('data.csv','w', newline='')as x:
    kolom = list(data[0].keys())
    writer = csv.DictWriter(x, fieldnames = kolom)
    writer.writeheader()
    writer.writerows(data)
print(data)