#!/usr/bin/env python3

import sys

n = int(sys.stdin.readline().rstrip())

scores = list(map(int, sys.stdin.readline().rstrip().split(' ')))

high = max(scores)

avg = sum(scores) / n
avg = avg / high * 100

print(avg)
