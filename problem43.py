#!/usr/bin/env python
from itertools import permutations

def div(d, m):
    return not (d[2] + d[1] * 10 + d[0] * 100) % m

s = 0

for d in permutations(range(10)):
    if div(d[1:4], 2) and div(d[2:5], 3) and div(d[3:6], 5) \
            and div(d[4:7], 7) and div(d[5:8], 11) and div(d[6:9], 13) \
            and div(d[7:10], 17):
        s += int(''.join(map(str, d)))

print s
