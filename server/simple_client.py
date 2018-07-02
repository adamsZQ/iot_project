#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/19 下午8:43
# @Author  : zchai
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s = socket.socket()
s.connect(('172.20.10.2',9999))
s.send('shopping4:0,3:2')
# "aaa"shopping_path = {}
# if len(shopping_path) != 0:
#     print