#!/usr/bin/python3

import urllib.request
import json
import turtle
import time

#Trace the ISS - earth orbital space station
eoss = 'http://api.open-notify.org/iss-now.json'

##Call the webserver
trackiss = urllib.request.urlopen(eoss)

##put into file object
ztrack=trackiss.read()

#json to python ds
result = json.loads(ztrack.decode('utf-8'))

#display the pythonic data

print("\n \n Converted python data")
print(result)
input ('\n ISS data retrieved and converted. Press any key to continue')

location=result['iss_position']
lat=location['latitude']
lon=location['longitude']
print('\n Latitude:',lat)
print('\n Longitude:',lon)

screen =turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('iss_map.gif')
screen.register_shape('spriteiss.gif')
iss=turtle.Turtle()
iss.shape('spriteiss.gif')
iss.setheading(90)

lon=round(float(lon))
lat=round(float(lat))
iss.penup()
iss.goto(lon,lat)
yellowlat=25
yellowlon=74
mylocation=turtle.Turtle()
mylocation.penup()
mylocation.color('yellow')
mylocation.goto(yellowlon,yellowlat)
mylocation.dot(5)
mylocation.hideturtle()

passiss = 'http://api.open-notify.org/iss-pass.json'
passis=passiss+'?lat='+str(yellowlat)+'&lon='+str(yellowlon)
response=urllib.request.urlopen(passis)
result=json.loads(response.read().decode('utf-8'))

print(result)

over=result['response'][1]['risetime']
style=('Arial',6,'bold')
mylocation.write(time.ctime(over),font=style)

turtle.mainloop()


