#!/usr/bin/env python
from __future__ import division
from utils import is_prime, nprimes

print list(nprimes(15499))
import sys; sys.exit()

def times(a, b):
    return a * b

known_primes = {}

def primes(n):
    for p in range(2, n):
        if p in known_primes:
            yield p
        elif is_prime(p):
            known_primes[p] = None
            yield p

def phi(n):
    return reduce(times, iter(1 - 1 / p for p in primes(n) if not n % p), n)

def resilience(d):
    return phi(d) / (d - 1)

d = 30

while True:
    print d,

    res = resilience(d)

    if res < 15499 / 94744:
        break

    print res, 15499 / 94744
    d += 30
