import sys

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

nums = list(map(int, sys.stdin.readline().rstrip().split(' ')))

sum = [0 for _ in range(n + 1)]
sum[1] = nums[0]
for i in range(2, n + 1):
    sum[i] = nums[i - 1] + sum[i - 1]

for _ in range(m):
    i, j = map(int, sys.stdin.readline().rstrip().split(' '))
    print(sum[j] - sum[i - 1])
