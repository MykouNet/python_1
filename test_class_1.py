#!/usr/bin/env python3

class my_class:
    def __init__(self, membre_1, membre_2):
        self.membre_1 = membre_1
        self.membre_2 = membre_2

    def add(self, x,y):
        return print(x+y)

    def subst(self, x,y):
        return print(x-y)

my_class_var = my_class(5,8)
my_class_var.add(5,8)
my_class_var.subst(8,5)
