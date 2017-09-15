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

def main():
    if len(sys.argv) <> 2:
        error('bar number of arguments')
    equation = sys.argv[1]
    terms = list()
    for part in equation.replace(' ', '').split('='):
        term = list(filter(None, re.split('\+?(-?[0-9*\^xX]+)', part)))
        for x in term:
            match = re.search('[Xx](\^[0-9]+)?', x)
            if match:
                help(match)
                print(match.group(0))
        terms.append(term)

    # print(terms)
    # print(equation)

if __name__ == '__main__':
        main()

