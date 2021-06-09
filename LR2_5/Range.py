#!/usr/bin/env python
# -*- coding: utf-8 -*-


class myRange():
    def __init__(self, start, end, *args):
        self.arr = range(start, end, *args)

    def __iter__(self):
        return iter(self.arr)

    def __reversed__(self):
        return reversed(self.arr)

    def __contains__(self, value):
        for item in self.arr:
            if item == value:
                return True
        return False

    def __len__(self):
        return(len(self.arr))


def range(start, end, *args):
    arr = []
    i = start
    step = 1

    if len(args):
        if isinstance(args[0], int):
            step = args[0]

    while i < end:
        arr.append(i)
        i += step

    if step < 0:
        while i > end:
            arr.append(i)
            i += step

    if len(args):
        if callable(args[0]):
            arrres = []
            for item in arr:
                if args[0](item):
                    arrres.append(item)
            return arrres

    if len(args) == 2:
        if callable(args[1]):
            arrres = []
            for item in arr:
                if args[1](item):
                    arrres.append(item)
            return arrres

    return arr


"""
Filter functions
"""


def filterEvenNum(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False


def filterOddNum(in_num):
    if(in_num % 2) == 0:
        return False
    else:
        return True


def filterOnlyHighFive(in_num):
    if(in_num % 5) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    print(range(1, 6))
    print(range(6, 1, -1))
    print(range(1, 100))
    print(range(1, 6, 5))
    print(range(1, 2, 5))
    print(range(1, 10, 5, filterEvenNum))
    print(range(1, 10, filterEvenNum))
    print(range(1, 10, 5, filterOddNum))
    print(range(1, 10, filterOnlyHighFive))
    print(range(1, 100, filterOnlyHighFive))
    print(list(myRange(1, 6)))
    print(list(myRange(6, 1, -1)))
    R = myRange(1, 10, 5, filterEvenNum)
    print(6 in R)
    print(7 in R)
    R = myRange(10, 1, -1)
    for item in reversed(R):
        print (item)
