#!/usr/bin/env python
def multdigits(D):
    answer = n = 1
    start = 0
    d = D.pop(0) - 1

    while True:
        ns = str(n)
        end = start + len(ns)

        while start <= d < end:
            answer *= int(ns[d - start])

            if not len(D):
                return answer

            d = D.pop(0) - 1

        start = end
        n += 1

    return answer

print multdigits([10 ** e for e in range(7)])
