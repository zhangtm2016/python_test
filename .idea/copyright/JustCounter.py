#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
##__private_method：两个下划线开头，声明该方法为私有方法，不能在类的外部调用。在类的内部调用
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0    # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter._JustCounter__secretCount  # 报错，实例不能访问私有变量

print(re.match('^www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配