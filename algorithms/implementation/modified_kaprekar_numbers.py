p = int(input().strip())
q = int(input().strip())

kaprekar_numbers = []
for i in range(p, q+1):
    squared = str(i**2)
    length = len(squared)
    right = squared[int(length/2):]
    left = squared[0:int(length/2)]

    left = int(left or 0)
    right = int(right or 0)
    if(left + right == i):
        kaprekar_numbers.append(i)


if len(kaprekar_numbers) > 0:
    print(' '.join(str(x) for x in kaprekar_numbers))
else:
    print('INVALID RANGE')
