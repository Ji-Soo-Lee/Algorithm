#!/usr/bin/env python3

import sys

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

nums = list(map(int, sys.stdin.readline().rstrip().split(' ')))

sum_list, sum = [0], 0

for num in nums:
    sum += num
    sum_list.append(sum)
    
for _ in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split(' '))
    print(sum_list[end] - sum_list[start - 1])
    