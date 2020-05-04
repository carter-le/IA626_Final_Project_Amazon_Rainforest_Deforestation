import json

with open('reduced_Legal_Amazon.json') as f:
    polygon = json.load(f)
	
from geomet import wkt

print(wkt.dumps(polygon, decimals=4))

# when you get this copy into a word doc and remove the space in between the 