#!/bin/python3

import sys
import math


s = input().strip()
n = int(input().strip())

r = n % len(s)
count = 0
count += s.count('a') * math.floor(n / len(s))
count += s[0: r].count('a')
print(count)
