from decimal import Decimal as D
import re

for i in range(2, 11):
    r = str(round(1. / i, 1000))[2:-1]

    for l in range(len(r) / 2, 0, -1):
        pass

    print i, r
