class Queue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    
    def insertion(self , value):
        return self.items.append(value)
    
    def deletion(self):
        if(self.isEmpty()):
            raise Exception("queue is empty")
        else:
            return self.items.pop(0)  
        
    def peek(self):
        if(self.isEmpty()):
            raise Exception("queue is empty")
        else:
            return self.items[0]
                   
        


obj = Queue()
obj.insertion(20)
obj.insertion(30)
obj.insertion(4)
obj.insertion(50)
print(obj.peek())