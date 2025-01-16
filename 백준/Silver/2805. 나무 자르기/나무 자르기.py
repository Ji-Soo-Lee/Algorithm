import sys

def cut(trees, m, n, low, high):
    h = (low + high) // 2
    if low > high:
        print(h)
        return
    
    x = 0
    for tree in trees:
        x += max(tree - h, 0)
    if x == m:
        print(h)
        return
    
    elif x > m:
        return cut(trees, m, n, h + 1, high)
    else:
        return cut(trees, m, n, low, h - 1)


n, m = map(int, sys.stdin.readline().rstrip().split(' '))
trees = list(map(int, sys.stdin.readline().rstrip().split(' ')))
trees.sort()

cut(trees, m, n, 0, trees[-1])
