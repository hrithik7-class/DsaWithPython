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

def succcessor(root):
    root =root.right
    while root.left is not None and root is not None:
        root = root.left
    return root

def deletion(root,value):
    if root is None:
        return root
    if root.data  > value:
       root.left =   deletion(root.left , value)
    elif root.data  < value:
        root.right = deletion(root.right , value)    
    else:
        if(root.left is None):
            return root.right
        elif(root.right is None):
            return root.left   
        else:
            temp = succcessor(root)
            root.data = temp.data
            root.right = deletion(root.right , temp.data)
            
    return root

        
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

deletion( root,18)   
print("\nAfter Deletion :")
inOrder(root )
print("\n")           