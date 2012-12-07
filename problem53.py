#!/usr/bin/python
from math import ceil

prev = [1, 2]
s = 0

for n in range(2, 100):
    cur = [1]
    half = int(ceil(n / 2.))

    for r in range(1, half + 1):
        cur.append(prev[r - 1] + prev[r])

        if cur[-1] > 1000000:
            s += 2 if not n & 1 or r != half else 1

    if not n & 1:
        cur.append(cur[-1])

    prev = cur

print s
