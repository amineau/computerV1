#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Computer v1
    42 Projet
    amineau <amineau@student.42.fr>
"""

import re

def __clear__(tab):
    while len(tab) > 0 and tab[len(tab) - 1] == 0:
        tab = tab[:-1]
    return tab

def __positive__(tab):
    if all(item <= 0 for item in tab):
        tab = [item * -1 for item in tab]
    return tab

def __merge__(monomials):
    a = monomials[0]
    b = monomials[1]
    size = len(a) if len(a) > len(b) else len(b)
    result = []
    for index in range(size):
        elem = 0.0
        if len(a) > index:
            elem = elem + a[index]
        if len(b) > index:
            elem = elem - b[index]
        result.append(elem)
    result = __clear__(result)
    result = __positive__(result)
    return result

def find(members):
    monomials = []
    for member in members:
        monomial = []
        rr = re.finditer('(\+|-|^)(?:(\d+(?:\.\d+)?)\*?)?(x(?:\^(\d+))?)?', member, re.IGNORECASE)
        for item in rr:
            match = item.groups()
            coef = float(match[0] + str(match[1] if match[1] else 1))
            index = (int(match[3]) if match[3] else 1) if match[2] else 0
            if coef <> 0:
                for n in range(len(monomial), index + 1):
                    monomial.append(0.0)
                monomial[index] = float(monomial[index]) + coef
        monomials.append(monomial)
    return __merge__(monomials)