#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os	#插入系统调用模块

print('Process %s start...' % os.getpid())	#通过系统调用获取当前进程id
# Only works on Unix/Linux/Mac, Windows没有fork调用，
pid = os.fork()
if pid == 0:
	#child
	print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
	#parent
	print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

