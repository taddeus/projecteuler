#!/usr/bin/env python
from itertools import permutations

def num(digits):
    return int(''.join(map(str, digits)))

N = 9
lens = [(mc, mp, N - mc - mp)
        for mc in range(1, N - 1)
        for mp in range(1, N - mc)]
mem = {}
s = 0

for seq in permutations(range(1, N + 1)):
    for mcl, mpl, prl in lens:
        mc = num(seq[:mcl])
        mp = num(seq[mcl:mcl + mpl])
        pr = num(seq[mcl + mpl:])

        if mc * mp == pr and pr not in mem:
            mem[pr] = 1
            s += pr

print s
