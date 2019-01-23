#!/usr/bin/python3
# -*- coding: utf-8 -*-

#函数定义与调用
def printstd( str ):		#函数的参数类型在实际调用中决定
	'打印传入的字符串到标准输出'
	print(str)
	return
	
printstd("function")
printstd(123)

def calsum( value ):
	'将传入的参数求和'
	sum = 0
	for i in value:
		sum = sum + i
	return sum
	
print('sum is', calsum([1,2,3]))
print('sum is', calsum((1,2,3)))


#默认参数
def printinfo(name = 'jack', age = 22):
	'打印传入的信息'
	print('name:', name)
	print('age:', age)
	return
	
printinfo()


#不定长度参数		加了星号（*）的变量名会存放所有未命名的变量参数
def printinfo2( argc, *argv ):
	"打印任何传入的参数"
	print(argc)
	print('argv len:', len(argv))
	for var in argv:
		print(var)
	return
	
printinfo2(5,['a','b'],2,3,4)


#匿名函数









