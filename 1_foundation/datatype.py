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
print('你好', 'python3')	#组合打印
print(e)

	
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


#字典dictionary		字典是无序的对象集合，字典的元素通过键来取
dict = {'name':'join', 'code':1234, 'dept':'sales', 5:'ok'}
print(dict)
print(dict['name'])	#通过键搜索值
print(dict[5])		#通过键搜索值
dict['age'] = 22	#添加元素
if dict.get('age'):
	print('%s is in dict' % 'age')
else:
	print('%s is not in dict' % 'age')
dict.pop(5)		#删除键值
print(dict.keys())	#打印所有键
print(dict.values())	#打印所有值


#集合set	集合是一组键的集合，但不包含值，而且键不能重复
s = set([1,2,3])	#创建一个set，需要提供一个list作为输入集合
print(s)
s.add(4)
s.add(3)
print(s)
s.remove(2)
print(s)
s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)	#set可以看成数学意义上的无序和无重复元素的集合


#数据类型转换
f = int('123')		#字符串转整型
g = int(123.456)	#浮点型转整型
h = float('123.4')	#字符串转浮点型
i = str(123)		#整型转字符串
j = tuple([1,2,3,4])		#列表转元组
k = tuple(set([1,2,3,4]))	#集合转元组
l = list((1,2,3)) 		#元组转列表
m = list(set([1,2,3])) 	#集合转列表
print(f)
print(g)
print(h)
print(i)
print(j)
print(k)
print(l)
print(m)










