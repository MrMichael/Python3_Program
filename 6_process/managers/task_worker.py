#!/usr/bin/python3
# -*- coding: utf-8 -*-


import random, time, queue
from multiprocessing.managers import BaseManager


class QueueManager(BaseManager):
	pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 连接到服务器，也就是运行task_master.py的机器
server_addr = '192.168.83.130'
print('Connect to server %s...' % server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 从网络连接:
manager.connect()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 从task队列取任务,并把结果写入result队列:
for i in range(10):
	try:
		n = task.get(timeout=1)	#从网络队列读出数据
		print('run task %d * %d...' % (n, n))
		r = '%d * %d = %d' % (n, n, n*n)	#处理数据
		time.sleep(1)
		result.put(r)	#往网络队列写入数据
	except Queue.Empty:
		print('task queue is empty')

# 处理结束:
print('worker exit.')



























