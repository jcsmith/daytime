#!/usr/bin/env python3

import cgi
import datetime
import ephem
import json
import sys

##################################################
#Since we are actively developing the script lets include cgitb
#and have it log to a fike.  This will be removed once we are at
#a more steady state.
##################################################
import cgitb
cgitb.enable(display=0, logdir="/var/log/cgitb.log")

#function to return HTTP 400 Bad Request Error
def returnHTTP400 ():
    print ('Status: 400 Bad Request')
    print ()

def observer2output(observer):
    dictObserver = {}

    #Since we are primarly integrating with javascript on the frontend and it seems to assume
    #a datetime string with no time zone specified is local time and _NOT_ UTC time we must
    #append a Z to the end of the datetime string.  This seems like a hack but I have not been able
    #to find a better solution anywhere online.

    dictObserver['previous_sunrise'] = observer.previous_rising(ephem.Sun()).datetime().isoformat() + 'Z'
    dictObserver['next_sunrise'] = observer.next_rising(ephem.Sun()).datetime().isoformat() + 'Z'
    dictObserver['previous_sunset'] = observer.previous_setting(ephem.Sun()).datetime().isoformat() + 'Z'
    dictObserver['next_sunset'] = observer.next_setting(ephem.Sun()).datetime().isoformat() + 'Z'
    dictObserver['is_daylight'] = is_daylight(observer)

    return (json.dumps(dictObserver))

def is_daylight(observer):
    #given a pyephem observer return true if it is currently daylight
    #false otherwise.
    if (observer.next_setting(ephem.Sun()).datetime() > observer.next_rising(ephem.Sun()).datetime()):
        return False
    else:
        return True

fs = cgi.FieldStorage()

location = fs.getfirst('loc')
try:
    location = json.loads(location)
except:
    returnHTTP400()
    sys.exit()

#Create pyephem observer using the coordinates provided.
try:
    myObserver = ephem.Observer()
    myObserver.lat = str(location['latitude'])
    myObserver.lon = str(location['longitude'])
except:
    returnHTTP400()
    sys.exit()



output = observer2output(myObserver)

#"Return" a JSON object to the webserver.
print("Content-type:application/json\r\n\r\n")
print (output)
