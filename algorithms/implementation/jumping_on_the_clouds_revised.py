#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
energy = 100
index = 0
jumped = False
while index != 0 or not jumped:
    if not jumped:
        jumped = True
    if c[index] == 1:
        energy -= 2

    energy -= 1
    index = (index + k) % n

    if index == n:
        index = 0
    elif index > n:
        index = index - n

print(energy)
