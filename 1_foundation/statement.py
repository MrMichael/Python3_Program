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
	
for value in list(range(2,5)):	#range生成从2开始小于5的数
	print(value)
	

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



	
