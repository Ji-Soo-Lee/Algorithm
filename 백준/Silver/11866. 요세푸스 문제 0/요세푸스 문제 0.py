#!/usr/bin/env python3

import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split(' '))

ring = deque()

for i in range(1, n+1):
    ring.append(i)

i = k
result = []

while len(ring) != 0:

    ring.rotate(-i)

    result.append(str(ring.pop()))

print('<' + ', '.join(result) + '>')
