#!/usr/bin/env python
from itertools import permutations, combinations
from utils import primes_until, digits, add
from sys import exit

def concat(digits):
    return int(reduce(add, digits))

def suited(n):
    return n > 999 and n not in (1487, 4817, 8147) and n in primes

primes = [p for p in primes_until(10000) if p > 999]

for p in primes:
    perm = map(concat, permutations(str(p)))

    for a, b, c in set(combinations(perm, 3)):
        if a >= b or a >= c or b >= c \
                or b - a != c - b or b - a < 1000 \
                or not all(map(suited, (a, b, c))):
            continue

        print '%d%d%d' % (a, b, c)
        exit()
