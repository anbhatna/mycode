#!/usr/bin/python3

import urllib.request
import json
import webbrowser
from pprint import pprint as pp #part of std lib

#define some constraints
NASAAPI='https://api.nasa.gov/planetary/apod?'
MYKEY='api_key=Icg2oXX7KxxKIVrv2mRfnGvGs9SepNZXCZdZevR5'

#pretty print JSON
def main():
    " " " run-time code " " "
    nasaapiobj=urllib.request.urlopen(NASAAPI + MYKEY)

    #read the file-like object
    nasaread=nasaapiobj.read()

    #decode json to python ds
    convertedjson = json.loads(nasaread.decode('utf-8'))

    #display pythonic data
    print("\n\n Converted Python Data")
    print(convertedjson)


    input('\n This is a converted json. Press Enter to continue.')

    pp(convertedjson)

    input ('\n This is pretty printed JSON')
    print(convertedjson['explanation'])
    input ('\n Press enter to view the photo of the day')

    webbrowser.open(convertedjson['hdurl'])

main()
