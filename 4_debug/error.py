#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy


import logging	#logging模块可以非常容易地记录错误信息

print('START')
try:	#如果try代码块出错，就会执行except代码块
	print('try...')
	#int('a')
	r = 10 / 0
	print('result:', r)
except ValueError as e:		#如果except捕获到ValueError类型错误，则执行
	print('ValueError:', e)
	logging.exception(e)
except ZeroDivisionError as e:	#如果except捕获到ZeroDivisionError类型错误，则执行
	print('ZeroDivisionError:', e)
	logging.exception(e)	#可以帮助分析错误位置
else:
	print('no error!')
finally:	#finally代码块一定被执行
	print('finally')
print('END')



#抛出错误
#因为错误是class，捕获一个错误就是捕获到该class的一个实例
class FooError(ValueError):
	pass

def foo(s):
	n = int(s)
	if n == 0:
		raise FooError('invaild value:%s' % s) #raise语句抛出一个错误的实例
	return 10 / n

foo('0')





