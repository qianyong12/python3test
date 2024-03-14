"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from typing import List
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def visit(self,root:'Node'):
            if not root:
                return
            l.append(root.val)
            for child in root.children:
                visit(self,child)
        l = []
        visit(self,root)
        return l

if __name__=='__main__':
    node1 = Node(1,None)
    node2 = Node(2, None)
    node3 = Node(3, None)
    node0 = Node(1, [node1,node2,node3])
    s=Solution
    print(s.preorder(s,node0))

