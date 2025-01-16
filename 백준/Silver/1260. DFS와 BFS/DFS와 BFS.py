import sys
from collections import deque

def dfs(visited, graph, pos, result):
    if pos not in graph:
        return
    else:
        for node in graph[pos]:
            if not visited[node]:
                visited[node] = True
                result.append(node)
                dfs(visited, graph, node, result)

n, m, start = map(int, sys.stdin.readline().rstrip().split(' '))
graph = {}

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split(' '))
    
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
        
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]
        
        
for node in range(1, n + 1):
    if node in graph:
        graph[node].sort()

visited = [False] * (n + 1)
result = [start]
visited[start] = True
dfs(visited, graph, start, result)
print(*result)

visited = [False] * (n + 1)
result = [start]
visited[start] = True
queue = deque([start])
while queue:
    v = queue.popleft()
    
    if v not in graph:
        continue

    for node in graph[v]:
        if not visited[node]:
            visited[node] = True
            result.append(node)
            queue.append(node)
print(*result)
