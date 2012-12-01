#!/usr/bin/env python
from math import sqrt
from sys import exit

def P(n):
    return n * (3 * n - 1) / 2

def is_pent(n):
    return ((1 + sqrt(24 * n + 1)) / 6.).is_integer()

for k in xrange(2, 10000):
    Pk = P(k)

    for j in range(k - 1, 0, -1):
        Pj = P(j)
        D = Pk - Pj

        if is_pent(D) and is_pent(Pk + Pj):
            print D
            exit()
