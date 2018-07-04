#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 下午3:58
# @Author  : zchai
import json
import threading

import RPi.GPIO as GPIO

from serial_receiver import data_receiver

if __name__ == '__main__':
    path_json = '{"0":0, "1":1, "2":2, "3":3}'
    path_json = json.loads(path_json)
    t = threading.Thread(target=data_receiver, args=(path_json,))
    t.start()

# enable_pin = 10
# # a_pin1 = 2
# # a_pin2 = 3
# # b_pin1 = 4
# # b_pin2 = 5
# #
# # GPIO.setmode(GPIO.BCM)
# # GPIO.setup(a_pin1, GPIO.OUT)
# # GPIO.setup(a_pin2, GPIO.OUT)
# # GPIO.setup(b_pin1, GPIO.OUT)
# # GPIO.setup(b_pin2, GPIO.OUT)
# # GPIO.setup(enable_pin, GPIO.OUT)
# # pwm = GPIO.PWM(enable_pin, 80)
# # # 小车将以90%的占空比运行
# # pwm.start(90)
