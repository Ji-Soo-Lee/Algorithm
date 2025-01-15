import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, graph, visited, bc):
    visited[x][y] = 1
    bc.discard((x, y))
    maxX = min(x + 1, m - 1)
    minX = max(x - 1, 0)
    maxY = min(y + 1, n - 1)
    minY = max(y - 1, 0)
    # right
    if graph[maxX][y] == 1 and visited[maxX][y] == 0:
        dfs(maxX, y, graph, visited, bc)
    # left
    if graph[minX][y] == 1 and visited[minX][y] == 0:
        dfs(minX, y, graph, visited, bc)
    # up
    if graph[x][minY] == 1 and visited[x][minY] == 0:
        dfs(x, minY, graph, visited, bc)
    # down
    if graph[x][maxY] == 1 and visited[x][maxY] == 0:
        dfs(x, maxY, graph, visited, bc)

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().rstrip().split(' '))
    worm = set()
    bc = set()

    graph = [[0 for _ in range(n)] for _ in range(m)]
    visited = [[0 for _ in range(n)] for _ in range(m)] 

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().rstrip().split(' '))
        graph[x][y] = 1
        bc.add((x, y))
    
    result = 0
    while len(bc) != 0:
        x, y = bc.pop()
        dfs(x, y, graph, visited, bc)
        result += 1
        
    print(result)
    