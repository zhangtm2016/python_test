#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 1.0
b = 1.0
z = 0.0
c = 0.0
d = 0

for i in range(1,21):

    d = d + ((a+b)/a)

    z = ((a+b)/a)

    c = a
    a = a+b
    b = c


print(d)
