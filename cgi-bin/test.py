#!/usr/bin/env python3

import cgi
import cgitb
import json
import ephem

fs = cgi.FieldStorage()

location = json.loads(fs.getvalue('loc'))
myObserver = ephem.Observer()
myObserver.date =  '2016/05/29 17:00'
myObserver.lat = str(location['latitude'])
myObserver.lon = str(location['longitude'])

dictMyObserver = {}

dictMyObserver['sunrise'] = myObserver.previous_rising(ephem.Sun()).datetime().isoformat()
dictMyObserver['sunset'] = myObserver.next_setting(ephem.Sun()).datetime().isoformat()

print("Content-type:text/html\r\n\r\n")
print ("Sunrise: ")
print (myObserver.previous_rising(ephem.Sun()))
print (" UTC </br>")
print ("Sunset: ")
print (myObserver.next_setting(ephem.Sun()))
print (" UTC </br>")
print (json.dumps(dictMyObserver))
