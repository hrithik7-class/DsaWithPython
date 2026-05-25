class Node:
    def __init__(self , value=None , prev=None , next=None ):
        self.prev = prev
        self.value = value
        self.next = next 
        
        
        
class circularlyLinkedList:
    
    def __init__(self,head):
        self.head = head
        
        
    def insertAtEnd(self , value):
        t1= self.head          
        
        
        