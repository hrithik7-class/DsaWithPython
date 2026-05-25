class Dequeue:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    
    def insertionAtLast(self , value):
        return self.items.append(value)
    
    def deletionFromFirst(self):
        if(self.isEmpty()):
            raise Exception("queue is empty")
        else:
            return self.items.pop(0)  
        
    def peek(self):
        if(self.isEmpty()):
            raise Exception("queue is empty")
        else:
            return self.items[0]
                   
    def insertionAtFirst(self , value):
        return self.items.insert(0, value)
    
    def deletionFromLast(self):
        if(self.isEmpty()):
            raise Exception("queue is empty")
        else:
            return self.items.pop() 


obj = Dequeue()
obj.insertionAtLast(20)
obj.insertionAtLast(30)
obj.insertionAtFirst(4)
obj.insertionAtFirst(50)
obj.deletionFromLast()
print(obj.peek())