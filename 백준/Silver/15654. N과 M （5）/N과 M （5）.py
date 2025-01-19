import sys

def backtracking(start, curr, n, m, result, comp):
    if len(result) == m:
        print(*result)
        return
    else:
        for num in range(n):
            if comp[num] not in result:
                result.append(comp[num])
                backtracking(start, curr + 1, n, m, result, comp)
                result.pop()
                    
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
comp = list(map(int, sys.stdin.readline().rstrip().split(' ')))

comp.sort()

for i in range(n):
    backtracking(i, i, n, m, [comp[i]], comp)
    