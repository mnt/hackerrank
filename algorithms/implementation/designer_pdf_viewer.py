#!/bin/python3

import sys
import string

h = list(map(int, input().strip().split(' ')))
word = input().strip()
heights = dict(zip(string.ascii_lowercase, h))
height = 0
for char in word:
    height = max(height, heights[char])

print(height * len(word))
