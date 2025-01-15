#!/usr/bin/env python3

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split(' '))

no_hear = {}

result = []

for i in range(n):
    no_hear[sys.stdin.readline().rstrip()] = i + 1

for i in range(m):
    no_see = sys.stdin.readline().rstrip()

    if no_see in no_hear:
        result.append(no_see)

result.sort()

print(len(result))

for name in result:
    print(name)
