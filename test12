'''
使用python实现二叉树的遍历算法，preorder,
postorder,inorder and BFS广度优先
'''
class TreeNode:
    def __init__(self, val=0 , right=None , left=None):
        self.val = val
        self.right = right
        self.left = left

def preorder(node):
    if not node:
        return
    print(node.val)
    preorder(node.left)
    preorder(node.right)

def inorder(node):
    if not node:
        return
    inorder(node.left)
    print(node.val)
    inorder(node.right)

def postorder(node):
    if not node:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.val)

def BFS(node):
    queue = [node]  #使用列表快速实现队列
    while queue:
        cur = queue.pop(0)
        if cur:
            print(cur.val)
            queue.append(cur.left)
            queue.append(cur.right)


if __name__=='__main__':
    node = []
    for i in range(0 , 50):
        node.append(TreeNode(i))
    for i in range(0 , 50):
        if i*2+2 < 50:
            node[i].left = node[i*2+1]
            node[i].right = node[i*2+2]
        else:
            node[i].right = None
            node[i].left = None
    root = node[0]
    BFS(root)
