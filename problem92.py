#!/usr/bin/env python
def digits(n):
    return [n] if n < 10 else digits(n / 10) + [n % 10]

def quad(n):
    return n * n

def end(s):
    return s if s == 1 or s == 89 else end(sum(map(quad, digits(s))))

count = 0

for n in xrange(1, 10000000):
    if end(n) == 89:
        count += 1

print count
