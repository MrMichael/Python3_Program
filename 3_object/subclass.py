#!/usr/bin/python3
# -*- coding: utf-8 -*-

#当我们定义一个class的时候，可以从某个现有的class继承，
#新的class称为子类（Subclass），而被继承的class称为父类（Base class）
#其实所有的类都是从object这个父类继承

class Animal(object):
	def __init__(self, type):
		self.type = type
	
	def get_type(self):
		print('type is %s' % self.type)
	
	def run(self):
		print('Animal is running')
		
	def eat(self):
		print('Animal is eating')
		
#子类获得了父类的全部功能
class Dog(Animal):
	def watch(self):	#子类可以添加自己的属性和方法
		print('Dog is watching')
	def eat(self):	#当子类与父类存在相同的方法，子类方法会覆盖父类，即多态
		print('Dog is eating beef')	
	
mammal = Animal('mammal')
jim = Dog('dog')
jim.get_type()
jim.run()
jim.eat()
jim.watch()

def eat_food(animal):
	animal.eat()
	
eat_food(jim)
eat_food(mammal)	#多态的好处是可以根据不同实例对相同方法有不同处理

print('isinstance:', isinstance(jim, Dog)) #isinstance可以判断实例是否属于某类
print(dir(jim))	#dir函数可以获取对象的所有属性与方法






