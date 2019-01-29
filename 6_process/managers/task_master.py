#!/usr/bin/python3
# -*- coding: utf-8 -*-


#managers子模块还支持把多进程分布到多台机器上。
#一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。

#服务进程负责启动Queue，把Queue注册到网络上，然后往Queue里面写入任务

import random, time, queue
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = queue.Queue()
#接收结果的队列
result_queue = queue.Queue()

class QueueManager(BaseManager):
	pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue
manager.start()
# 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
	n = random.randint(0, 10000)
	print('Put task %d...' % n)
	task.put(n)	#往网络队列写入数据

print('Try get results...')
for i in range(10):
	r = result.get(timeout=10)	#从网络队列读出数据
	print('Result: %s' % r)

#关闭manager
manager.shutdown()





