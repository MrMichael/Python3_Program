#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket

#创建socket	AF_INET指定使用IPv4协议，SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接，参数是tuple类型
s.connect(('192.168.83.130', 8000))

print(s.recv(1024))
for data in ['li', 'bo', 'ca']:
	s.send(data.encode())	# 向服务器发送数据	对发送的数据进行加密
	print(s.recv(1024))		# 每次最多接收1024b(1kb)
s.send('exit'.encode())
s.close()




















