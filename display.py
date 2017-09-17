#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Computer v1
    42 Projet
    amineau <amineau@student.42.fr>
"""

from math import convert_if_integer
import sys

def error(str):
    print(str)
    sys.exit(-1)

def reduce_form(monomials):
    tab = []
    for index, elem in reversed(list(enumerate(monomials))):
        if elem:
            sign = '-' if elem < 0 else '+'
            if len(tab) or sign == '-':
                tab.append(sign)
            if abs(elem) <> 1 or index == 0:
                tab.append(str(convert_if_integer(abs(elem))))
                if index:
                    tab.append('*')
            if index:
                x = 'X'
                x += '^%d'%(index) if index > 1 else ''
                tab.append(x)
    print("Reduced form: " + ' '.join(tab) + " = 0")

def polynomial_degree(degree):
    if degree >= 0:
        print("Polynomial degree: %d"%(degree))

def discriminant(discriminant):
    print("Discriminant: %d"%(discriminant))

def solutions(solutions):
    if len(solutions) == 2:
        print("x1: %s"%(solutions[0]))
        print("x2: %s"%(solutions[1]))
    elif len(solutions) == 1:
        print("x: %s"%(solutions[0]))
    else:
        print("x is a real")