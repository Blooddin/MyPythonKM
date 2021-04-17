#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse


def checkPositive(value):
    value = int(value)
    if value <= 0:
        raise argparse.ArgumentTypeError(f'The {value} is invalid(not positive)')
    return value


def fibonacci(n: int) -> int:
    '''Finding the n number of Fibonacci'''
    if n == 1:
        return 0
    if n == 2:
        return 1
    a = 0
    b = 1
    for x in range(2, n):
        temp = b
        b = a + b
        a = temp
    return b


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="calculate the n's fibonacci number")
    parser.add_argument("-n", "--number", help="display the fibonacci number", type=checkPositive)
    args = parser.parse_args()

    if(args.number):
        a = args.number
    else:
        a = input('Enter a positive integer ')
        if a.isdigit() and a != '0':
            a = int(a)
        else:
            sys.exit('Incorrect input')

    print(f"The {a}'s is {fibonacci(a)}")
