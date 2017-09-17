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

def print_reduce_form(monomials):
    tab = []
    print(monomials)
    for index, elem in reversed(list(enumerate(monomials))):
        if elem:
            sign = '-' if elem < 0 else '+'
            if len(tab) or sign == '-':
                tab.append(sign)
            if abs(elem) <> 1:
                tab.append(str(convert_if_integer(abs(elem))))
                if index:
                    tab.append('*') 
            if index:
                x = 'X'
                x += '^%d'%(index) if index > 1 else ''
                tab.append(x)
    print("Reduced form: " + ' '.join(tab) + " = 0")

def print_polynomial_degree(degree):
    print("Polynomial degree: %d"%(degree))

def print_discriminant(discriminant):
    print("Discriminant: %d"%(discriminant))

def print_solutions(solutions):
    if len(solutions) == 2:
        print("x1: %s"%(solutions[0]))
        print("x2: %s"%(solutions[1]))
    elif len(solutions) == 1:
        print("x: %s"%(solutions[0]))
    else:
        print("x is a real")

def clear(tab):
    while len(tab) > 0 and tab[len(tab) - 1] == 0:
        tab = tab[:-1]
    return tab

def positive(tab):
    if all(item <= 0 for item in tab):
        tab = [item * -1 for item in tab]
    return tab

def merge_monomials(monomials):
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
    result = clear(result)
    result = positive(result)
    return result
    
def discriminant(monomials):
    # b^2 - 4 a c
    a = monomials[2]
    b = monomials[1]
    c = monomials[0]
    result = b * b - 4 * a * c
    return result

def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b

def fraction(num, div):
    if num.is_integer() and div.is_integer():
        denominator = pgcd(num, div)
        if denominator <> div:
            return "%s / %s"%(int(num/denominator),int(div/denominator))
    return str(convert_if_integer(num/div))

def convert_if_integer(number):
    return int(number) if number.is_integer() else number

def first_degree_solution(monomials):
    a = monomials[1]
    b = monomials[0]
    x = fraction(b*-1, a)
    return x

def second_degree_solution(monomials, discriminant):
    a = monomials[2]
    b = monomials[1]
    d = discriminant
    if d > 0:
        x1 = fraction(- b - sqrt(d), 2 * a)
        x2 = fraction(- b + sqrt(d), 2 * a)
    elif d == 0:
        x = fraction(b, 2 * a)
    else:
        x1 = "(%s-i√%s)/%s"%(b*-1, d*-1, 2 * a)
        x2 = "(%s+i√%s)/%s"%(b*-1, d*-1, 2 * a)
    return (x, ) if d == 0 else (x1, x2)

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
    print(sys.argv)
    if len(sys.argv) <> 2:
        error('Bad number of arguments')
    equation = sys.argv[1]
    monomials = list()
    members = equation.replace(' ', '').split('=')
    if len(members) == 1:
        error("'=' statement is missing")
    elif len(members) > 2:
        error("Too many '=' statements")
    elif "" in members:
        error("At least one monomial is empty")
    for member in members:
        monomial = []
        # rr = re.search('x(?:\^(\d+))?', member)
        rr = re.finditer('(\+|-|^)(?:(\d+(?:\.\d+)?)\*?)?(x(?:\^(\d+))?)?', member, re.IGNORECASE)
    
        for item in rr:
            match = item.groups()
            coef = float(match[0] + match[1] if match[1] else 1)
            index = (int(match[3]) if match[3] else 1) if match[2] else 0
            if coef <> 0:
                for n in range(len(monomial), index + 1):
                    monomial.append(0.0)
                monomial[index] = float(monomial[index]) + coef
        monomials.append(monomial)

    monomials = merge_monomials(monomials)
    print_reduce_form(monomials)
    print_polynomial_degree(len(monomials) - 1)
    if len(monomials) >= 4:
        error("The polynomial degree is stricly greater than 2, I can't solve.")
    elif len(monomials) == 3:
        d = discriminant(monomials)
        print_discriminant(d)
        print_solutions(second_degree_solution(monomials, d))
    elif len(monomials) == 2:
        print_solutions(first_degree_solution(monomials))
    else:
        print("petit malin")


if __name__ == '__main__':
        main()

