#!/usr/bin/env python3

import sys

m = int(sys.stdin.readline().rstrip())

s = set()

for i in range(m):
    command = list(sys.stdin.readline().rstrip().split(' '))
    
    if len(command) == 1:
        if command[0] == 'all':
            s = set(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'])
        elif command[0] == 'empty':
            s = set()
    else:
        if command[0] == 'add':
            s.add(command[1])
        elif command[0] == 'remove':
            if command[1] in s:
                s.remove(command[1])
        elif command[0] == 'check':
            if command[1] in s:
                print('1')
            else:
                print('0')
        elif command[0] == 'toggle':
            if command[1] in s:
                s.remove(command[1])
            else:
                s.add(command[1])
