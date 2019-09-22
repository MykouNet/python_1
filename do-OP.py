#!/usr/bin/env python3
#  python3 do-OP.py 45 / 3
# opération basique, arguments entrés en ligne de commande

import sys
x, op, y = sys.argv[1:4]

x = int(x)
y = int(y)


def add(x, y):
    return x + y

def subst(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    return x / y



functMapper = { '+' : add,
                '-' : subst,
                '*' : mult,
                '/' : div }

print(str(int(functMapper[op](x,y))))
