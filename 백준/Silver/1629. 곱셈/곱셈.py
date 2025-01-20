import sys

def divCon(a, i, c):
    if i == 1:
        return a%c
    
    x = divCon(a, i//2, c)
    if i%2 != 0:
        return (x * x * a % c)
    else:
        return (x * x % c)
    
a, b, c = map(int, sys.stdin.readline().split(' '))

print(divCon(a, b, c))
