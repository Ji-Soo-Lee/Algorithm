#!/usr/bin/env python3

n = int(input())
voca = [0 for i in range(n)]

for i in range(n):
    voca[i] = input()
    i += 1

repeat = set(voca)

result = list(repeat)

result.sort()
result.sort(key = len)

for i in range(len(result)):
    print(result[i])
    i += 1
