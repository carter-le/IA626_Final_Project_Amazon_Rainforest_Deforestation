# Legal Amazon 
# COPY

import json

with open('LegalAmazonArea.json') as f:
  data = json.load(f)

newMap = {"type":"Polygon","coordinates":[[]]}
#print(newMap)

n = 0
for point in data['features'][0]['geometry']['coordinates'][0][0]:
    if n == 0:
        firstpoint = point
    if n % 10 == 0:
        newMap['coordinates'][0].append(point)
    n+=1 
newMap['coordinates'][0].append(firstpoint)
#print(newMap)

with open('reduced_Legal_Amazon.json', 'w') as json_file:
    json.dump(newMap, json_file)
