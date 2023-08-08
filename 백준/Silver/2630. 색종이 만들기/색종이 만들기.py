#!/usr/bin/env python3

import sys

def same(paper, n):
    color = paper[0][0]
    for i in range(n):
        for square in paper[i]:
            if color != square:
                return False
    return True

def cut(paper, n, white, blue):

    if same(paper, n):
        if paper[0][0] == 1:
            blue += 1
        elif paper[0][0] == 0:
            white += 1
        return white, blue
    
    else:
        length = n//2
        
        i = list()
        ii = list()
        iii = list()
        iv = list()
        for j in range(n//2):
            i.append(paper[j][:n//2])
            ii.append(paper[j][n//2:])
            iii.append(paper[j+n//2][:n//2])
            iv.append(paper[j+n//2][n//2:])
        
        white_i, blue_i = cut(i, length, white, blue)
        white_ii, blue_ii = cut(ii, length, white_i, blue_i)
        white_iii, blue_iii = cut(iii, length, white_ii, blue_ii)
        white_iv, blue_iv = cut(iv, length, white_iii, blue_iii)

        return white_iv, blue_iv


    
n = int(sys.stdin.readline().rstrip())
paper = [0 for i in range(n)]

for i in range(n):
    paper[i] = list(map(int, sys.stdin.readline().rstrip().split(' ')))

white = 0
blue = 0

white, blue = cut(paper, n, white, blue)

print(white)
print(blue)
