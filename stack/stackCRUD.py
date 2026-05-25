class stack:
    def __init__(self):
        self.s = []
        
        
    def length(self):
        return len(self.s)
    
    def insertFn(self , value ):
        
        return self.s.insert(0,value)
    
    def peekFn(self):
        if(len(self.s) == 0 ):
            raise Exception("stack is empty")
        return self.s[0] 
    
    def deleteFn(self):
        if(len(self.s) == 0 ):
            raise Exception("empty stcak is not able to do deletion")
        return self.s.pop(0)    
    
    
    # task instead of insert fn use the append fn 
    
obj = stack()
# obj.insertFn(20)
# obj.insertFn(30)
# obj.insertFn(40)
# obj.insertFn(50)
# print(obj.deleteFn())
print(obj.deleteFn())
