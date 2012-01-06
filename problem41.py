from math import sqrt, ceil
from itertools import permutations

def is_prime(n):
    if n == 2:
        return True

    if not n % 2:
        return False

    for i in xrange(3, int(ceil(sqrt(n))) + 1 + 1, 2):
        if not divmod(n, i)[1]:
            return False

    return True

m = 0

for i in xrange(2, 10):
    for digits in permutations(map(str, range(i, 0, -1))):
        n = int(''.join(digits))

        if n > m and is_prime(n):
            m = n

print m
