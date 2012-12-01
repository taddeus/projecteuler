def add(a, b):
    return a + b

def digits(n):
    return [n] if n < 10 else digits(n / 10) + [n % 10]

def _gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def gcd(*args):
    return reduce(_gcd, args)

def is_prime(n):
    if n == 2:
        return True

    if n < 2 or not n & 1:
        return False

    for i in xrange(3, int(n ** .5) + 1, 2):
        if not n % i:
            return False

    return True

def primes_until(n):
    """ Sieve of Eratosthenes """
    lst = [False] * n
    i = 2

    while i < n:
        if not lst[i]:
            yield i

            for j in xrange(i, n, i):
                lst[j] = True

        i += 1

def nprimes(n):
    a = 2

    while n:
        if is_prime(a):
            yield a
            n -= 1

        a += 1
