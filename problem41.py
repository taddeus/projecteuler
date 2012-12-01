#!/usr/bin/env python
from itertools import permutations
from utils import is_prime

m = 0

for i in xrange(2, 10):
    for digits in permutations(map(str, range(i, 0, -1))):
        n = int(''.join(digits))

        if n > m and is_prime(n):
            m = n

print m
