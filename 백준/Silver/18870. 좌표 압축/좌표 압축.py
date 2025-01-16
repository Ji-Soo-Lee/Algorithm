import sys

n = int(sys.stdin.readline().rstrip())
x = list(map(int, sys.stdin.readline().rstrip().split(' ')))

y = sorted(list(set(x)))
mapping = {}
for idx in range(len(y)):
    mapping[y[idx]] = idx

compressed = []

for num in x:
    compressed.append(str(mapping[num]))
    
print(' '.join(compressed))
