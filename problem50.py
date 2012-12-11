#!/usr/bin/env python
from utils import primes_until

def maxprime(n):
    primes = list(primes_until(n))
    maxp = maxlen = 2

    for start in xrange(len(primes)):
        for end in xrange(start + maxlen + 1, start + 800):
            if end - start < maxlen:
                break

            conseq = primes[start:end]
            s = sum(conseq)

            if s >= 1000000:
                break

            if s in primes[start + maxlen:]:
                maxlen = end - start
                maxp = s

    return maxp

print maxprime(1000000)
