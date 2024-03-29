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
   while a % b != 0:
      a, b = b, a % b
   return b

def abs(x):
    return x if x >= 0 else -x

def sqrt(x):

    last_guess = x / 2.0
    while True:
        guess = (last_guess + x / last_guess) / 2
        if abs(guess - last_guess) < 0.000001:
            return guess
        last_guess= guess

def sqrt_facto(n):
    # √a => b√c or sqrt(a)
	root = sqrt(n)
	if root.is_integer():
		return (int(root))
	root = int(root)
	while n % (root * root):
		root -= 1
	return [root, int(n / (root * root))]

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

def factorisation(b, d, a):
    root = sqrt_facto(d)
    coef = 1
    if type(root) == list:
        coef = reduce(pgcd, (root[0], b, 2*a) if b else (root[0], 2*a))
        factor = str(root[0] / coef) if root[0] / coef <> 1 else ""
        root = factor + u"√" + str(root[1])
    else:
        coef = reduce(pgcd, (root, b, 2*a) if b else (root, 2*a))
        root = convert_if_integer(abs(root / coef))
    num = convert_if_integer(b * -1 / coef)
    div = convert_if_integer(2 * a / coef)
    return (num, root, div)

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
        res = factorisation(b, -d, a)
        x1 = u" * %s"%(res[1]) if res[1] <> 1 else "" 
        x2 = u" * %s"%(res[1]) if res[1] <> 1 else "" 
        if res[0]:
            x1 = u"%s - i%s"%(res[0], x1)
            x2 = u"%s + i%s"%(res[0], x2)
        else:
            x1 = u"-i%s"%(x1)
            x2 = u"i%s"%(x2)
        if res[2] <> 1:
            x1 = u"( %s ) / %s"%(x1, res[2])
            x2 = u"( %s ) / %s"%(x2, res[2])
    return (x, ) if d == 0 else (x1, x2)

def zero_degree_solution(monomials):
    a = monomials[0]
    if a:
        return ("empty set", )
    return []