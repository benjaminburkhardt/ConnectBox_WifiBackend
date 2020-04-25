from flask import Flask
from flask_ask import Ask, statement, convert_errors
import logging
import toggle_wifi

GPIO.setmode(GPIO.BCM)

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

def toggle_wifi_service():

    return statement(toggle_wifi.switch_wifi())