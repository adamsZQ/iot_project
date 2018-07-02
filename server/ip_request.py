#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/21 下午6:26
# @Author  : zchai
import json

import requests

# r = requests.get('http://pv.sohu.com/cityjson?ie=utf-8')
# r = r.text
# json_data = r.split("{")
#
# ip = json.loads("{" + json_data[1].replace(';', ''))
#
# print ip.get('cip')
try:
    file = open('aa.txt', 'r')

except IOError,e:
    print e


