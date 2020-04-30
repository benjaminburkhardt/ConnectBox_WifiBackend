import flask
from flask import request

# Flask App
import wifi_tools

app = flask.Flask(__name__)
app.config["DEBUG"] = False


# Get WiFi status
@app.route('/wifi/status')
def status():
    connect_box_ip = str(request.args.get('ip', None))
    connect_box_password = str(request.args.get('password', None))

    enabled = wifi_tools.wifi_enabled(connect_box_ip, connect_box_password)

    if enabled:
        return "on"
    else:
        return "off"


# Enable WiFi
@app.route('/wifi/on')
def on():
    connect_box_ip = str(request.args.get('ip', None))
    connect_box_password = str(request.args.get('password', None))

    result = wifi_tools.change_wifi_to(connect_box_ip, connect_box_password, True)
    return result


# Disable WiFi
@app.route('/wifi/off')
def off():
    connect_box_ip = str(request.args.get('ip', None))
    connect_box_password = str(request.args.get('password', None))

    result = wifi_tools.change_wifi_to(connect_box_ip, connect_box_password, False)
    return result


app.run(debug=True, host="0.0.0.0")
