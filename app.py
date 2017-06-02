#!flask/bin/python
from flask import Flask, jsonify
import datetime
import ephem

app = Flask(__name__)

@app.route('/api/v1.0/<float:latitude>,<float:longitude>')
def index(latitude,longitude):
    results = dict()
    myObserver = ephem.Observer()
    myObserver.lat = str(latitude)
    myObserver.lon = str(longitude)
    results['previous_rising'] = ((myObserver.previous_rising(ephem.Sun())).datetime()).isoformat()
    results['next_setting'] = ((myObserver.next_setting(ephem.Sun())).datetime()).isoformat()
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)
