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
print('__slots__')
class People(object):
	__slots__ = ('name', 'age')	## 用tuple定义允许绑定的属性名称

Worker = People()
Worker.name = 'Mike'
Worker.age = 26
#Worker.height = 180
print(Worker.name, Worker.age)



#类的装饰器@property	可以把一个类方法转换为类属性
#用属性的方式操作方法，使调用更简单，也可以很好保护内部参数，避免乱设置
print('@property')
class Animal(object):

	#初始化时的实例属性
	def __init__(self, skill, age):
		self.__skill = skill
		self.__age = age

	@property	#装饰器@property把一个getter方法变为属性，可读功能
	def skill(self):
		return self.__skill

	@skill.setter	#装饰器@skill.setter把一个setter方法变为属性，可写功能
	def skill(self, skill):
		self.__skill  = skill
		
	@property	#装饰器@property把一个getter方法变为属性，可读功能
	def age(self):
		return self.__age

	@age.setter	#装饰器@skill.setter把一个setter方法变为属性，可写功能
	def age(self, age):
		self.__age  = age

cat = Animal('run', 2)
print(cat.skill, cat.age)	#方法变为了属性
#print(cat.skill(), cat.age())	#当作方法调用会出错
cat.skill = 'eat'	#该属性可写
cat.age = 3
print(cat.skill, cat.age)



#多重继承
#一个子类可以从多个父类中继承
print('Multiple inheritance')
class Runable(object):
	def run(self):
		print('Running')

class Flyable(object):
	def fly(self):
		print('Flying')

class Mammal(Animal, Runable):	#子类同时继承了多个父类
	pass

class Bird(Animal, Flyable):
	pass
	
dog = Mammal('run', 2)
parrot = Bird('fly', 3)
print(dog.skill, dog.age)
dog.run()
print(parrot.skill, parrot.age)
parrot.fly()



#枚举类
print('Enumeration class')

#一般的枚举类型
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Jan.value)
for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

#枚举类
from enum import Enum, unique

@unique	#@unique装饰器可以帮助我们检查保证没有重复值
class Weekday(Enum):	#从父类Enum中继承
	Sun = 0 # Sun的value被设定为0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

day = Weekday.Sun
print(Weekday.Sun)
print(Weekday.Sun.value)
print(day == Weekday.Sun)

@unique
class Gender(Enum):
	Male = 0
	Female = 1
	
class Student(object):
	def __init__(self, name, gender):
		self.name = name
		self.gender = gender

bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
	print('Test Pass')
else:
	print('Test Fail')

	

#元类	
#python中所有的对象（包括整数、字符串、函数和类等）都是从一个类中创建出来的
#str是用来创建字符串对象的类，int是用来创建整数对象的类。type就是创建类对象的类。
print('MetaClass')

#动态地创建类
#type函数可以动态地创建类
#type(类名, 父类的元组（针对继承的情况，可以为空），包含属性的字典（名称和值）)
print('Create classes dynamically')
MyClass = type('MyClass', (), {})	#类的父类是object，类的属性为空
print(MyClass)

def set_age(self, age):
	self.age = age
	return

def get_age(self):
	print('get_age:', self.age)
	return

#通过字典定义类的属性或方法
MySubClass = type('MySubClass', (MyClass,), {'age':12, 'set_age':set_age, 'get_age':get_age,})
print(MySubClass)
mysubclass = MySubClass()	#类需要创建实例才能调用方法
mysubclass.set_age(10)
mysubclass.get_age()




