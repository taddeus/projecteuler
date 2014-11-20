#!/usr/bin/env python
from copy import deepcopy

m = [map(int, line.split(',')) for line in open('matrix.txt', 'r').readlines()]
h, w = len(m), len(m[0])
orig = deepcopy(m)

def trypath(paths, *indices):
    try:
        paths.append(sum(orig[y][x] for x, y in indices))
    except IndexError:
        pass

for c in xrange(1, w):
    for r in xrange(h):
        paths = []
        trypath(paths, (c - 1, r - 1), (c, r - 1))
        trypath(paths, (c - 1, r))
        trypath(paths, (c - 1, r + 1), (c, r + 1))
        m[r][c] += min(paths)

print min(row[-1] for row in m)
