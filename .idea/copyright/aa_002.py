#!/usr/bin/python
# -*- coding: UTF-8 -*-




def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: #not iterable
        return False

def add_and_maybe_multiply(a,b,c=None):
    result = a + b

    if c is not None:
        result += c
    return result

# print(add_and_maybe_multiply(5,6,))

sequence = [1,2,None,4,None,6]
total = 0
total0 = 0
for value in sequence:
    if value is None:
        continue
    total += value

print(total)

for value in sequence:
    if value == None:
        continue
    elif value == 4:
        break
    else:
        total0 += value

print(total0)

for i in range(4):
    for j in range(4):
        if j > i:
            break
        print((i,j))
# a = 4.5
# b = 2
#
# print('a is {0},b is {1}'.format(type(a),type(b)))
#
# c = a / b
#
# print(isinstance(c,int))
#
# a = 'foo'
#
# print(a.islower())
#
# print(isiterable(5))
#
# print(isiterable([1,2,3,4,5]))

