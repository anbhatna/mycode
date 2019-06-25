#!/usr/bin/python3

import urllib.request
import json

##Define NEOapi
neourl='https://api.nasa.gov/neo/rest/v1/feed?'
mykey='&api_key=Icg2oXX7KxxKIVrv2mRfnGvGs9SepNZXCZdZevR5'
startdate='start_date=2018-06-01'
enddate='&end_date=END_DATE'

neourl= neourl + startdate + mykey

#Call the webservice
neourlobj=urllib.request.urlopen(neourl)

#read the file-like object
neoread=neourlobj.read()

#decode json to python ds
decodeneo = json.loads(neoread.decode('utf-8'))

#display pythonic data
print("\n\n Converted Python Data")
print(decodeneo)

