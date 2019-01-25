#!/usr/bin/python3
# -*- coding: utf-8 -*-


#当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法
class Student(object):
	pass
	
s = Student()
s.name = 'Jack'	#动态给实例绑定一个属性，只对当前实例有效
print(s.name)

def set_age(self, age):
	self.age = age	#调用时动态给实例绑定一个属性
	
from types import MethodType
s.set_age = MethodType(set_age, s) #给实例绑定一个方法
s.set_age(23)
print(s.age)

Student.name = ''	#直接给类动态绑定属性
Student.set_age = set_age	#直接给类动态绑定方法, 这样所有实例都可以调用
Tom = Student()
Tom.set_age(25)
print(Tom.age)



#限制类的属性__slots__ 
class People(object):
	__slots__ = ('name', 'age')	## 用tuple定义允许绑定的属性名称

Worker = People()
Worker.name = 'Mike'
Worker.age = 26
#Worker.height = 180
print(Worker.name, Worker.age)
