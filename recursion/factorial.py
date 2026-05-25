# def fac(num):
#     if(num ==0 or num ==1 ):
#         return 1
#     else:
#         return num * fac(num-1)
    
    
    
    
# print (fac(3))    
    
    
def fibo(num):
    if(num == 1 or num ==2): return 1
    else: 
        return fibo(num-1) + fibo(num-2)
print(fibo(4 ))