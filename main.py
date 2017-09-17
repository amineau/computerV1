#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    Computer v1
    42 Projet
    amineau <amineau@student.42.fr>
"""


import sys
import re
import monomial
import display
from math import *


def check_syntactic(members):
    if len(members) == 1:
        display.error("'=' statement is missing")
    elif len(members) > 2:
        display.error("Too many '=' statements")
    elif "" in members:
        display.error("At least one monomial is empty")
    for member in members:
        if re.match("^((\+|-|^|^-)((\d+(\.\d+)?)(\*?X(\^(\d+))?)?|((\d+(\.\d+)?)\*?)?X(\^(\d+))?))+$", member, re.IGNORECASE) is None:
            display.error("parse error")

def main():
    if len(sys.argv) <> 2:
        display.error('Bad number of arguments')
    members = sys.argv[1].replace(' ', '').split('=')
    check_syntactic(members)
    monomials = monomial.find(members)
    display.reduce_form(monomials)
    display.polynomial_degree(len(monomials) - 1)
    if len(monomials) >= 4:
            display.error("The polynomial degree is stricly greater than 2, I can't solve.")
    elif len(monomials) == 3:
        d = discriminant(monomials)
        display.discriminant(d)
        display.solutions(second_degree_solution(monomials, d))
    elif len(monomials) == 2:
        display.solutions(first_degree_solution(monomials))
    elif len(monomials) == 1:
        display.solutions(zero_degree_solution(monomials))
    else:
        display.solutions([])


if __name__ == '__main__':
        main()
