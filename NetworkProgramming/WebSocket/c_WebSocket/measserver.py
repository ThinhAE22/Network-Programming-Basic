import json
# For creating a server application:
from flask import Flask, render_template, request, Response
from flask_socketio import SocketIO, emit

app = Flask(__name__)       # global Flask-server instance
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

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

    s = json.dumps(meas)
    # socketio.emit('my_response', {'result': s}, broadcast=True)
    socketio.emit('my_response', {'result': s})

    return json.dumps(meas, indent = True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
   