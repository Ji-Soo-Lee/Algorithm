import sys

n = int(sys.stdin.readline())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, sys.stdin.readline().split(' '))))


sums = [[] for _ in range(n)]
sums[0].append(triangle[0][0])

for line in range(1, n):
    m = len(triangle[line])
    for idx in range(m):
        sums[line].append(triangle[line][idx] + max(sums[line - 1][max(0, min(idx, m - 2))], sums[line - 1][max(0, idx - 1)]))

print(max(sums[n - 1]))
