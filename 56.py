#!/usr/bin/env python
def digit_sum(n):
    s = 0

    while n > 0:
        s += n % 10
        n /= 10

    return s

m = 0

for a in xrange(100):
    for b in xrange(100):
        s = digit_sum(a ** b)
        if s > m:
            m = s

print m
