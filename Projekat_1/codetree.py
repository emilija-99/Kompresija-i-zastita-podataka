class node:
    def __init__(self, data):
        self.data = data;
        self.left = None
        self.right = None

root = node(1)
root.left = node(2)
root.right = node(3)

root.left.left = node(4);
root.left.right = node(5);

root.right.left = node(6)
root.right.right = node(7)

def inorder(node):
    if node:
        inorder(node.left)
        print(node.data)
        inorder(node.right)

inorder(root)
    
###
#             1
#        2           3
#    4       5   6       7
###