import math;

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

first = True
evenly_divisible = []
for i in range(0, n):
    if arr[i] % k == 0 and not first:
        evenly_divisible.append(arr[i])
    if arr[i] % k == 0 and first:
        first = False

arr = list(set(arr) - set(evenly_divisible))

for i in range(1, math.ceil(k / 2) + 1):
    if i != k - i:
        a = []
        b = []
        for j in range(0, len(arr)):
            if arr[j] % k == i:
                a.append(arr[j])

            if arr[j] % k == k - i:
                b.append(arr[j])

        if len(a) > len(b):
            arr = list(set(arr) - set(b))
        else:
            arr = list(set(arr) - set(a))
    else:
        first = True
        evenly_divisible = []
        for j in range(0, len(arr)):
            if arr[j] % k == i and not first:
                evenly_divisible.append(arr[j])
            if arr[j] % k == i and first:
                first = False

        arr = list(set(arr) - set(evenly_divisible))

print(len(arr))
