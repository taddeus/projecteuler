#!/usr/bin/env python
def concatprod(number, n):
    s = str(number)

    for i in xrange(2, n + 1):
        s += str(number * i)

    return s

def ispandig(s):
    return sorted(s) == map(None, '123456789')

m = ''

for number in xrange(192, 100000):
    n = c = 2

    while int(c) < 999999999:
        c = concatprod(number, n)
        n += 1

        if ispandig(c):
            m = c
            print number, n, c

print m
