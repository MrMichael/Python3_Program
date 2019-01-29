#!/usr/bin/python3
# -*- coding: utf-8 -*-

#备注：Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。

import time, threading

# 新线程执行的代码
def loop():
	print('thread %s is running...' % threading.current_thread().name)
	n = 0
	while n < 5:
		n = n + 1
		print('thread %s >>> %s' % (threading.current_thread().name, n))
		time.sleep(0.2)
	print('thread %s ended.' % threading.current_thread().name)


print('thread %s is running...' % threading.current_thread().name)
#传入执行函数和执行函数的参数
t = threading.Thread(target=loop, name='LoopThread')
t.start()	#启动线程
t.join()
print('thread %s ended.' % threading.current_thread().name)



#互斥量
#多线程中，所有变量都由所有线程共享，任何一个变量都可以被任何一个线程修改
balance = 0
lock = threading.Lock()

def change_it(n):
	global balance	#全局变量声明
	balance = balance + n
	balance = balance - n
	
def run_thread(n):
	for i in range(100000):
		lock.acquire()	#获取互斥锁
		try:
			change_it(n)
		finally:
			lock.release()	#释放互斥锁

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(5,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)



#ThreadLocal
#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
#ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
print('ThreadLocal')
import threading
local_school = threading.local()
temp_age = 12

def process_student():
	# 获取当前线程关联的student:
	std = local_school.student
	grade = local_school.grade
	age = temp_age	#函数中只读全局变量，不用声明
	print('Hello, %s %d %d(in %s)' % (std, grade, age, threading.current_thread().name))

def process_thread(name, grade, age):
	# 定义ThreadLocal的变量
	local_school.student = name	#ThreadLocal全局变量在每个线程中都有独立副本
	local_school.grade = grade
	#global temp_age
	temp_age = age	##函数中对全局变量赋值，需要声明，不声明代表赋值的局部变量变量
	process_student()

#name为线程名称
t1 = threading.Thread(target=process_thread, args=('Alice', 6, 14), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob', 5, 13), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()











