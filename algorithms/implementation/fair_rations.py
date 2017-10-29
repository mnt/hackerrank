n = int(input().strip())
a = [int(_) for _ in input().strip().split(' ')]

if (sum(a) % 2 != 0):
    print('NO')
else:
    c = 0
    for i in range(n):
        if a[i] % 2 != 0:
            a[i + 1] += 1
            c += 2
    print(c)
