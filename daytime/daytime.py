#!/usr/bin/env python
from flask import Flask, jsonify
import datetime
import ephem

app = Flask(__name__)

@app.route('/api/v1.0/<string:latitude>,<string:longitude>')
def index(latitude,longitude):
    results = dict()
    myObserver = ephem.Observer()
    myObserver.lat = latitude
    myObserver.lon = longitude
    results['previous_rising'] = ((myObserver.previous_rising(ephem.Sun())).datetime()).isoformat()
    results['next_setting'] = ((myObserver.next_setting(ephem.Sun())).datetime()).isoformat()
    if (myObserver.next_setting(ephem.Sun()).datetime() > myObserver.next_rising(ephem.Sun()).datetime()):
        results['isDaylight'] = False
    else:
        results['isDaylight'] = True

    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
