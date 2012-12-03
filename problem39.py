#!/usr/bin/env python
from math import sqrt

def euclid(m, n):
    mq = m ** 2
    nq = n ** 2
    return mq - nq, 2 * m * n, mq + nq

def hist(maxp):
    hist = [set() for i in xrange(maxp+1)]

    for m in xrange(2, int(sqrt(maxp))):
        for n in xrange(1, m):
            a, b, c = oa, ob, oc = euclid(m, n)
            k = 1

            while True:
                p = a + b + c

                if p > maxp:
                    break

                hist[p].add(tuple(sorted((a, b))) + (c,))
                k += 1
                a += oa
                b += ob
                c += oc

    return hist

maxp = maxs = 0

for p, s in enumerate(hist(1000)):
    if len(s) >= maxs:
        maxp, maxs = p, len(s)

print maxp
