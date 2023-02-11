import numpy as np
import time

def merge_sort(array): # divide and conquer
        if len(array) == 1: return array 
        
        middle_index = len(array)//2
        
        right_split = merge_sort(array[middle_index:])
        left_split = merge_sort(array[:middle_index])
        
        return merge(left_split, right_split)    
    
def merge(left, right): # conquer and combine
    out = []
    r_index = l_index = 0
    
    while(r_index < len(right) and l_index<len(left)):
        if left[l_index] <= right[r_index]:
            out.append(left[l_index])   
            l_index+=1
        else: 
            out.append(right[r_index])
            r_index+=1
    out.extend(left[l_index:])
    out.extend(right[r_index:])
    return out
            
if __name__ == '__main__':
    arr = np.random.randint(40, size=20)
    print('Unsorted array is :', arr)
    arr = merge_sort(arr)
    print('Sorted array is:', arr)