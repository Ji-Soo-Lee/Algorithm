import sys

def backtracking(result, n, m, idxAns):
    if len(result) == m:
        idxAns.add(' '.join(str(s) for s in result))
        return
    
    for num in range(n):
        if num not in result:
            result.append(num)
            backtracking(result, n, m, idxAns)
            result.pop()
                    
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
comp = list(map(int, sys.stdin.readline().rstrip().split(' ')))

comp.sort()

idxAns = set()

for i in range(n):
    backtracking([i], n, m, idxAns)
    
idxAns = sorted(list(idxAns))
# print(idxAns)
results = set()

for idxs in idxAns:
    idxs = map(int, idxs.split(' '))
    result = []
    for idx in idxs:
        result.append(str(comp[idx]))
    results.add(' '.join(result))

results = list(results)
for idx in range(len(results)):
    results[idx] = list(map(int, results[idx].split(' ')))
    
for result in sorted((results)):
    print(*result)
