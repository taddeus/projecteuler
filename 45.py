#!/usr/bin/env python
def tri(n): return n * (n + 1) / 2
def pent(n): return n * (3 * n - 1) / 2
def hexa(n): return n * (2 * n - 1)
funcs = (tri, pent, hexa)
init = 20
n = [init] * len(funcs)
vals = [f(init) for f in funcs]

while len(set(vals)) > 1 or vals[0] == 40755:
    mini = 0
    minv = None

    for i, v in enumerate(vals):
        if minv is None or v < minv:
            mini = i
            minv = v

    n[mini] += 1
    vals[mini] = funcs[mini](n[mini])

print vals[0]
