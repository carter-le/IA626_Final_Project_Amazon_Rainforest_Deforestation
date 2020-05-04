# FIRMS data 

import csv
import time

start = time.time()
fn = 'fire_archive_M6_118818.csv'
#fn = 'fire_archive_M6_115418.csv'

f = open(fn,"r")
reader = csv.reader(f) 


n = 0
totalfireareaperyr = {}
totalfirevegitation = {}
totalfireotherstatic = {}
for row in reader:
    if n % 10000 == 0:
        print(n)
    if n > 0:
        if int(row[9]) > 74:
            if row[14] == "0" or row[14] == "2":
                date = row[5][0:4]
                #print(date)
                #print(row[14])
                if date in totalfireareaperyr.keys():
                    totalfireareaperyr[date] += 1
                    #each row represents 1km area where there is a fire (this is the highest level of granularity that we have)
                else:
                    totalfireareaperyr[date] = 1
            if row[14] == "0":
                if date in totalfirevegitation.keys():
                    totalfirevegitation[date] += 1
                else:
                    totalfirevegitation[date] = 1
                    
            if row[14] == "2":
                if date in totalfireotherstatic.keys():
                    totalfireotherstatic[date] +=1
                else:
                    totalfireotherstatic[date] =1

    n+=1
print(totalfireareaperyr) 
print(totalfirevegitation)
print(totalfireotherstatic)


'''
with open('test.csv', 'w' ) as file:
    writer = csv.writer(file)
    writer.writerows(totalfireareaperyr)
    '''


