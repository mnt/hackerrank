#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
   topic_t = int(input().strip(), 2)
   topic.append(topic_t)

max_topics = 0
count = 0
for i in range(0, n - 1):
    for j in range(i + 1, n):
        topics = bin(topic[i] | topic[j]).count("1")

        if topics > max_topics:
            max_topics = topics
            count = 1
        elif topics == max_topics:
            count += 1

print(max_topics)
print(count)
