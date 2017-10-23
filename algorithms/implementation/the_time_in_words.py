h = int(input().strip())
m = int(input().strip())

time = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'quarter',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    21: 'twenty one',
    22: 'twenty two',
    23: 'twenty three',
    24: 'twenty four',
    25: 'twenty five',
    26: 'twenty six',
    27: 'twenty seven',
    28: 'twenty eight',
    29: 'twenty nine',
    30: 'half'
}

if m == 0:
    print(time[h] + " o' clock")
elif m > 30:
    m = 60 - m
    if m == 1:
        print(time[m] + ' minute to ' + time[h+1])
    elif m != 15:
        print(time[m] + ' minutes to ' + time[h+1])
    else:
        print(time[m] + ' to ' + time[h+1])
else:
    if m == 1:
        print(time[m] + ' minute past ' + time[h])
    if m == 30:
        print(time[m] + ' past ' + time[h])
    elif m != 15:
        print(time[m] + ' minutes past ' + time[h])
    else:
        print(time[m] + ' past ' + time[h])
