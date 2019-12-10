import csv
import json

infile = open("customersdata.json","r")
outfile = open ("file.csv","w")

writer = csv.writer(outfile)
for row in infile:
  data = json.loads(row)
  writer.writerow(data)