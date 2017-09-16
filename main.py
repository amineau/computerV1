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

def merge_terms(terms):
    result = [0] * 3
    for item in range(3):
        result[item] = terms[0][item] - terms[1][item]
    return result

def main():
    if len(sys.argv) <> 2:
        error('bar number of arguments')
    equation = sys.argv[1]
    terms = list()
    for part in equation.replace(' ', '').split('='):
        term = [0] * 3
        # re.match('([0-9]+(\.[0-9]+)?\*)([xX](\^[0-9]+))+') // regex à finir
        for x in list(filter(None, re.split('\+?(-?[0-9*\^xX]+)', part))):
            match = re.search('(-?[0-9\.]+)?\*?[Xx]\^?([0-9]+)?', x)
            if match:
                index = int(match.groups(1)[1])
                if index not in range(3):
                    error(index + ' is not a valid polynomial degree')
                term[index] = float(term[index]) + float(match.groups(1)[0])
            else:
                print("0, ya pas")
        terms.append(term)


    print(merge_terms(terms))

if __name__ == '__main__':
        main()

