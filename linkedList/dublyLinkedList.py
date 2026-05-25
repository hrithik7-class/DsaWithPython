class Node:
    def __init__(self, value=None, prev=None , next=None ):
        self.prev = prev
        self.data = value
        self.next = next
        
        
class DublyLinkedList:     
       
        def __init__(self ,head=None):
            self.head = Node(head) if head is not None else None
                   
        
        def insertAtEnd (self , value):
            temp = Node(value)
            
            if(self.head == None):
                self.head = temp
                return
            
            t1 = self.head
            while(t1.next != None):
                t1= t1.next
                
            t1.next = temp
            temp.prev = t1  
        
        def PrintDLL(self):
            t = self.head
            while(t != None):   # ✅ safe traversal
                print(t.data)
                t = t.next
                
                
        def insertAtStart(self , value):
            temp = Node(20)
            t1 = self.head
            if(self.head== None):
                self.head= temp
                return
            else:
                temp.next=self.head
                self.head.prev = temp
                self.head = temp
                
        def insertAtMid(self , value , x):
            temp = Node(50)
            t1 = self.head
            while(t1.next != None):
                if(t1.data ==  x):
                    break
                else:
                    t1= t1.next
                 
                temp.next = t1.next 
                t1.next.prev =temp              
                t1.next=temp                
                temp.prev = t1
                
                
        def deleteDLL(self , value):
            t1 = self.head
            if(self.head == None):
                print("no node foundLL is empty")
                
            if(t1.data == value):
                self.head = t1.next
                self.head.prev = None
                return 
                
                         
                
            while(t1.next != None):
                if(t1.data == value):
                    
                    t1.prev.next = t1.next
                    t1.next.prev = t1.prev    
                    return
                t1 = t1.next
            
            if(t1.data == value):
                t1.prev.next = None
                return
            t1 = t1.next
                
                    
                    
                         
                   
obj = DublyLinkedList()
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtEnd(20)

obj.deleteDLL(40)
obj.PrintDLL()
        

        
