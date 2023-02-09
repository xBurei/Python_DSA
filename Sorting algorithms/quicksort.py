import numpy as np

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
        
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1    

def quicksort(arr, low, high):
    if low<high:
        splitIndex = partition(arr, low, high)
        
        quicksort(arr, low, splitIndex-1)
        
        quicksort(arr, splitIndex+1, high)
    
if __name__ == '__main__':
    array = np.random.randint(300, size=15)
    print('Unordered array is :', array)
    quicksort(array, 0, len(array)-1)
    print('Ordered array is :',array)