#!/bin/python3

import sys
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
height = list(map(int, input().strip().split(' ')))
# your code goes here
height.sort()
if height[-1] > k:
    print(height[-1] - k)
else:
    print(0)
