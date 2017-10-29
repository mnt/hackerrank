t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    a = int(input().strip())
    b = int(input().strip())

    f = []
    for i in range(0, n):
        f.append((a * i) + (b * (n - i - 1)))

    f = list(set(f))
    print(' '.join(map(str, sorted(f))))
