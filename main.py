#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Computer v1
    42 Projet
    amineau <amineau@student.42.fr>
"""


import sys
import re

def error(str):
    print(str)
    sys.exit(-1)

def print_reduce_form(terms):
    None

def clear(tab):
    while len(tab) > 0 and tab[len(tab) - 1] == 0:
        tab = tab[:-1]
    return tab

def merge_terms(terms):
    a = terms[0]
    b = terms[1]
    size = len(a) if len(a) > len(b) else len(b)
    result = []
    for index in range(size):
        elem = 0.0
        if len(a) > index:
            elem = elem + a[index]
        if len(b) > index:
            elem = elem - b[index]
        result.append(elem)
    result = clear(result)
    print(a, b, result)
    return result
    
def discriminant(terms):
    # b^2 - 4 a c
    a = terms[2]
    b = terms[1]
    c = terms[0]
    result = b * b - 4 * a * c
    return result

def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b

def fraction(num, div):
    print(num, type(num))
    print(div, type(div))
    if num.is_integer() and div.is_integer():
        denominator = pgcd(num, div)
        if denominator <> div:
            return "%s / %s"%(int(num/denominator),int(div/denominator))
    return str(convert_if_integer(num/div))

def convert_if_integer(number):
    return int(number) if number.is_integer() else number

def first_degree_soluce(terms):
    a = terms[1]
    b = terms[0]
    x = fraction(b*-1, a)
    return {
        "polynomial": 1,
        "soluce": x 
    }

def second_degree_soluce(terms):
    a = terms[2]
    b = terms[1]
    d = discriminant(terms)
    if d > 0:
        x1 = fraction(- b - sqrt(d), 2 * a)
        x2 = fraction(- b + sqrt(d), 2 * a)
    elif d == 0:
        x = fraction(b, 2 * a)
    else:
        x1 = "(%s-i√%s)/%s"%(b*-1, d*-1, 2 * a)
        x2 = "(%s+i√%s)/%s"%(b*-1, d*-1, 2 * a)
    return {
        "polynomial": 2,
        "discriminant": convert_if_integer(d),
        "soluces": (x, ) if d == 0 else (x1, x2),
    }

def abs(x):
    return x if x >= 0 else -x

def sqrt(x):
    last_guess = x/2.0
    while True:
        guess = (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .000001:
            return guess
        last_guess= guess


def main():
    if len(sys.argv) <> 2:
        error('bar number of arguments')
    equation = sys.argv[1]
    terms = list()
    for part in equation.replace(' ', '').split('='):
        term = []
        # rr = re.search('x(?:\^(\d+))?', part)
        rr = re.finditer('(\+|-|^)(?:(\d+(?:\.\d+)?)\*?)?(x(?:\^(\d+))?)?', part)
        # print(rr)
        for item in rr:
            match = item.groups()
            coef = float(match[0] + match[1] if match[1] else 1)
            index = (int(match[3]) if match[3] else 1) if match[2] else 0
            if coef <> 0:
                for n in range(len(term), index + 1):
                    term.append(0.0)
                print(term)
                term[index] = float(term[index]) + coef
        terms.append(term)

    terms = merge_terms(terms)
    if len(terms) >= 4:
        error("The polynomial degree is stricly greater than 2, I can't solve.")
    elif len(terms) == 3:
        print(second_degree_soluce(terms))
    elif len(terms) == 2:
        print(first_degree_soluce(terms))
    else:
        print("petit malin")


if __name__ == '__main__':
        main()

