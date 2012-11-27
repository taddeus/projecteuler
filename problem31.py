#!/usr/bin/env python
def pos(amt, coins):
    p = 0

    for i, c in enumerate(coins):
        if c == amt:
            p += 1
        elif c < amt:
            p += pos(amt - c, coins[i:])

    return p

print pos(200, [1, 2, 5, 10, 20, 50, 100, 200])
