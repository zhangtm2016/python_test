#!/usr/bin/python
# -*- coding: UTF-8 -*-

s = 0

for i in range(1,21):

    d = 1

    for j in range(1,i+1):
        d *= j

    s += d


print s
