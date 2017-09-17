#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Computer v1
    42 Projet
    amineau <amineau@student.42.fr>
"""

def discriminant(monomials):
    # d = b^2 - 4 a c
    a = monomials[2]
    b = monomials[1]
    c = monomials[0]
    result = b * b - 4 * a * c
    return result

def pgcd(a,b) :  
   while a%b != 0 : 
      a, b = b, a%b 
   return b

def abs(x):
    return x if x >= 0 else -x

def sqrt(x):
    last_guess = x/2.0
    while True:
        guess = (last_guess + x/last_guess)/2
        if abs(guess - last_guess) < .000001:
            return guess
        last_guess= guess

def fraction(num, div):
    if num.is_integer() and div.is_integer():
        denominator = pgcd(num, div)
        if denominator <> div:
            return "%s / %s"%(int(num/denominator),int(div/denominator))
    return str(convert_if_integer(num/div))

def convert_if_integer(number):
    return int(number) if number.is_integer() else number

def first_degree_solution(monomials):
    # x = -b / a
    a = monomials[1]
    b = monomials[0]
    x = fraction(b*-1, a)
    return (x,)

def second_degree_solution(monomials, discriminant):
    a = monomials[2]
    b = monomials[1]
    d = discriminant
    if d > 0:
        # x1 = -b - √d / 2a
        # x2 = -b + √d / 2a    
        x1 = fraction(- b - sqrt(d), 2 * a)
        x2 = fraction(- b + sqrt(d), 2 * a)
    elif d == 0:
        # x = -b / 2a    
        x = fraction(-b, 2 * a)
    else:
        # x1 = -b - i√-d / 2a
        # x2 = -b + i√-d / 2a
        x1 = "(%s-i√%s)/%s"%(b*-1, d*-1, 2 * a)
        x2 = "(%s+i√%s)/%s"%(b*-1, d*-1, 2 * a)
    return (x, ) if d == 0 else (x1, x2)

def zero_degree_solution(monomials):
    a = monomials[0]
    if a:
        return ("empty set", )
    return []