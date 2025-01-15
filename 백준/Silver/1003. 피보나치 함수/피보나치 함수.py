import sys

fib = [0 for _ in range(41)]

fib[0] = (1, 0)
fib[1] = (0, 1)

for i in range(2, 41):
    fib[i] = (fib[i - 1][0] + fib[i - 2][0], fib[i - 1][1] + fib[i - 2][1])

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(fib[n][0], fib[n][1])
