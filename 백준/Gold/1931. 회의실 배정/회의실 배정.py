import sys

n = int(sys.stdin.readline().rstrip())
times = []


for _ in range(n):
    s, e = map(int, sys.stdin.readline().rstrip().split(' '))
    times.append((s, e))
    
times.sort()

curr = times[0]
cnt = 1

for time in times[1:]:
    if curr[1] > time[0] and curr[1] > time[1]:
            curr = time
            
    elif curr[1] <= time[0]:
        curr = time
        cnt += 1

print(cnt)
