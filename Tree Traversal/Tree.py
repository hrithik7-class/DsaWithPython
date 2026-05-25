class Node:
    def  __init__(self, data , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
        
def preOrder(root):
    if  root is not None:
        print(root.data , end=" ")
        
        preOrder(root.left)
        preOrder(root.right)
        
        
        
def postOrder(root):
    if  root is not None:

        
        postOrder(root.left)  
        
        postOrder(root.right)     
        print(root.data , end=" ")
        
def InOrder(root):
    if  root is not None:

        
        InOrder(root.left)
        print(root.data , end=" ")     
        InOrder(root.right)     
             
        

root = Node(1)  
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.right =  Node(8)      

preOrder(root)
print("")
InOrder(root)
print("")   
postOrder(root)

