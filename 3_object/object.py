#!/usr/bin/python3
# -*- coding: utf-8 -*-

#面向对象的程序设计思想，我们首选思考的不是程序的执行流程，
#而是这些数据类型应该被视为一个对象，这个对象拥有哪些属性（Property）。

#class定义一个类，类是一个抽象的概念，类的内部有属性和方法
#类名通常是大写开头的单词
class Student(object):

	#__init__方法定义初始化实例时要创建的属性
	#类的方法的第一个参数永远是self，表示创建的实例本身
	def __init__(self, name, score):
		self.__name = name	#属性名称前面加上两个下划线就变为私有属性，外部不能访问
		self.__score = score
	
	#自定义方法
	#类的方法的第一个参数永远是self，调用时不用传递该参数，其他与函数一致
	def get_name(self):
		return self.__name
		
	def get_score(self):
		return self.__score
		
	def set_score(self, score):
		if score >= 0 and score <=100:
			self.__score = score
			return True
		else:
			return False

	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
	
		
#通过类创建的变量就是实例
michael = Student('michael', 100)
lisa = Student('lisa', 98)
michael.set_score(99)

print(michael.get_name(), michael.get_score(), michael.get_grade())
print(lisa.get_name(), lisa.get_score(), lisa.get_grade())


