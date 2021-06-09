#!/usr/bin/env python
# -*- coding: utf-8 -*-

class SingletonParent(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonParent, cls).__new__(cls)
        return cls.instance

class single(SingletonParent):
    def __init__(self, val1, val2):
        self.field1 = val1
        self.field2 = val2


def SingletonDecorator(cls):
    instance = None
    def get_instance(*args, **kwargs):
        nonlocal instance
        if instance is None:
            instance = cls(*args, **kwargs)
        else:
            instance.change(*args, **kwargs)
        return instance
    return get_instance

@SingletonDecorator
class single2:
    def __init__(self, x):
        self.x = x

    def change(self, x):
        self.x = x


if __name__ == '__main__':
    pro1 = single(2,2)
    pro2 = single(3,3)
    print(pro1.field2, pro2.field2)
    print(pro1==pro2)

    gg1 = single2(4)
    gg2 = single2(5)
    print(gg1.x, gg2.x)
    print(gg1 == gg2)