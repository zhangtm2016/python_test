#!/usr/bin/python
# -*- coding: UTF-8 -*-
def f(n):

    sum = 0
    if n == 0:
        sum = 1
    else:
        sum = n * f(n-1)
    return sum


print(f(5))

