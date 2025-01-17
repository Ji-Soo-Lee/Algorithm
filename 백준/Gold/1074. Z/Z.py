import sys

n, r, c = map(int, sys.stdin.readline().rstrip().split(' '))

x = n
result = 0
cnt = 0

while x > 1:
    div = 2**(x - 1)
    result += 2**(2*(n - 1 - cnt)) * (2*(r//div) + c//div)
    
    x -= 1
    r, c = r%div, c%div
    cnt += 1

print(result + 2*r + c)
