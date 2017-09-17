#!/bin/python3

import sys

q = int(input().strip())
for a0 in range(q):
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]

    a = abs(z - x)
    b = abs(z - y)

    if a < b:
        print('Cat A')
    elif a > b:
        print('Cat B')
    else:
        print('Mouse C')
