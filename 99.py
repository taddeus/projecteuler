#!/usr/bin/env python3
from math import log


def comparable(index_line):
    base, exp = map(int, index_line[1].split(','))
    return exp * log(base)


print(max(enumerate(open('p099_base_exp.txt')), key=comparable)[0] + 1)
