t = int(input().strip())
for a0 in range(t):
    n, c, m = input().strip().split(' ')
    n, c, m = [int(n),int(c),int(m)]
    choc = n // c
    r = n // c
    while r >= m:
        choc += r // m
        r = r % m + r // m

    print(choc)
