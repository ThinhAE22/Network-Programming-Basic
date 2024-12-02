import json
# For creating a server application:
from flask import Flask, render_template, request, Response

app = Flask(__name__)       # global Flask-server instance
measurements = []           # global list for measurements

# Root path (/)
@app.route('/')
def get_all_measurements_page():
    """
    Opens page result.html (in templates folder) and renders
    measurements to it.
    """
    return render_template("result.html", result = measurements)

# Path /newmeasurement
@app.route('/newmeasurement/', methods = ['POST'])
def new_measurement():
    """
    Receives HTTP POST request contaning measurement data and adds the data
    to the list (measurements).
    """
    meas = request.get_json(force = True)
    measurements.append(meas)
    return json.dumps(meas, indent = True)

if __name__ == '__main__':
   app.run(debug = True)
   