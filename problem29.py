#!/usr/bin/env python
print len(set(a ** b for b in range(2, 101) for a in range(2, 101)))
