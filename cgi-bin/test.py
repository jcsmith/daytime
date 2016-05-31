#!/usr/bin/env python3

import cgi
import cgitb
import json
import ephem
import datetime

fs = cgi.FieldStorage()

location = json.loads(fs.getvalue('loc'))
location['timeStampAsDate'] = datetime.datetime.strptime(location['timeStampAsDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
myObserver = ephem.Observer()
myObserver.date = str(location['timeStampAsDate'])
myObserver.lat = str(location['latitude'])
myObserver.lon = str(location['longitude'])

dictMyObserver = {}

dictMyObserver['sunrise'] = myObserver.previous_rising(ephem.Sun()).datetime().isoformat() + 'Z'
dictMyObserver['sunset'] = myObserver.next_setting(ephem.Sun()).datetime().isoformat() + 'Z'

print("Content-type:application/json\r\n\r\n")
print (json.dumps(dictMyObserver))
