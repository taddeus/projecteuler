#!/usr/bin/python
def digits(n):
    return set(list(str(n)))

x = 1

while True:
    found = True
    d = digits(x)

    for i in range(2, 7):
        if digits(i * x) != d:
            found = False

    if found:
        print x
        break

    x += 1
