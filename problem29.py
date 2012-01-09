#!/usr/bin/env python
def combos(A, B):
    c = set()

    for a in A:
        for b in B:
            c.add(a ** b)

    return sorted(c)

print len(combos(range(2, 101), range(2, 101)))
