#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse


def checkPositive(value):
    value = int(value)
    if value < 0:
        raise argparse.ArgumentTypeError(f'The {value} is invalid(not positive or zero)')
    return value


def fibonacci(n: int) -> int:
    '''Finding the n number of Fibonacci'''
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for x in range(1, n):
        temp = b
        b = a + b
        a = temp
    return b


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="calculate the n's fibonacci number")
    parser.add_argument("-n", "--number", help="display the fibonacci number", type=checkPositive)
    args = parser.parse_args()

    if(not(args.number is None)):
        a = args.number
    else:
        a = input('Enter a positive integer ')
        if a.isdigit():
            a = int(a)
        else:
            exit('Incorrect input')

    print(f"The {a}'s is {fibonacci(a)}")
