import sys

def backtracking(curr, n, m, result):
    if len(result) == m:
        print(*result)
        return
    else:
        for num in range(curr + 1, n + 1):
            # print(num, curr, result)
            if num > result[-1]:
                result.append(num)
                backtracking(curr + 1, n, m, result)
                result.pop()
            
        
n, m = map(int, sys.stdin.readline().rstrip().split(' '))

for i in range(1, n - m + 2):
    backtracking(i, n, m, [i])
