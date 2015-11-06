#!/usr/bin/env python

def rev(n):
    r = 0
    base = 1

    while n > 0:
        div, rem = divmod(n, 10)
        r = r * 10 + rem
        base *= 10
        n = div

    return r

def is_lychrel(n):
    niter = 0

    while niter < 50:
        n += rev(n)

        if rev(n) == n:
            return False

        niter += 1

    return True

print sum(int(is_lychrel(n)) for n in xrange(1, 10000))
