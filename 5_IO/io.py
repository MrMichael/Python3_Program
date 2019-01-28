#!/usr/bin/python3
# -*- coding: utf-8 -*-


PATH = '/home/michael/Python3_Program/5_IO/'

#读文本文件，并且是UTF-8编码的文本文件
try:
	f = open(PATH+'test.txt', 'r')	#打开文件
	#调用read()方法可以一次读取文件的全部内容，用一个str对象表示
	print(f.read())
finally:
	if f:
		f.close()	#关闭文件
	
#使用with语句自动调用close关闭文件
with open(PATH+'test.txt', 'r') as f:
	print(f.read())

#限定字节数读取read(size)
with open(PATH+'test.txt', 'r') as f:
	str = f.read(10)
	while str!='':	#限定一次读10bytes
		print(str)
		str = f.read(10)

#写文件	以覆盖形式写入
with open(PATH+'test.txt', 'w') as f:
	f.write('hello file2\n')	#当调用close时，系统才能保证数据已经写入文件

#写文件	以追加形式写入
with open(PATH+'test.txt', 'a') as f:
	f.write('hello file3\n')

#按行读取readline()
with open(PATH+'test.txt', 'r') as f:
	str = f.readline()
	while str!='':
		print(str.strip())	# 把末尾的'\n'删掉
		str = f.readline()

#读写二进制文件		比如图片、视频等
#以二进制格式打开
with open(PATH+'file.bin', 'rb') as f:
	str = f.readline()
	print(str)



#从内存中读写str	StringIO
print('StringIO')
from io import StringIO
f = StringIO()	#创建StringIO后就可以像普通文件那样读写
f.write('hello stringio')
print(f.getvalue())	#getvalue()方法用于获得写入后的str



#从内存中读写二进制数据		BytesIO
print('BytesIO')
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.tell())	#返回当前读写位置
f.write('hello'.encode('utf-8'))
print(f.tell())	#返回当前读写位置
print(f.getvalue())



#序列化pickle	
#把变量从内存中变成可存储或传输的过程称之为序列化，序列化后的内容可以写入磁盘或通过网络传输
#把变量内容从序列化的对象重新读到内存里称之为反序列化
print('pickle')
import pickle
d = dict(name='Bob', age=20, score=88)
bytes = pickle.dumps(d)	#pickle.dumps()方法把可序列化对象编码成bytes
print(bytes)	
e = pickle.loads(bytes)	#pickle.loads()方法将bytes反序列化出对象
print(e)

with open(PATH+'dump.txt', 'wb') as f:
	pickle.dump(d, f)	#pickle.dump()直接把对象序列化后写入一个file-like Object(文件描述符)

with open(PATH+'dump.txt', 'rb') as f:
	g = pickle.load(f)	#pickle.load()方法从一个file-like Object(文件描述符)中直接反序列化出对象
	print(g)


	
#序列化 JSON类型
#JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
print('json')
import json
d = dict(name='Tom', age=20, score=88)	# 不一定要字典，可序列化为JSON的对象都可以
jsonstr = json.dumps(d)	#json.dumps 用于将 Python 对象编码成 JSON 字符串。
print(jsonstr)
e = json.loads(jsonstr)	#json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型。
print(e)

with open(PATH+'json.txt', 'w') as f:
	json.dump(d, f)	#json.dump()直接把对象序列化后写入一个file-like Object(文件描述符)
	pass
	
with open(PATH+'json.txt', 'r') as f:
	g = json.load(f)	#json.load()方法从一个file-like Object(文件描述符)中直接反序列化出对象
	print(g)

#将类序列化为json
print('json class')
class Student(object):
	def __init__(self, name, age, score):
		self.name = name
		self.age = age
		self.score = score

def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}
	
def dict2student(d):
	return Student(d['name'], d['age'], d['score'])

s = Student('Jack', 20, 88)
#jsonstr = json.dumps(s, default=student2dict)	#需要传入将类转换为字典的函数
jsonstr = json.dumps(s, default=lambda obj: obj.__dict__) #class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。
print(jsonstr)
s1 = json.loads(jsonstr, object_hook=dict2student)
print(s1)





