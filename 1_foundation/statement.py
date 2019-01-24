#!/usr/bin/python3
# -*- coding: utf-8 -*-


#条件判断
age = '12'#input("birth:")	#input输出的是字符串
age = int(age)
if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')
	
	
#for循环
print("for")
i = [1,2,3]
for value in i:
	print(value)
	
print("for list range")
for value in list(range(2,5)):	#range生成从2开始小于5的数
	print(value)
	
print("for range")
for value in range(2,5):	#range生成从2开始小于5的数
	print(value)
	
l = [1,2,3,4,5,6]
for var in l[2:4]:	#分段循环
	print(var)

print("for multi variate")
people = {'name':'jony', 'age':22, 'adpt':'sale'}
for item, value in people.items():	#多变量
	print(item,'\t:',value)
	
	
#while循环
print("while")
n = 0
while n < 5:
	print(n)
	n += 1
	

#break
print("break")
n = 0
while n < 10:
	if n > 5:
		break
	print(n)
	n += 1
	
	
#continue
print("continue")
n = 0
while n < 10:
	n += 1
	if n == 5:
		continue
	print(n)


#列表生成式
print("List Comprehensions")
num1 = [x*x for x in range(1,5)]
num2 = [x*y for x in range(1,5) for y in range(2,5)]	#两重循环
P = [str(item) + '=' + str(value) for item, value in people.items()]
print(num1)
print(num2)
print(P)


#生成器		在循环的过程中不断推算出后续的元素,不必创建完整的list，从而节省大量的空间
print("generator")
g = (x*x for x in range(1,5))	#通过生成器产生的对象与元组是不同的
k = (1,2,3,4)
print(g)
print(k)

for n in g:	#生成器和元组、列表都能迭代，但是生成器占用空间很少
	print(n)

for n in k:
	print(n)

def odd():
	print('step1')
	yield(1)	#函数中有yield，那么函数就会变为生成器
	print('step2')
	yield(3)
	print('step3')
	yield(5)
	return 
o = odd()
next(o)		#每次调用next()，开始执行，遇到yield返回参数，再次执行next从上次返回yield的地方执行
next(o)
next(o)

for var in odd():
	print(var)


