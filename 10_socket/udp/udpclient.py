#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

 # 创建一个基于UDP的socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 向指定服务器与端口号发送内容
s.sendto('hello!'.encode(), ('192.168.83.130', 8000))
print(s.recv(1024))
s.close()





















