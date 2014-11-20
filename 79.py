#!/usr/bin/env python
codes = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710,
         629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290,
         719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362,
         319, 760, 316, 729, 380, 319, 728, 716]
codes = map(str, codes)

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

passcode = []

def genpass():
    return ''.join(c for i, c in passcode)

for c, code in enumerate(codes):
    for d in code:
        if d in :
            pass
        else:
            a
