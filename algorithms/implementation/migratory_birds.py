#!/bin/python3

import sys

def migratoryBirds(n, ar):
    birds = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    for i in range(n):
        birds[ar[i]] += 1

    return max(birds, key=birds.get)

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)
