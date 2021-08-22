#!/usr/bin/env python3
from functools import lru_cache


@lru_cache(maxsize=None)
def pos(amt, coins):
    p = 0
    for i, c in enumerate(coins):
        if c == amt:
            p += 1
        elif c < amt:
            p += pos(amt - c, coins[i:])
    return p


def ways(n):
    return pos(n, tuple(range(n - 1, 0, -1)))


assert ways(5) == 6
assert ways(50) == 204225
print(ways(100))
