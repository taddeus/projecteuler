def _gcd(a, b):
    while b:
        a, b = b, a % b

    return a

def gcd(*args):
    return reduce(_gcd, args)
