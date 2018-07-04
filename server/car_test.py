#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/4 下午9:20
# @Author  : zchai
import RPi.GPIO as GPIO


enable_pin = 10
a_pin1 = 2
a_pin2 = 3
b_pin1 = 4
b_pin2 = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(a_pin1, GPIO.OUT)
GPIO.setup(a_pin2, GPIO.OUT)
GPIO.setup(b_pin1, GPIO.OUT)
GPIO.setup(b_pin2, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)
pwm = GPIO.PWM(enable_pin, 80)
# 小车将以90%的占空比运行
pwm.start(90)

GPIO.output(a_pin1, True)
GPIO.output(a_pin2, False)
GPIO.output(b_pin1, True)
GPIO.output(b_pin2, False)