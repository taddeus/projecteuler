#!/usr/bin/env python
from __future__ import division
from itertools import combinations, permutations
from utils import gcd

nrs = [(i, str(i)) for i in xrange(10, 100)]
pairs = ((0, 0), (0, 1), (1, 0), (1, 1))

pn = pd = 1

for (n, ns), (d, ds) in combinations(nrs, 2):
    if n < d:
        for i, j in pairs:
            if ds[1 - j] != '0' and ns[i] == ds[j] \
                    and int(ns[1 - i]) / int(ds[1 - j]) == n / d \
                    and ns[1] != '0':
                pn *= n
                pd *= d
                print '%d / %d == %s / %s' % (n, d, ns[1 - i], ds[1 - j])

g = gcd(pn, pd)
print 'product: %d / %d' % (pn/ g, pd / g)
print 'answer: %d' % (pd / g)
