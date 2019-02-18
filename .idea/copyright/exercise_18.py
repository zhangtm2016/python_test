#!/usr/bin/python
# -*- coding: UTF-8 -*-

Tn = 0
Sn = []
n = int(raw_input('n = '))
a = int(raw_input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    print Tn
#用 lambda匿名函数 对集合内元素进行累计
Sn = reduce(lambda x,y : x + y,Sn)
print "计算和为：",Sn