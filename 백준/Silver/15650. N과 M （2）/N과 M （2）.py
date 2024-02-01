#!/usr/bin/env python3

import sys

def append(arr, index, n, m):

    for num in range(index+1, n+2):
        if len(arr) == m:
            print(*arr)
            arr.pop()
            break
        
        elif num > n:
            arr.pop()
        
        elif len(arr) != m:
            arr.append(num)
            
            append(arr, num, n, m)
                        

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

for index in range(1, n - m + 2):
    
    arr = [index]

    append(arr, index, n, m)
        