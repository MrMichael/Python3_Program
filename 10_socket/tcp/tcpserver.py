#!/usr/bin/python3
# -*- coding: utf-8 -*-

import socket
import threading


# 创建socket	AF_INET指定使用IPv4协议，SOCK_STREAM指定使用面向流的TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       
s.bind(('192.168.83.130', 8000))	 # 绑定地址和端口
s.listen(5)	#最多监听5个客户端

def fun(sock, addr):
	print('Accept new connection from {}'.format(addr))
	sock.send('Hello!'.encode())	# 向客户端发送数据
	while True:
		data = sock.recv(1024)		# 每次最多接收1024b(1kb)
		if data == 'exit' or not data:
			break
		sock.send('hello,{}'.format(data).encode())	# 向客户端发送数据
	sock.close()
	print('Connection closed {}'.format(addr))

print('Waiting for connection...')
while True:
	sock, addr = s.accept()	# 等待连接，返回socket对象和请求连接的客户端地址
	# 创建新线程（或进程）来处理TCP连接
	t = threading.Thread(target=fun, args=(sock, addr))
	t.start()# 启动线程




