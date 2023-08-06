#!/usr/bin/env python3

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

m = int(sys.stdin.readline().rstrip())

graph = {}

for i in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split(' '))

    if start in graph:
        graph[start].append(end)
    else:
        graph[start] = [end]

    if end in graph:
        graph[end].append(start)
    else:
        graph[end] = [start]

if 1 in graph:
    stack = deque([1])
    result = [1]
    
    while len(stack) != 0:
        u = stack.pop()

        for num in graph[u]:
            if num not in result:
                result.append(num)
                stack.append(num)
        
    #print(u)

    print(len(result) - 1)
else:
    print(0)
    