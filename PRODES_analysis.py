#PRODES data

import csv
import time

start = time.time()
fn = 'PRODES_deforestation.csv'

f = open(fn,"r")
reader = csv.reader(f) 


n = 0 
totalpieceslostperyr = {}
totalsqmeterslostperyr = {}
for row in reader:
    if n % 10000 == 0:
        print(n)
    if n > 0:
        date = row[2]
        if date in totalpieceslostperyr.keys():
            totalpieceslostperyr[date] += 1 
        else:
            totalpieceslostperyr[date] = 1 
        if date in totalsqmeterslostperyr.keys():
            totalsqmeterslostperyr[date] += round(float(row[5]), 0)
        else:
            totalsqmeterslostperyr[date] = round(float(row[5]),0)
         #this is more valuable because we don't entirely know about the pieces of land 
    n+=1
        
print(totalpieceslostperyr, totalsqmeterslostperyr)


