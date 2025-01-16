import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split(' '))
graph = []
dist = [[-1 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

target = (0, 0)

for x in range(n):
    line = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    graph.append(line)
    
    for y in range(len(line)):
        if line[y] == 2:
            target = (x, y)
        if line[y] == 0:
            dist[x][y] = 0

queue = deque([target])
dist[target[0]][target[1]] = 0
visited[target[0]][target[1]] = True

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while queue:
    currX, currY = queue.popleft()
    
    for i in range(4):
        nextX = currX + dx[i]
        nextY = currY + dy[i]
        
        if nextX < 0 or nextY < 0 or nextX >= n or nextY >= m:
            continue
        if visited[nextX][nextY] or graph[nextX][nextY] == 0:
            continue

        visited[nextX][nextY] = True

        dist[nextX][nextY] = dist[currX][currY] + 1
        queue.append((nextX, nextY))
        
for line in dist:
    print(*line)
