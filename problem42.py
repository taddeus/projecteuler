words = open('words.txt', 'r').read()[1:-1].split('","')

def word_value(word):
    return sum([ord(c) - 96 for c in word.lower()])

values = [word_value(w) for w in words]
m = max(values)

triangle = [1]
v = n = 1

while v < m:
    n += 1
    v = n * (n + 1) / 2
    triangle.append(v)

count = 0

for v in values:
    if v in triangle:
        count += 1

print count
