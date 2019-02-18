#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name,  ", Salary: ", self.salary

employee = Employee("ztm",8990);
employee1 = Employee("ds",990);
employee.displayEmployee();
employee.displayCount()
employee1.displayCount()
print "Total all Employee",Employee.empCount

##销魂对象

del employee
del employee1
