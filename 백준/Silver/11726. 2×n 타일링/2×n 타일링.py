import sys

n = int(sys.stdin.readline().rstrip())

num = [0 for _ in range(1001)]
num[1] = 1
num[2] = 2

for i in range(3, 1001):
    num[i] = num[i - 1] + num[i - 2]
    
print(num[n]%10007)
