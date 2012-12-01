#!/usr/bin/env python
from utils import primes_until

MAX = 10000
comps = [False] * MAX
comps[1] = True

for p in primes_until(MAX - 1):
    q = 1
    comps[p] = True

    while True:
        pplusq = p + 2 * q ** 2

        if pplusq >= MAX:
            break

        comps[pplusq] = True
        q += 1

for i, passed in enumerate(comps):
    if i & 1 and not passed:
        print i
        break
