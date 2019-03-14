#!/usr/bin/env python3

import math
import operator
operators = {'+'  : operator.add,
             '-'  : operator.sub,
             '*'  : operator.mul,
             '/'  : operator.truediv,
             '^'  : operator.pow,
             '//' : operator.floordiv
        }

def is_numeric(text):
    try:
        float(text)
        return True
    except ValueError:
        return False

def calculate(arg):
    calc_stack = []
    for token in arg.split(' '):
        if is_numeric(token):
            calc_stack.append(float(token))
        else:
            a = calc_stack.pop()
            b = calc_stack.pop()
            return operators[token](a, b)

def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ == '__main__':
    main()
