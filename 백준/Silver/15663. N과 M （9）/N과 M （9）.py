import sys

def backtracking(result, n, m, comp, idx):
    if len(result) == m:
        print(*result)
        return
    
    prevNum = -1
    for num in range(n):
        if num not in idx:
            if prevNum != comp[num]:
                result.append(comp[num])
                idx.append(num)
                backtracking(result, n, m, comp, idx)
                result.pop()
                idx.pop()
                prevNum = comp[num]
                    
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
comp = list(map(int, sys.stdin.readline().rstrip().split(' ')))

comp.sort()

prevNum = -1
for i in range(n):
    if comp[i] != prevNum:
        backtracking([comp[i]], n, m, comp, [i])
        prevNum = comp[i]
    