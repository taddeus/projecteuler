#!/usr/bin/env python
from math import gamma, factorial

def S(p):
    return sum(factorial(p - k) for k in range(1, 6)) % p

def modfac(, p)

facs = [factorial(p) for p in range(5)]
total = s = S(5)
pmin6fac = 0
pmin1fac = factorial(5)
print 5, S(5)

N = 100
facs = [factorial(p) % p for p in range(5)]

for p in xrange(6, 1000000):
    s = s - pmin6fac + pmin1fac
    total += s % p
    if s: print p, s % p
    pmin6fac *= p - 5
    pmin1fac *= p

print total
