import sys

def dfs(v, graph, visited, sum):
    visited[v - 1] = True
    virus = set()
    
    for c in graph[v]:
        if visited[c - 1] == False:
            sum.add(c)
            dfs(c, graph, visited, sum)


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

coms = {}

for idx in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    
    if a in coms:
        coms[a].append(b)
    else:
        coms[a] = [b]
        
    if b in coms:
        coms[b].append(a)
    else:
        coms[b] = [a]
        
if 1 not in coms:
    print(0)
else:
    visited = [False for _ in range(n)]
    sum = set()
    dfs(1, coms, visited, sum)
    
    print(len(sum))
