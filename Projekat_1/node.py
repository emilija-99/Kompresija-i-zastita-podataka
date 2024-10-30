# Define a Binnary Tree
# each node must two have minimun 2 child
# left child is always smaller then right child
#             g 
#         c       i 
#     b      e h      j
# a        d    f         k 

import collections


class Node:
    def __init__(self, data):
        self.left = None;
        self.right = None;
        self.data = data;
    
    #     data
    # None    None
    
    def insert(self, data):
        if(self.data is None):
            self.data = data;
        else: 
            if data < self.data:
                if(self.left is None):
                    self.left = Node(data);
                else:
                    self.left.insert(data); # new root of tree
            elif (data > self.data):
                if(self.right is None):
                    self.right = Node(data);
                else:
                    self.right.insert(data);
class Tree:
# recursive function for inserting node
    
    def createNode(self,data):
        return Node(data);

    def insertNode(self, node, data):
        # print("Node,data",node, data);
        if node is None:
            return self.createNode(data)
        if(data < node.data):
            node.left = self.insertNode(node.left, data);
        elif(data > node.data):
            # print("data, node.data", data, node.data);
            node.right = self.insertNode(node.right, data);
        return node;
    
    def search(self, node, data):
        if node is None or node.data == data:
            return node;
        
        if node.data < data:
            return self.search(node.right,data);
        else:
            return self.search(node.left,data); 
        
    # print Tree <root, left, right>    
    def printTraversal(self, root):
        if root is None:
            return;
        print(root.data, end=" ")
        self.printTraversal(root.left)
        self.printTraversal(root.right)
     

def makeList(root):
    if(root is None):
        return
    else:
        d[root.data] = []
        makeList(root.left)
        if root.left:
            d[root.data].append(root.left.data)
        if(root.right):
            d[root.data].append(root.right.data)
        makeList(root.right)
    return d        

# print Tree <left,root,right>
def printTree(root):
    if root is None:
        return;
    printTree(root.left)
    print(root.data, end=' ')
    printTree(root.right)

def BFS(root, node):
    print("root, node",root, node)
    queue = []
    visited = []
    
    visited.append(node)
    print("visited",visited)
    queue.append(node)
    
    while(queue):
        ele = queue.pop(0)
        # print("ele",ele)
        for x in root[ele]:
            # print(x)
            if(x not in visited):
                # print("visited: ",x)
                visited.append(x)
                queue.append(x)
    return visited
        
if __name__ == '__main__':
    root = None
    tree = Tree()
    root = tree.insertNode(root, 10)
    
    
    tree.insertNode(root, 20)
    tree.insertNode(root, 30)
    tree.insertNode(root, 40)
    tree.insertNode(root, 70)
    tree.insertNode(root, 60)
    tree.insertNode(root, 80)
    
    d = {}
    print(' ')
    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(10)
    root.insert(19)
    root.insert(31)
    root.insert(42)
    print("Binnary Tree:");
    printTree(root)
    
    print(' ')
    
    # tree.printTraversal(root);
    
    aList = makeList(root)
    print(aList)
    
    BFS(aList,35);
    
    
    
    
    
    
        