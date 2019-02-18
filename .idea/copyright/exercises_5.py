#!/usr/bin/python
# -*- coding: UTF-8 -*-


x=int(raw_input('X:'))
y=int(raw_input('Y:'))
z=int(raw_input('Z:'))

#判断法
if (x >= y and y >= z ):
    print x,y,z
elif(x >= z and z >= y):
    print x,z,y
elif(y >= x and y >= z):
    print y,x,z
elif(y >= z and z >= x):
    print y,z,x
elif(z >= x and x >= y):
    print z,x,y
elif(z >= y and y >= x):
    print z,y,x

#重写sort







