#!/usr/bin/env python
from itertools import permutations

codes = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710,
         629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290,
         719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362,
         319, 760, 316, 729, 380, 319, 728, 716]

def indices(partial):
    ind = []
    start = 0

    for c in partial:
        index = passcode[start:].find(c)

        if index == -1:
            return []

        ind.append(index + start)
        start = index + 1

    return ind

def match(code):
    partials = (code, code[1:], code[:2], code[::2], code[0], code[1], code[2])

    for i, partial in enumerate(partials):
        ind = indices(partial)

        if ind:
            return partial, i, ind

    return None, None, None

#codes.sort()
codes = map(str, set(codes))
passcode = codes.pop(0)
print passcode

while len(codes):
    possibilities = [(0, -1, [])]

    for index, code in enumerate(codes):
        partial, i, ind = match(code)

        if ind:
            #print code, partial, ind
            possibilities.append((index, i, ind, partial))

    possibilities.sort(lambda a, b: cmp(len(a[2]), len(b[2])))
    #print possibilities
    index, i, ind, partial = possibilities[-1]
    code = codes.pop(index)

    if i == 1:
        passcode = code[0] + passcode
    elif i == 2:
        passcode += code[2]
    elif i == 3:
        passcode = passcode[:ind[0]] + code[1] + passcode[ind[0]:]
    elif i == 4:
        passcode += code[1:]
    elif i == 5:
        passcode = code[0] + passcode + code[2]
    elif i == 6:
        passcode = code[:2] + passcode
    elif i == -1:
        passcode += code

    print code, partial, passcode

    #print len(passcode), len(codes) * 3, passcode
    #print passcode
