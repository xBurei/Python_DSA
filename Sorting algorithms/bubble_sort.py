# Bubble sort implementation

print("Enter 2 or more values, stop the prompt by entering \'.\'")
val = None
arr = []
while(val != '.'):
    val = input("Enter a number or finish the prompt ")
    if val.isnumeric() : arr.append(int(val)) # Input sanitization

changes = 1
while(changes!=0):
    changes=0
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            changes+=1
    
    
print(arr)