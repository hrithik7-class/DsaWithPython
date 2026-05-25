def selection_sort(arr):
    n =len(arr)
    

    for i in range(n):
        min_index = i
        
        for j in range(i,n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index], arr[i]
        
        
    return arr


arr = [64, 25, 12, 22, 11]
selection = selection_sort(arr)
print("Sorted array:", selection)    
        


    