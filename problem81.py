from numpy import array

m = array([l.split(',') for l in open('matrix.txt', 'r').readlines()],
          dtype=int)
h, w = m.shape

def add(x, y):
    global m

    p = []
    if x: p.append(m[y, x - 1])
    if y: p.append(m[y - 1, x])
    m[y, x] += min(p)

for i in range(w+h):
    for x in range(i + 1):
        y = i - x

        if (x or y) and x < w and y < h:
            add(x, y)

print m[h - 1, w - 1]
