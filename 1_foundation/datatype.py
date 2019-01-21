#!/usr/bin/python3

a = 12
b = 0x12
c = 3.14
d = 'hello world'
e = True

print(a)
print('%s' % a)	#数据类型是在被调用的时候定义的
print('0x%x' % b)
print(c)
print('%s' % d)
print('I\'m \"OK\"!')	#字符串内含有特性字符可以使用转义字符
print('''michael
jack
tony''')	#打印多行的其中一种方法

if e:
	print('OK')
else:
	print('Fail')