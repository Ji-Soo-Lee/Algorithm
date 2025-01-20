import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    
    line1 = list(map(int, sys.stdin.readline().rstrip().split(' ')))
    line2 = list(map(int, sys.stdin.readline().rstrip().split(' ')))
        
    result = [[0, 0] for _ in range(2*n)]
    
    result[0][0] = line1[0]
    result[n][0] = line2[0]
    
    for idx in range(1, n):
        # 윗줄 idx번째 붙이고 안 붙이고
        result[idx][0] = line1[idx] + max(result[idx - 1][1], max(result[idx - 1 + n]))
        result[idx][1] = max(max(result[idx - 1]), max(result[idx - 1 + n]))
        
        # 아랫줄 idx번째 붙이고 안 붙이고
        result[idx + n][0] = line2[idx] + max(result[idx + n - 1][1], max(result[idx - 1]))
        result[idx + n][1] = max(max(result[idx + n - 1]), max(result[idx - 1]))
    
    # print(result)     
    print(max(max(result[2*n - 1]), max(result[n - 1])))
