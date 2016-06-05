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



#Create an empty dictionary to hold results of sunrise/sunset calculations for json serialization.
dictMyObserver = {}

fs = cgi.FieldStorage()

location = fs.getfirst('loc')
try:
    location = json.loads(location)
except:
    returnHTTP400()
    sys.exit()



offset = fs.getfirst("offset")
try:
    offset = json.loads(offset)
except:
    dictMyObserver['offset'] = "0"




#Convert timestamp to python datetime object.
try:
    location['timeStampAsDate'] = datetime.datetime.strptime(location['timeStampAsDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
except:
    returnHTTP400()
    sys.exit()

#Create pyephem observer using the timestamp and coordinates provided.
try:
    myObserver = ephem.Observer()
    myObserver.date = str(location['timeStampAsDate'])
    myObserver.lat = str(location['latitude'])
    myObserver.lon = str(location['longitude'])
except:
    returnHTTP400()
    sys.exit()


#Since we are primarly integrating with javascript on the frontend and it seems to assume
#a datetime string with no time zone specified is local time and _NOT_ UTC time we must
#append a Z to the end of the datetime string.  This seems like a hack but I have not been able
#to find a better solution anywhere online.

dictMyObserver['sunrise'] = myObserver.previous_rising(ephem.Sun()).datetime().isoformat() + 'Z'
dictMyObserver['sunset'] = myObserver.next_setting(ephem.Sun()).datetime().isoformat() + 'Z'

#"Return" a JSON object to the webserver.
print("Content-type:application/json\r\n\r\n")
print (json.dumps(dictMyObserver))
