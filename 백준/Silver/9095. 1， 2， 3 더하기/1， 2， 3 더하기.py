import sys

# 1 => 1
# 2 => 1 + 1, 2 => 2
# 3 => 1 + 1 + 1, 1 + 2, 2 + 1, 3 => 4
# 4 => 7
num = [0 for i in range(11)]

num[1] = 1
num[2] = 2
num[3] = 4

for i in range(4, 11):
    num[i] = num[i - 1] + num[i - 2] + num[i - 3]


t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(num[n])
