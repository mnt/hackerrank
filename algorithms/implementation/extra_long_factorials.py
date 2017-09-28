#!/bin/python3

import sys

n = int(input().strip())
output = n
for i in range(n - 1, 1, -1):
    output = output * i

print(output)
