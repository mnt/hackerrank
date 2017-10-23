n, d = input().strip().split(' ')
n, d = [int(n), int(d)]
seq = {}
for a in input().strip().split(' '):
    seq[int(a)] = int(a)

count = 0
for i in seq.keys():
    if i - d in seq and i + d in seq:
        count += 1

print(count)
