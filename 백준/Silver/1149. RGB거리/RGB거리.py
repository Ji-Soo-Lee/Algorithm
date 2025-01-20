import sys

n = int(sys.stdin.readline().rstrip())

houses = []
for _ in range(n):
    r, g, b = map(int, sys.stdin.readline().rstrip().split(' '))
    houses.append((r, g, b))

costs = [[0, 0, 0] for _ in range(n)]

costs[0] = list(houses[0])

for idx in range(1, n):
    costs[idx][0] = houses[idx][0] + min(costs[idx - 1][1], costs[idx - 1][2])
    costs[idx][1] = houses[idx][1] + min(costs[idx - 1][0], costs[idx - 1][2])
    costs[idx][2] = houses[idx][2] + min(costs[idx - 1][0], costs[idx - 1][1])

print(min(costs[-1]))
