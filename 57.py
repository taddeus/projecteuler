#!/usr/bin/env python
# https://en.wikipedia.org/wiki/Continued_fraction#Some_useful_theorems

def nom(n):
    h = hp = hpp = 1

    while n > 0:
        h = 2 * hp + hpp
        hpp = hp
        hp = h
        n -= 1

    return h

def denom(n):
    kpp = 0
    k = kp = 1

    while n > 0:
        k = 2 * kp + kpp
        kpp = kp
        kp = k
        n -= 1

    return k

def ndig(n, base=10):
    i = 1 if n == 0 else 0

    while n > 0:
        i += 1
        n /= base

    return i

count = 0

for n in xrange(1, 1001):
    if ndig(nom(n)) > ndig(denom(n)):
        count += 1

print count
