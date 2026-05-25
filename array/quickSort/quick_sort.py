def quick_sort(arr,l,r):
    if(l<r):
        p = partition(arr,l,r)
        
        quick_sort(arr,l,p-1)
        quick_sort(arr,p+1,r)
            
        
def partition(arr,l,r):

    pivot = arr[l]
    i = l + 1
    j = r

    while True:
        while i <= r and arr[i] < pivot:   # Bug fix 1: use proper bounds, not i<j
            i += 1
        while j > l and arr[j] > pivot:    # Bug fix 1: use proper bounds, not i<j
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
        i += 1                             # Bug fix 2: advance pointers after swap
        j -= 1


    arr[l], arr[j] = arr[j], arr[l]
    return j
arr = [22, 35, 20, 15, 40, 5]
quick_sort(arr,0,len(arr)-1)
print("Sorted array is: ", arr)

#  Quick Sort Concept
  
#   Core idea: Pick a pivot, put everything smaller on the left and everything
#    larger on the right, then recurse on both halves.

#   [22, 35, 20, 15, 40, 5]
#     ^pivot

#   After partition → [15, 5, 20, | 22 | 40, 35]
#                                  ^pivot is in its final sorted position

#   Recurse left:  [15, 5, 20]
#   Recurse right: [40, 35]

#   ---
#   How Partition Works (step by step)

#   You use two pointers (i from left, j from right) to scan toward the
#   middle:

#   pivot = arr[l] = 22
#   i starts at l+1 = 1  (scans right, looking for element >= pivot)
#   j starts at r   = 5  (scans left,  looking for element <= pivot)

#   [22, 35, 20, 15, 40, 5]
#     P   i               j

#   Step 1: i stops at 35 (≥22), j stops at 5 (≤22)
#           i < j → swap them → [22, 5, 20, 15, 40, 35]
#           advance: i=2, j=4

#   Step 2: i scans: 20<22→skip, 15<22→skip, 40≥22→stop. i=4
#           j scans: 40>22→skip, 15≤22→stop. j=3
#           i >= j → BREAK

#   Place pivot: swap arr[l] with arr[j]
#           swap arr[0] with arr[3] → [15, 5, 20, 22, 40, 35]
#                                                  ^pivot in place!
#   return j=3

#   ---
#   Why your original code broke
  
#   In your original code, the guard i<j inside the inner while loops caused j
#    to stop early (when i==j) without checking if arr[j] > pivot. So when you
#    swapped arr[l] with arr[j], j was pointing at an element larger than the 
#   pivot, placing the pivot in the wrong spot.

#   The fix: give each pointer its own independent boundary (i <= r and j > 
#   l), and let them cross — the outer if i >= j: break is what stops the
#   process.
                      
        