i, j, k = input().strip().split(' ')
i, j, k = [int(i), int(j), int(k)]

count = 0
for date in range(i, j + 1):
    reverse = int(str(date)[::-1])
    if abs(date - reverse) % k == 0:
        count += 1

print(count)
