#!/usr/bin/python3
# -*- coding: utf-8 -*-

'a test module'	#任何模块的第一行字符串被视为模块的文档注释

__author__ = 'Michael Lee'

import sys	#导入sys模块

def test():
	args = sys.argv		#sys.argv指向命令行的所有参数
	if len(args) == 1:
		print('hello world')
	elif len(args) == 2:
		print('hello, %s' % args[1])
	else:
		print('Too many arguments')
		
#_xxx和__xxx这样的函数或变量表示私有的，不应该被外部引用
def _private_1(name):
	return 'Hello, %s' % name
		
def _private_2(name):
	return 'Hi, %s' % name		
		
def greeting(name):
	if len(name) > 3:
		return _private_1(name)
	else:
		return _private_2(name)
		
	
#如果运行模块，解析器会将特殊变量__name__置为__main__
#所以如果是运行模块，就调用模块函数；只是导入模块，则不会运行
if __name__=='__main__':	
	test()
	
