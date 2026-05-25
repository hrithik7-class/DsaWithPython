def divide(arr , l ,r):
    
    m= (l + r )//2
    if(l<r):
        divide(arr , l , m)
        divide(arr , m+1 , r)
    
        merge_sort(arr , l, m ,r)

         
    
def merge_sort(arr ,  l , m, r ):
    
    s1 = m - l + 1
    s2 = r - m
    left = [0]* s1
    right = [0]* s2
    
    for i in range(s1):
        left[i ]=arr[l + i]
    for j in range(s2):
        right[j] = arr[m + 1 + j]
        
    i = j = 0
    k= l
    
    while(i <s1 and j <s2):
        if(left[i] <= right[j]):
            arr[k] = left   [i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1  
        
    while(i < s1):
        arr[k] = left[i]
        i += 1
        k += 1  
        
    while(j < s2):
        arr[k] = right[j]
        j += 1
        k += 1    
              
              
arr = [38, 27, 43, 3, 9, 82, 10]
divide(arr , 0 , len(arr)-1)
print("Sorted array is: ", arr)                   
        
        
    
    