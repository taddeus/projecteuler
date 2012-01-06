from numpy import array, zeros

#m = array([[131, 673, 234, 103, 18 ],
#           [201, 96 , 342, 965, 150],
#           [630, 803, 746, 422, 111],
#           [537, 699, 497, 121, 956],
#           [805, 732, 524, 37 , 331]])
f = open('matrix.txt', 'r')
m = array([map(int, l.split(',')) for l in f.readlines()])
f.close()

def add(x, y):
    global m

    h, w = m.shape
    if x == w or y == h: return

    p = []
    if x: p.append(m[y, x - 1])
    if y: p.append(m[y - 1, x])
    m[y, x] += min(p)

h, w = m.shape

for i in range(w+h):
    for x in range(i + 1):
        y = i - x
        if (x or y) and x < w and y < h:
            add(x, y)

print m[h - 1, w - 1]
