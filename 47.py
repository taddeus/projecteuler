#!/usr/bin/env python
from __future__ import division
from utils import primes_until

primes = list(primes_until(10000))

def distinct(n, frm=0):
    for i, p in enumerate(primes[frm:]):
        div = n / p

        if div < 2:
            break

        if div.is_integer():
            others = set([int(div)]) if div in primes[i:] else distinct(div, i)

            if others:
                return others | set([p])

n = N = 4
counter = 0

while counter != N:
    factors = distinct(n)
    counter = counter + 1 if factors and len(factors) == N else 0
    n += 1

print n - N
