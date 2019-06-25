#!/usr/bin/python3

import requests

##Define NEOapi
def main():
    neourl='https://api.nasa.gov/neo/rest/v1/feed?'
    mykey='&api_key=Icg2oXX7KxxKIVrv2mRfnGvGs9SepNZXCZdZevR5'
    startdate='start_date=2018-06-01'
    enddate='&end_date=END_DATE'

    neourl= neourl + startdate + mykey

    #Call the webservice
    neojson=(requests.get(neourl)).json()

    #read the file-like object
    print(neojson)

main()
