#!/usr/bin/python3
# -*- coding: utf-8 -*-

#整型、浮点型、字符串、布尔类型
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
print('你好')
print(e)


#类型转换
f = int('123')		#字符串转整型
g = int(123.456)	#浮点型转整型
h = float('123.4')	#字符串转浮点型
i = str(123)		#整型转字符串
print(f)
print(g)
print(h)
print(i)

	
#列表list	元素可以是不同数据类型
classmates = ['michael', 'jack', 'tony']
print(classmates)
classmates.append('gavin')	#追加元素
print(classmates)
classmates.insert(1, 'tom')	#插入元素
print(classmates)
classmates.pop()	#删除末尾元素
print(classmates)
classmates.pop(2)	#删除指定位置元素
print(classmates)
classmates[1] = 'lily'	#修改元素
print(classmates)
classmates[2] = 123	
print(classmates)


#元组tuple  元素可以是不同数据类型,一旦初始化就不能修改
fruit = ('apple', 'banana', 'orange', 123)
print(fruit)
fruit = ('apple', classmates, 'orange')	#变量可以被重定义
print(fruit)
fruit[1][0] = 'ming'	#如果元组中含有可变元素，则可变元素的内容是可修改的
fruit[1][1] = 'jim'
print(fruit)
print(classmates)




#条件判断
age = '12'#input("birth:")
age = int(age)
if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')








