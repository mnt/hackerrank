#!/bin/python3

import sys

def getMoneySpent(keyboards, drives, s):
    amount = -1
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive > amount and keyboard + drive <= s:
                amount = keyboard + drive
                
    return amount

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)
