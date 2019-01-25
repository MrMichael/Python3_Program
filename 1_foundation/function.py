#!/usr/bin/python3
# -*- coding: utf-8 -*-

#函数定义与调用
def printstd( str ):		#函数的参数类型在实际调用中决定
	'打印传入的字符串到标准输出'
	print(str)
	return
	
printstd("function")
printstd(123)

f = printstd	#变量可以指向函数和调用函数
f('function f')

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


#递归函数
def fact(n):
	'递归处理参数'
	if n==1:
		return 1
	return n*fact(n-1)

print(fact(5))


#高阶函数		一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
print('Higher order function')
def add(a,b):
	return a+b

def fun1(x,y,f):
	return f(x,y)*y

print(fun1(1,2,add))


#高阶函数map	
#map()函数接收两个参数，一个函数，一个序列。
#map()将传入的函数依次作用到序列的每一个元素，把结果作为新的序列返回
print('Higher order function: map')
def f(x):
	return x*x;

r = map(f, range(5))
print(list(r))


#高阶函数reduce
#reduce()函数接收两个参数，一个函数，一个序列。
#reduce()将函数作用在序列上，这个函数必须接收两个参数，reduce将结果与序列下一元素作累积计算
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce	#插入reduce函数 only python3

print('Higher order function: reduce')
s = reduce(add, [1,2,3,4,5])
print(s)

#定义字典
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
	def fn(x,y):
		return x*10+y
	def char2num(s):
		return DIGITS[s]
	return reduce(fn, map(char2num, s))

print('sum:', str2int('1245'))


#高阶函数filter		过滤
#filter()函数接收两个参数，一个函数，一个序列。
#filter将传入的函数依次作用到序列的每一个元素，然后根据返回值为真的元素
print('Higher order function: filter')
def is_odd(n):
	return n % 2 == 1

m = filter(is_odd, range(10))
print(list(m))


#高阶函数sorted		排序
#sorted()函数接收两个参数，一个函数，一个序列。
#sorted通过参数key指定的函数依次作用到序列的每一个元素，并根据函数返回的结果对元素进行排序
print('Higher order function: sorted')
n = sorted([10,-5,3,-20,8], key=abs)	#序列按绝对值结果排序
print(n)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]	#字典元素的第一个对象
def by_score(t):
	return -t[1]	#字典元素的第一个对象
	
m = sorted(L, key=by_name)
print(m)
m = sorted(L, key=by_score)
print(m)


#返回函数			把函数作为结果值返回
print('Return function')
def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax = ax + n
		return ax
	return sum

f = lazy_sum(1,2,3,4,5)
print(f())	#当调用函数时，才真正计算求和结果

def createcounter():
	x = [0,]	#外部作用域 对内部函数counter而言，x就是外部变量
				#每返回一个函数，都有自己的外部变量，从初始值开始，调用函数，外部变量就保持改变
	def counter():
		x[0] += 1 	#对序列操作不是对变量赋值，而是对指向的对象赋值，不受局部作用域影响
		return x[0]
	return counter

counterA = createcounter()
counterB = createcounter()
print(counterA(),counterA(),counterA())
print(counterB(),counterB(),counterB())

k = 0
def outside():
	m = 1	#外部作用域
	n = 1
	global k	#声明为全局变量，不会重复定义一个变量
	k += 1
	def inside():
		m = 2	#局部作用域		两个m是不一样的变量
		nonlocal n	#声明为非局部变量，不会重复定义一个变量
		n += 1
		global k	#声明为全局变量，不会重复定义一个变量
		k += 1
		print(m,n,k)
		return
	inside()
	print(m,n,k)
	return

print('Return function call1')
outside()
print('Return function call2')
outside()
print('Return function call3')
outside()


#匿名函数
#关键字lambda表示匿名函数，冒号前面的表示函数参数，冒号后面的表示返回值。
print('Anonymous function')
m = map(lambda x: x * x, [1,2,3,4,5])
print(list(m))

f = filter(lambda n: n%2==1, range(10))
print(list(f))


#装饰器
#接受一个函数作为参数，并返回一个函数，即对函数进行装饰。
print('decorator')
#定义装饰器
def log(func):
	def wrapper(*args, **kv):	#参数定义为(*args, **kv)，可以接受任意参数的调用
		print('call %s()'% func.__name__)	#额外添加的代码
		return func(*args, **kv)	#运行函数原来的代码
	return wrapper

def now():
	print('2019-01-24')
	return

f = log(now)
f()

#使用python内置函数定义装饰器
import functools

def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kv):
		print('call %s()'% func.__name__)
		return func(*args, **kv)
	return wrapper

g = log(now)
g()

#带输入参数的装饰器
def log(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kv):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kv)
		return wrapper
	return decorator
		
h = log("hello")(now)
h()
		
	
#偏函数
#通过functools.partial函数，把一个函数的某些参数设置默认值，返回一个新函数
import functools

def info(x = 10, y = 5):
	print(x,y)
	return

print('functools partial')
info2 = functools.partial(info, y=2)	#将默认的10进制改为2进制
info2()
	
	
	
	
	

