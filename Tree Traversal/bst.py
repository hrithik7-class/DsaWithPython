class Node:
    def  __init__(self, data , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
             
        
def insert(root , data): 
    if root is None:
        return Node(data) 
    if (root.data  == data):
        return root
    if root.data > data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)    
    return root    


def search(root , data):
    if root is None:
        return print("Element Not Found") 
        
    if (root.data  == data):
        return print("Element Found")
    if root.data > data:
        search(root.left, data)
    else:
        search(root.right, data)     
            
            
def inOrder(root):
    if root is not None:
        inOrder(root.left)
        print(root.data, end=" ")
        inOrder(root.right)
        
        
root = insert(None , 20)
root = insert(root , 15)
root = insert(root , 30)
root = insert(root , 12)
root = insert(root , 18)
root = insert(root , 40)        
              
            
inOrder(root )            