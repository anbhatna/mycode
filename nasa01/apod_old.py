#!/usr/bin/python3

import urllib.request
import json
import webbrowser

##Define APOD
apodurl='https://api.nasa.gov/planetary/apod?'
mykey='api_key=Icg2oXX7KxxKIVrv2mRfnGvGs9SepNZXCZdZevR5'

#Call the webservice
apodurlobj=urllib.request.urlopen(apodurl + mykey)

#read the file-like object
apodread=apodurlobj.read()

#decode json to python ds
decodeapod = json.loads(apodread.decode('utf-8'))

#display pythonic data
print("\n\n Converted Python Data")
print(decodeapod)

##use firefox to open the HTTPS URL
input('\n Use browser to open Picture of the Day by NASA')
webbrowser.open(decodeapod['url'])
