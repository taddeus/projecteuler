#!/usr/bin/env python
# https://en.wikipedia.org/wiki/Continued_fraction#Some_useful_theorems

def nom(n):
    nexth = hp = hpp = 1

    while n > 0:
        nexth = 2 * hp + hpp
        hpp = hp
        hp = nexth
        n -= 1

    return nexth

def denom(n):
    kpp = 0
    nextk = kp = 1

    while n > 0:
        nextk = 2 * kp + kpp
        kpp = kp
        kp = nextk
        n -= 1

    return nextk

def ndig(n, base=10):
    i = 0

    while n > 0:
        i += 1
        n /= base

    return i

count = 0

for n in xrange(1, 1001):
    if ndig(nom(n)) > ndig(denom(n)):
        count += 1

print count
