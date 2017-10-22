#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

changes = abs(len(s) - len(t))
shorter_string_length = min(len(s), len(t))
for i in range(0, shorter_string_length):
    if s[i] != t[i]:
        changes += (shorter_string_length - i) * 2
        break

if changes > k:
    print('No')
elif changes == 0:
    print('Yes')
elif len(s) + len(t) <= k:
    print('Yes')
elif changes % 2 == k % 2 and changes != 0:
    print('Yes')
else:
    print('No')
