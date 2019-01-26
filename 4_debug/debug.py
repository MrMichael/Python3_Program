#!/usr/bin/python3
# -*- coding: utf-8 -*-

#断言（assert）
def foo(s):
	n = int(s)
	#如果条件（n != 0）为假，assert语句就会抛出AssertionError，错误内容为：'n is zero!'	
	assert n != 0, 'n is zero!'	
	return 10 / n

#foo('0')



#logging	输出错误信息到文件
#可以通过指定不同的消息级别输出不同的消息
import logging
#logging.basicConfig(level=logging.INFO)	#指定消息记录的级别，输出INFO级别及以上的消息
logging.basicConfig(level=logging.DEBUG)	#指定消息记录的级别

n = int('0')
logging.info('info n = %d' % n)
logging.debug('debug n = %d' % n)
#print(10 / n)


#设置断点
import pdb	#插入pdb模块，程序可以通过pdb插入断点调试

s = '1'
m = int(s)
pdb.set_trace()	#在这里设置断点，运行到这会自动暂停,Pdb中输入c继续运行
print(m)
