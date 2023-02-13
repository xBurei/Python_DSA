import numpy as np

class Node:
    def  __init__(self, value, depth) :
        self.value = value
        self.left = None
        self.right = None
        self.depth = depth
        
    def insertNode(self, value):
        if self.value:
            if value<self.value:
                if self.left is None:
                    self.left = Node(value, self.depth+1)
                else:
                    self.left.insertNode(value)
            elif value>self.value:
                if self.right is None:
                    self.right = Node(value, self.depth+1)
                else:
                    self.right.insertNode(value)    
        else:
            self.value = value
            
    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.value, 'd'+ str(self.depth))
        if self.right:
            self.right.printTree()
        
                
root = Node(10, 0)
for i in range(20):
    root.insertNode(np.random.randint(0, 20)
)
    
root.printTree()