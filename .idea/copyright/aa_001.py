#!/usr/bin/python
# -*- coding: UTF-8 -*-
def my_abs(x):
    if x < 0:
        print('negative!')
        # pass
    elif x == 0:
        print("输入的数字正好是零")
    else:
        print("输入的是个正数")

def sum():
    sum = 0
    for i in range(100000):
        if i % 3 == 0 or i % 5 ==0:
            sum += i
    print(sum)



def nested_tup():
    nested_tup = (4, 5, 6), (7, 8),(9,3,4),(7,3,3)
    ac = 0
    for i in range(len(nested_tup)):
        for j in range(len(nested_tup[i])):
            print(nested_tup[i][j])
            ac += nested_tup[i][j]

    print("所有数据的值为",ac)


def func(a,b=4,c=5):
    print(a,b,c)



#print(nested_tup[0][1])

sum()
