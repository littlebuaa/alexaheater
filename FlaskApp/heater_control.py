#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask
from flask_ask import Ask, statement, convert_errors
import RPi.GPIO as GPIO
import logging
from logging.handlers import RotatingFileHandler

GPIO.setmode(GPIO.BCM)
app = Flask(__name__)

ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)


# file_handler = logging.FileHandler('server_heater.log')
# file_handler.setLevel(logging.DEBUG)
# formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# file_handler.setFormatter(formatter)
# app.logger.addHandler(file_handler)

@app.route("/")
def hello():
    return "Hello world!"

@ask.intent('ControlHeater', mapping={'status': 'status'})
def gpio_control(status):
    # try:
        # pinNum = int(pin)
    # except Exception as e:
        # return statement('Pin number not valid.')
    pinNum =26
    GPIO.setup(pinNum, GPIO.OUT)

    if status in ['on', 'high']:
        GPIO.output(pinNum, GPIO.HIGH)
        return statement('Yo beach, The fa king heater is {}, Are you satisfied!'.format(status))
    if status in ['off', 'low']:
        GPIO.output(pinNum, GPIO.LOW)
        return statement('Yo beach, I"m turning the fa king heater {}, Kiss my Ass, beach!'.format(status))
    
if __name__ == '__main__':
    app.run(port=5000)
