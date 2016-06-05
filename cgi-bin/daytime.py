#!/usr/bin/env python3

import cgi
import datetime
import ephem
import json

fs = cgi.FieldStorage()

location = json.loads(fs.getvalue('loc'))

#Convert timestamp to python datetime object.
location['timeStampAsDate'] = datetime.datetime.strptime(location['timeStampAsDate'], '%Y-%m-%dT%H:%M:%S.%fZ')

#Create pyephem observer using the timestamp and coordinates provided.
myObserver = ephem.Observer()
myObserver.date = str(location['timeStampAsDate'])
myObserver.lat = str(location['latitude'])
myObserver.lon = str(location['longitude'])

#Create an empty dictionary to hold results of sunrise/sunset calculations for json serialization.
dictMyObserver = {}

#Since we are primarly integrating with javascript on the frontend and it seems to assume
#a datetime string with no time zone specified is local time and _NOT_ UTC time we must
#append a Z to the end of the datetime string.  This seems like a hack but I have not been able
#to find a better solution anywhere online.

dictMyObserver['sunrise'] = myObserver.previous_rising(ephem.Sun()).datetime().isoformat() + 'Z'
dictMyObserver['sunset'] = myObserver.next_setting(ephem.Sun()).datetime().isoformat() + 'Z'

#"Return" a JSON object to the webserver.
print("Content-type:application/json\r\n\r\n")
print (json.dumps(dictMyObserver))
