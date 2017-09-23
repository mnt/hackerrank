#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    height = 1
    for i in range(0, n):
        height = height * 2 if i % 2 == 0 else height + 1

    print(height)
