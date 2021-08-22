#!/usr/bin/env python3
import sys
from itertools import combinations_with_replacement, permutations
from string import ascii_lowercase

with open('p059_cipher.txt') as f:
    ciphertext = list(map(int, f.read().rstrip().split(',')))

for chars in combinations_with_replacement(ascii_lowercase, 3):
    for key in permutations(chars):
        plaintext = ''.join(chr(b ^ ord(key[i % len(key)]))
                            for i, b in enumerate(ciphertext))
        if 'Euler' in plaintext:
            print(''.join(key), sum(map(ord, plaintext)), plaintext)
            sys.exit()
