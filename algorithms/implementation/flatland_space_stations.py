n, m = input().strip().split(' ')
n, m = [int(n),int(m)]
stations = [int(_) for _ in input().strip().split(' ')]
stations.sort()

if m == 1:
    c = max(stations[0] - 0, n - 1 - stations[0])
else:
    c = 0
    for i in range(1, m):
        c = max((stations[i] - stations[i - 1]) // 2, c)

    c = max(stations[0] - 0, n - 1 - stations[m - 1], c)

print(c)
