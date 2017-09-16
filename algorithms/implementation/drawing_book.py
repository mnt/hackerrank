#!/bin/python3

import sys
import math

def solve(n, p):
    front = p // 2
    back = (n - p) // 2 if p % 2 == 0 else (n - p + 1) // 2

    return front if front < back else back

n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
