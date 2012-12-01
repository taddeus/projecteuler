#!/usr/bin/env python
from utils import nprimes

print reduce(lambda a, b: b, nprimes(10001))
