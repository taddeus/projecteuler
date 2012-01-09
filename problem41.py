#!/usr/bin/env python
def is_prime(n):
    if n == 2:
        return True

    if n < 2 or not n & 1:
        return False

    for i in xrange(3, int(n ** .5) + 1, 2):
        if not divmod(n, i)[1]:
            return False

    return True

if __name__ == '__main__':
    from itertools import permutations

    m = 0

    for i in xrange(2, 10):
        for digits in permutations(map(str, range(i, 0, -1))):
            n = int(''.join(digits))

            if n > m and is_prime(n):
                m = n

    print m
