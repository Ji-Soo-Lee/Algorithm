import sys
sys.setrecursionlimit(10**6)

def dfs(graph, u, visited, node):
    visited[u] = 1
    node.discard(u)
    
    for v in graph[u]:
        if visited[v] == 0:
            dfs(graph, v, visited, node)

n, m = map(int, sys.stdin.readline().rstrip().split(' '))
graph = {}

for _ in range(m):
    u, v = map(int, sys.stdin.readline().rstrip().split(' '))
    
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)
    
    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u)
    
node = set([i for i in range(1, n+1)])
visited = [0 for _ in range(n + 1)]
connected = 0

while len(node) != 0:
    u = node.pop()
    if u not in graph:
        connected += 1
    else:
        dfs(graph, u, visited, node)
        connected += 1
    
print(connected)
