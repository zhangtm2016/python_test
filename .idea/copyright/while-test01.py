#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time;

count = 0
while  ( count < 9 ):
    print 'the count is ',count
    count = count + 1



numbers = [23,33,45,22,56,43,44,67,88]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if(number % 2 == 0 ):
        even.append(number)
    else:
        odd.append(number)

while len(even) > 0:
    eve = even.pop()
    print 'even is ',eve

while len(odd) > 0:
    od = odd.pop()
    print 'odd is ',od

for letter in 'python':
    if letter == 'o':
        pass
        print 'pass'
    print '当前字母 :', letter

ticks = time.time()
print '当前时间为:',ticks
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

str = raw_input("请输入：")
print "你输入的内容是: ", str

