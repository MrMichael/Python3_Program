#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import threading

 # 创建一个基于UDP的socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('192.168.83.130', 8000))	# 绑定地址与端口

def fun(data, addr):
	print('from {}, content is {}'.format(addr, data))
	s.sendto('Hi!{}'.format(data).encode(), addr)	# 向客户端返回内容

while True:
	#等待接收客户端发送的内容
	data, addr = s.recvfrom(1024)	#返回客户端的数据和地址
	t = threading.Thread(target=fun, args=(data, addr))
	t.start()	# 启动线程
























