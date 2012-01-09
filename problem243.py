#!/usr/bin/env python
def is_resilient(n, d):
    if n == 1:
        return True

    for div in xrange(2, min(n, d) + 1):
        if not n % div and not d % div:
            return False

    return True

def resilience(d):
    r = 0

    for n in xrange(1, d):
        if is_resilient(n, d):
            r += 1

    return r / (d - 1.)

smallest = 15499. / 94744
d = 2

while True:
    if resilience(d) < smallest:
        print d
        break

    d += 1
