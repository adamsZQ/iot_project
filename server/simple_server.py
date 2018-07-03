#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 下午9:10
# @Author  : zchai

from flask import Flask
import RPi.GPIO as GPIO
import json
import threading

from serial_receiver import data_receiver

app = Flask(__name__)

enable_pin = 10
a_pin1 = 2
a_pin2 = 3
b_pin1 = 4
b_pin2 = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(a_pin1, GPIO.OUT)
GPIO.setup(a_pin2, GPIO.OUT)
GPIO.setup(b_pin1, GPIO.OUT)
GPIO.setup(b_pin2, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)
pwm = GPIO.PWM(enable_pin, 80)
# 小车将以90%的占空比运行
pwm.start(90)


@app.route('/initPath/<string:path>')
def init_path(path):
    print path
    global path_data
    path_data = path
    path_json = json.loads(path_data)

    t = threading.Thread(target=data_receiver, args=path_json)
    t.start()
    return 'path received'


@app.route('/switchOnCar')
def switch_on_car():
    # 启动小车
    GPIO.output(a_pin1, True)
    GPIO.output(a_pin2, False)
    GPIO.output(b_pin1, True)
    GPIO.output(b_pin2, False)

    print "car is running"


@app.route('/switchOffCar')
def switch_off_car():
    # 停止小车
    GPIO.output(a_pin1, False)
    GPIO.output(a_pin2, False)
    GPIO.output(b_pin1, False)
    GPIO.output(b_pin2, False)

    print "car is stopped"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=9988)
