#!/usr/bin/env python
m = [map(int, line.split(',')) for line in open('matrix.txt', 'r').readlines()]
h, w = len(m), len(m[0])

def add(x, y):
    global m
    p = []
    if x: p.append(m[y][x - 1])
    if y: p.append(m[y - 1][x])
    m[y][x] += min(p)

for i in xrange(w + h):
    for x in xrange(i + 1):
        y = i - x

        if (x or y) and x < w and y < h:
            add(x, y)

print m[h - 1][w - 1]
