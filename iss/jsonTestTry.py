#!/usr/bin/python3

import urllib.request
import json

#Trace the ISS
majortom = 'http://api.open-notify.org/astros.json'

#Call the webservice
groundctl = urllib.request.urlopen(majortom)

#put file object into helmet
helmet= groundctl.read()

##decode json to python ds

helmetson = json.loads(helmet.decode('utf-8'))

## display our pythonic data
print ("\n\nConverted Python Data")
print(helmetson)

print("\n\nPeople in Space:",helmetson['number'])
people=helmetson['people']
#print (people)

for i in people:
    print (i['name']+" on the "+i['craft'])
   # print(people[0])
