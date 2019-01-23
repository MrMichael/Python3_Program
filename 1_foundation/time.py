#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time;	#引入时间模块

#获取UTC时间
ticks = time.time()	
print('Current UTC', ticks, 's')


#获取当地时间		格林时间，元组格式
localtime = time.localtime()	
print('local time:', localtime)


#获取格式化的时间		当地时间转换为简单的可读时间模式
formattime = time.asctime(localtime) 
print('format time:', formattime)


#获取格式化日期			定制输出格式
formatdate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
print('format date:', formatdate)
formatdate2 = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
print('format date2:', formatdate2)


#获取某月日历
import calendar

cal = calendar.month(2019, 1)
print(cal)