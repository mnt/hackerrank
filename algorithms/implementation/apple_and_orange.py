#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

ac = 0
oc = 0

for i in range(m):
    if apple[i] + a >= s and apple[i] + a <= t:
        ac = ac + 1

for i in range(n):
    if orange[i] + b >= s and orange[i] + b <= t:
        oc = oc + 1

print(ac)
print(oc)
