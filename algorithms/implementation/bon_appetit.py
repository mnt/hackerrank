#!/bin/python3

import sys

def bonAppetit(n, k, b, ar):
    bill = ar[:]
    bill.pop(k)
    cost = sum(bill)

    if cost / 2 == b:
        return "Bon Appetit"
    else:
        refund = ar[k] / 2
        return int(refund) if refund.is_integer() else refund

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
