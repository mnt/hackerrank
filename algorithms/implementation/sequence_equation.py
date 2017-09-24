n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

for i in range(1, n + 1):
    print(a.index(a.index(i) + 1) + 1)
