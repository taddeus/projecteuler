#!/usr/bin/env python
from __future__ import division
from math import sqrt, ceil

def primes_until(n):
    """ Sieve of Eratosthenes """
    lst = [False] * n
    i = 2

    while i < n:
        if not lst[i]:
            yield i

            for j in xrange(i, n, i):
                lst[j] = True

        i += 1

def times(a, b):
    return a * b

def div(m, n):
    return not divmod(n, m)[1]

MAX = 2000000
all_primes = list(primes_until(MAX))

def primes(n):
    for p in all_primes:
        if p >= n:
            raise StopIteration

        yield p

def phi(n):
    return reduce(times, iter(1 - 1 / p for p in primes(n) if div(p, n)), n)

def resilience(d):
    return phi(d) / (d - 1)

d = 2

try:
    while resilience(d) >= 15499 / 94744:
        d += 1

        if d == MAX:
            print 'maximum reached:',
            break
except KeyboardInterrupt:
    print 'interrupted:',

print d
