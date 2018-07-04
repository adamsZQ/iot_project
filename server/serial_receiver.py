#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/2 下午9:27
# @Author  : zchai
import serial
import RPi.GPIO as GPIO
import time


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

ser = serial.Serial('/dev/ttyAMA0', 19200, timeout=1)

last_data = b''


def data_receiver(path):
    while True:
        print "data_receiver runningu"
        #ser.write(b'pi is running')
        data = ser.read(1)
        if len(data) < 1:
            continue
        print "this is data:", data
        if data.find(last_data):
            continue
        last_data = data

        for key in path:
            if data.find(key):
                # 0 直行， 1 右转， 2 停止， 3， 左转
                if path[key] == 0:
                    print '直行'
                    GPIO.output(a_pin1, True)
                    GPIO.output(a_pin2, False)
                    GPIO.output(b_pin1, True)
                    GPIO.output(b_pin2, False)
                elif path[key] == 1:
                    print '右转'
                    GPIO.output(a_pin1, True)
                    GPIO.output(a_pin2, False)
                    GPIO.output(b_pin1, False)
                    GPIO.output(b_pin2, False)
                    time.sleep(0.5)
                    GPIO.output(a_pin1, True)
                    GPIO.output(a_pin2, False)
                    GPIO.output(b_pin1, True)
                    GPIO.output(b_pin2, False)
                elif path[key] == 2:
                    print '停止'
                    GPIO.output(a_pin1, False)
                    GPIO.output(a_pin2, False)
                    GPIO.output(b_pin1, False)
                    GPIO.output(b_pin2, False)
                elif path[key] == 3:
                    print '左转'
                    GPIO.output(a_pin1, False)
                    GPIO.output(a_pin2, False)
                    GPIO.output(b_pin1, True)
                    GPIO.output(b_pin2, False)
                    time.sleep(0.5)
                    GPIO.output(a_pin1, True)
                    GPIO.output(a_pin2, False)
                    GPIO.output(b_pin1, True)
                    GPIO.output(b_pin2, False)

