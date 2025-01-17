#!/usr/bin/env python3

import sys
from collections import deque

def find_z(num, r, c, position, i):

    if num == 0:
        return position
    
    else:
        if (r <= num//2) and (c <= num//2):
            pos = 0
        elif (r > num//2) and (c <= num//2):
            pos = 2
        elif (r <= num//2) and (c > num//2):
            pos = 1
        elif (r > num//2) and (c > num//2):
            pos = 3

        num = num//2

        if pos == 3:
            r -= 2**i
            c -= 2**i
        elif pos == 2:
            r -= 2**i
        elif pos == 1:
            c -= 2**i
        
        if r < 0:
            r = 0
        if c < 0:
            c = 0

        i -= 1

        position.append(pos)

        find_z(num, r, c, position, i)

        return position

n, r, c = map(int, sys.stdin.readline().rstrip().split(' '))

num = 2**n - 1

i = n - 1

position = deque()

position = find_z(num, r, c, position, i)

result = position.pop()

for i in range(1, n):
    num = position.pop()

    result += 2**(2*i)*num

print(result)
