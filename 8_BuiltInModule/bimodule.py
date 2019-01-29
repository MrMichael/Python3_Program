#!/usr/bin/python3
# -*- coding: utf-8 -*-

#获取当前日期和时间	datetime
from datetime import datetime
now = datetime.now()
print(now)
#指定某个日期和时间
dt = datetime(2019,1,29,12,20)
print(dt)
#datetime转换为timestamp
#	timestamp是相对于epoch time（1970年1月1日 00:00:00 UTC+00:00时区）的秒数
tstamp = now.timestamp()
print(tstamp)
#timestamp转换为datetime
dt = datetime.fromtimestamp(tstamp)
print(dt)
#datetime加减
from datetime import datetime, timedelta
now = now + timedelta(hours=8)
print(now)
now = now - timedelta(days=2,hours=8)
print(now)



#集合模块collections，提供了许多有用的集合类。
#namedtuple	用来创建一个自定义的tuple对象，并且规定了tuple元素的个数
from collections import namedtuple
Point = namedtuple('Point', ['x','y'])
























