from flask import Flask, render_template, redirect, url_for, request, send_from_directory
import RPi.GPIO as GPIO

app = Flask(__name__)

pins = (21,12)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.output(21, GPIO.HIGH)
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    
@app.route('/on')
def on():
    GPIO.output(21, GPIO.HIGH)
    return render_template('on.html')

@app.route('/off')
def off():
    GPIO.output(21, GPIO.LOW)
    return render_template('off.html')

@app.route('/assets/<filename>')
def assets(filename):
    return send_from_directory('assets',filename)

