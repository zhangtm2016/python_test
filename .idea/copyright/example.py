#!/usr/bin/python
# -*- coding: UTF-8 -*-

student = ['jack',18,'男','上海']
print("修改之前的列表为：",student)
student[3]='杭州'
print("修改之后的列表为：",student)
student.extend(student)
print(student)
