#!/usr/bin/env python3

import sys
from collections import deque

n, k = map(int, input().rstrip().split(' '))

queue = deque([n])

visit = [0 for _ in range(100001)]

visit[n] = 1

time = 0

while visit[k] != 1:
    
    limit = len(queue)

    for i in range(limit):
        curr = queue.popleft()

        if curr - 1 >= 0:
            if visit[curr - 1] == 0:
                queue.append(curr - 1)
                visit[curr - 1] = 1
            
        if curr + 1 <= 100000:
            if visit[curr + 1] == 0:
                queue.append(curr + 1)
                visit[curr + 1] = 1
        
        if curr*2 <= 100000:
            if visit[curr*2] == 0:
                queue.append(curr*2)
                visit[curr*2] = 1
    
    time += 1

print(time)
