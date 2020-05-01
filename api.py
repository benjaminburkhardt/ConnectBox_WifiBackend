import flask
from flask import request

# Flask App
import wifi_tools

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# Get WiFi status
@app.route('/wifi/status')
def status():
    connect_box_ip = request.args.get('ip', None)
    connect_box_password = request.args.get('password', None)

    print(connect_box_ip, connect_box_password)

    if connect_box_ip is not None and connect_box_password is not None:
        if wifi_tools.wifi_enabled(str(connect_box_ip), str(connect_box_password)):
            return "on"
        else:
            return "off"
    else:
        return "Please provide ip and password!"


# Enable WiFi
@app.route('/wifi/on')
def on():
    return toggle_to(True)


# Disable WiFi
@app.route('/wifi/off')
def off():
    return toggle_to(False)


def toggle_to(turn_wifi_on):
    connect_box_ip = request.args.get('ip', None)
    connect_box_password = request.args.get('password', None)

    if connect_box_ip is not None and connect_box_password is not None:
        result = wifi_tools.change_wifi_to(str(connect_box_ip), str(connect_box_password), turn_wifi_on)

    else:
        result = "Please provide ip and password!"
    return result


app.run(debug=True, host="0.0.0.0", port=80)
