# Bubble sort implementation

print("Enter 2 or more values, stop the prompt by entering \'.\'")
val = None
arr = []
while(val != '.'):
    val = input("Enter a number or finish the prompt ")
    if val.isnumeric() : arr.append(int(val)) # Input sanitization
    
i = 1 
while i<len(arr):
    j=i
    while j>0 and arr[j-1] > arr[j]:
        arr[j-1], arr[j] = arr[j], arr[j-1]
        j-=1
    i+=1
                
print(arr)
