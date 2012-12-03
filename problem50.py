#!/usr/bin/env python
from math import sqrt
from utils import primes_until

def maxprime(n):
    primes = list(primes_until(n))
    maxp = maxlen = 2

    for start in xrange(len(primes)):
        for end in xrange(start + maxlen + 1, start + 800):
            if end - start >= maxlen:
                conseq = primes[start:end]
                s = sum(conseq)

                if len(conseq) > 1 and s in primes[start:]:
                    maxlen = end - start
                    maxp = s
                    print maxp
                    #print '%s = %d' % (' + '.join(map(str, primes[start:end])), s)

    return maxp

print maxprime(1000000)
