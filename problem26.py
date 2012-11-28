#!/usr/bin/env python
from decimal import getcontext, Decimal

def findrec(d):
    getcontext().prec = d * 3
    dec = str(Decimal(1) / d)[2:]

    for l in xrange(d - 1, 0, -1):
        for offset in xrange(d):
            pivot = len(dec) - offset - l
            left = dec[pivot - l:pivot]
            right = dec[pivot:pivot + l]

            if left == right:
                if len(left) == 1 or len(set(left)) > 2:
                    return dec[pivot - l:pivot]

if __name__ == '__main__':
    longest = 0
    ld = None

    for d in xrange(2, 1000):
        rec = findrec(d)

        if rec and len(rec) > longest:
            longest, ld = len(rec), d
            print '%d (%d)' % (d, longest), rec
