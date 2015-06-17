#!/usr/bin/env python
def pos(amt, coins):
    p = 0

    for i, c in enumerate(coins):
        if c == amt:
            p += 1
        elif c < amt:
            p += pos(amt - c, coins[i:])

    return p

print pos(200, [200, 100, 50, 20, 10, 5, 2, 1])
