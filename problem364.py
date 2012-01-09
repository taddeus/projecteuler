#!/usr/bin/env python
from copy import copy
from sys import argv, exit, setrecursionlimit

setrecursionlimit(10000000)

def T(N, seats=None):
    if not seats:
        seats = [False] * N
    elif all(seats):
        return 1

    t = 0
    seated = False

    # 1. If there is any seat whose adjacent seat(s) are not occupied, take
    # such a seat
    for i, taken in enumerate(seats):
        if not taken and (not i or not seats[i - 1]) \
                and (i == N - 1 or not seats[i + 1]):
            new_seats = copy(seats)
            new_seats[i] = True
            t += T(N, new_seats)
            seated = True

    # 2. If there is no such seat and there is any seat for which only one
    # adjacent seat is occupied take such a seat
    if not seated:
        for i, taken in enumerate(seats):
            if not taken and ((not i and seats[1]) \
                              or (i == N - 1 and seats[N - 2])
                              or (seats[i - 1] ^ seats[i + 1])):
                new_seats = copy(seats)
                new_seats[i] = True
                t += T(N, new_seats)
                seated = True

    # 3.Otherwise take one of the remaining available seats
    if not seated:
        for i, taken in enumerate(seats):
            if not taken:
                new_seats = copy(seats)
                new_seats[i] = True
                t += T(N, new_seats)

    del seats

    return t

if len(argv) < 2:
    print 'Usage: python %s N' % argv[0]
    exit(1)

print T(int(argv[1])) % 100000007
