#!/usr/bin/env python3

import sys

global cnt
global pos

pos = 4

def one(pos, num):

    result = []

    if cnt[num] == -1:
        for i in range(pos, num+1):
            if i%3 == 0:
                result.append(1 + cnt[i//3])
            if i%2 == 0:
                result.append(1 + cnt[i//2])
            result.append(1 + cnt[i - 1])

            cnt[i] = min(result)
            result = []

        pos = num
    
    return cnt[num]

num = int(sys.stdin.readline().rstrip())

cnt = [-1 for i in range(num+1)]

cnt[1] = 0
if num > 1:
    cnt[2] = 1
if num > 2:
    cnt[3] = 1

result = one(pos, num)

print(result)
