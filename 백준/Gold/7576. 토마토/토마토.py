#!/usr/bin/env python3

import sys
from collections import deque

def search(box, queue, cnt):

    x, y = queue.popleft()

    if x == 0 and y == 0:
        right = x + 1
        if box[y][right] == 0:
            queue.append((right, y))
            box[y][right] = '_'
            cnt += 1
        
        down = y + 1
        if box[down][x] == 0:
            queue.append((x, down))
            box[down][x] = '_'
            cnt += 1

    elif y == 0:
        right = x + 1
        if box[y][right] == 0:
            queue.append((right, y))
            box[y][right] = '_'
            cnt += 1
        
        down = y + 1
        if box[down][x] == 0:
            queue.append((x, down))
            box[down][x] = '_'
            cnt += 1
        
        left = x - 1
        if box[y][left] == 0:
            queue.append((left, y))
            box[y][left] = '_'
            cnt += 1

    elif x == 0:
        right = x + 1
        if box[y][right] == 0:
            queue.append((right, y))
            box[y][right] = '_'
            cnt += 1
        
        down = y + 1
        if box[down][x] == 0:
            queue.append((x, down))
            box[down][x] = '_'
            cnt += 1
        
        up = y - 1
        if box[up][x] == 0:
            queue.append((x, up))
            box[up][x] = '_'
            cnt += 1

    else:
        right = x + 1
        if box[y][right] == 0:
            queue.append((right, y))
            box[y][right] = '_'
            cnt += 1
        
        down = y + 1
        if box[down][x] == 0:
            queue.append((x, down))
            box[down][x] = '_'
            cnt += 1
        
        up = y - 1
        if box[up][x] == 0:
            queue.append((x, up))
            box[up][x] = '_'
            cnt += 1

        left = x - 1
        if box[y][left] == 0:
            queue.append((left, y))
            box[y][left] = '_'
            cnt += 1
        
    return cnt

m, n = map(int, sys.stdin.readline().rstrip().split(' '))

box = [['_']*(m + 1) for _ in range(n + 1)]

for i in range(n):
    tomatoes = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    
    for j in range(m):
        box[i][j] = tomatoes[j]

queue = deque()

day = 0

cnt = 0

no_tomato = 0

for y in range(n):
    for x in range(m):
        if box[y][x] == 1:
                queue.append((x, y))
                box[y][x] = '_'
                cnt += 1
        if box[y][x] == -1:
            no_tomato += 1

while len(queue) != 0:

    limit = len(queue)

    for i in range(limit):
        cnt = search(box, queue, cnt)
    
    day += 1   

if cnt < n*m - no_tomato:
    day = -1
else:
    day -= 1

print(day)
