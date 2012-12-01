#!/usr/bin/env python
from math import factorial

def digits(n):
    return map(int, str(n))

def facsum(n):
    return sum(facs[d] for d in digits(n))

facs = map(factorial, range(10))
s = 0

for n in xrange(10, 99999):
    if n == facsum(n):
        s += n

print s
