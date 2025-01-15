import sys

n = int(sys.stdin.readline().rstrip())
p = list(map(int, sys.stdin.readline().rstrip().split(" ")))

if n == 1:
    print(p[0])
elif n == 2:
    print(p[0] + p[0] + p[1])
else:
    p.sort()

    sum = []
    sum.append(p[0])
    sum.append(p[0] + p[1])

    for idx in range(2, len(p)):
        sum.append(sum[idx - 1] + p[idx])
        
    val = 0
    for time in sum:
        val += time

    print(val)
