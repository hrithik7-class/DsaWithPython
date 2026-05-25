class CircularyList:
    def __init__(self , size):
        self.size = size
        self.items = [None] * size
        self.front = self.rear = -1
        
        
    def enqueue (self , value):
        
        if((self.rear + 1) % self.size ==  self.front):
            print(f"queue is full")
            
        elif self.front == -1:
            self.front = self.rear =0 
            self.items[self.rear] = value 
            print(self.items) 
             
        else:
            self.rear = (self.rear + 1 ) % self.size    
            self.items[self.rear] = value
        
        
    def dequeue(self):
        if(self.front == -1):
            print("queue is empty")
            
        elif  self.front == self.rear:
            self.front = self.rear = -1
            
        else:
            print(self.items[self.front])
            self.front = ( self.front +1 ) % self.size     
        
           
        
obj = CircularyList(9)

obj.enqueue(20)
obj.enqueue(24)
obj.enqueue(26)
obj.enqueue(28)
obj.enqueue(30)
obj.enqueue(32)
