#!/usr/bin/env python
# -*- coding: utf-8 -*-


# KeyError


class defaultdict(dict):
    def __getitem__(self, item):
        try:
            val = dict.__getitem__(self, item)
            return val
        except KeyError:
            def_val = defaultdict()
            dict.__setitem__(self, item, def_val)
            return def_val


if __name__ == '__main__':
    d = defaultdict()
    d['a']['b']['c'] = 23
    d['d']['b']['c'] = 23
    print(d['a']['b']['c'])
    print(str(d))
