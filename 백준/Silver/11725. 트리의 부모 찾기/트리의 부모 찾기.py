import sys
sys.setrecursionlimit(10**6)

def search(graph, curr, visited, parent):
    for node in graph[curr]:
        if not visited[node]:
            parent[node] = curr
            visited[node] = True
            search(graph, node, visited, parent)
            
n = int(sys.stdin.readline().rstrip())
graph = {}

for _ in range(n - 1):
    i, j = map(int, sys.stdin.readline().rstrip().split(' '))
    
    if i in graph:
        graph[i].append(j)
    else:
        graph[i] = [j]
    
    if j in graph:
        graph[j].append(i)
    else:
        graph[j] = [i]
        
parent = [None for _ in range(n + 1)]
# parent[0], parent[1] = 0, 0
visited = [False for _ in range(n + 1)]
visited[1] = True
search(graph, 1, visited, parent)

for idx in range(2, n + 1):
    print(parent[idx])
    