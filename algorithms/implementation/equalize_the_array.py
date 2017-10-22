n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

unique = list(set(arr))
counts = []
for i in range(0, len(unique)):
    counts.append(arr.count(unique[i]))

unique_counts = dict(zip(unique, counts))
unique_counts = sorted(unique_counts.values())
print(sum(unique_counts[0:-1]))
