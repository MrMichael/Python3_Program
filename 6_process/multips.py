#!/usr/bin/python3
# -*- coding: utf-8 -*-

#跨平台版本的多进程模块	multiprocessing
#multiprocessing模块提供了一个Process类来代表一个进程对象
from multiprocessing import Process
import os


#子进程要执行的代码
def run_proc(name):
	print('Run child process %s (%s).' % (name, os.getpid()))

if __name__ == '__main__':
	#传入执行函数和执行函数的参数
	print('Parent process %s.' % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print('Child process will start.')
	p.start()
	p.join()	#等待子进程结束后再继续往下运行
	print('Child process end.')



#进程池的方式批量创建子进程	Pool
print('\n')
from multiprocessing import Pool
import os, time, random

def long_timr_task(name):
	print('Run task %s (%s)...' % (name, os.getpid()))
	start = timr.time()
	time.sleep(random.random()*3)
	end = time.time()
	print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
	print('Parent process %s.' % os.getpid())
	p = Pool(4)	#定义一个进程池，最大进程数4
	for i in range(5):
		#Pool.apply_async(要调用的目标,(传递给目标的参数元祖,))
		#每次循环将会用空闲出来的子进程去调用目标
		p.apply_async(long_timr_task, args=(i,))
	print('Waiting for all subprocesses done...')
	p.close()	#关闭pool，使其不在接受新的任务。
	p.join()	#等待子进程结束后再继续往下运行
	print('All subprocesses done.')


	
#子进程subprocess模块
#subprocess模块可以方便地启动一个子进程，然后控制其输入和输出。
print('\n')
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])	#运行外部进程，命令nslookup
print('Exit code:', r)
r = subprocess.call(['pwd',])	#运行外部进程，命令pwd
print('Exit code:', r)



#进程间通信
#Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
print('\n')
from multiprocessing import Process, Queue
import os, time, random

#写进程代码
def ps_write(q):
	print('Process to write: %s' % os.getpid())
	for value in ['A', 'B', 'C']:
		print('Put %s to queue...' % value)
		q.put(value)
		time.sleep(random.random())

#读进程代码
def ps_read(q):
	print('Process to read: %s' % os.getpid())
	while(True):
		value = q.get(True)
		print('Get %s from queue.' % value)
	
if __name__=='__main__':
	q = Queue()	#创建队列
	pw = Process(target=ps_write, args=(q,))
	pr = Process(target=ps_read, args=(q,))
	pw.start()
	pr.start()
	pw.join()
	pr.terminate()	#pr进程里是死循环，无法等待其结束，只能强行终止
	


