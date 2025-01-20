import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None

class Tree:
    def __init__(self, root = None):
        self.root = root

    def findParent(self, curr, parent):
        if curr != None:
            if curr.val == parent:
                return curr
                
            left = self.findParent(curr.left, parent)
            if left != None:
                return left

            right = self.findParent(curr.right, parent)
            if right != None:
                return right
        
    def preorder(self, curr, result, n):
        if len(result) == n:
            return
        
        if curr != None:
            result.append(curr.val)
            self.preorder(curr.left, result, n)
            self.preorder(curr.right, result, n)
    
    def inorder(self, curr, result, n):
        if len(result) == n:
            return
        
        if curr != None:
            self.inorder(curr.left, result, n)
            result.append(curr.val)
            self.inorder(curr.right, result, n)
            
    def postorder(self, curr, result, n):
        if len(result) == n:
            return
        
        if curr != None:
            self.postorder(curr.left, result, n)
            self.postorder(curr.right, result, n)
            result.append(curr.val)
        
n = int(sys.stdin.readline().rstrip())

tree = {}
parent = {}
nodes = ['A']
for _ in range(n):
    me, left, right = sys.stdin.readline().rstrip().split(' ')
    
    tree[me] = (left, right)
    
    if left != '.':
        nodes.append(left)
        parent[left] = me
    if right != '.':
        nodes.append(right)
        parent[right] = me
    

rootNode = Node('A')
binTree = Tree(rootNode)

for node in nodes[1:]:
    parentNode = binTree.findParent(rootNode, parent[node])
    childNode = Node(node)
    childNode.parent = parentNode

    if tree[parent[node]][0] == node:
        parentNode.left = childNode
    else:
        parentNode.right = childNode

result = []
binTree.preorder(rootNode, result, n)
print(''.join(result))

result = []
binTree.inorder(rootNode, result, n)
print(''.join(result))

result = []
binTree.postorder(rootNode, result, n)
print(''.join(result))
