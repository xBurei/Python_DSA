# Selection sort implementation

print("Enter 2 or more values, stop the prompt by entering \'.\'")
val = None
arr = []
while(val != '.'):
    val = input("Enter a number or finish the prompt ")
    if val.isnumeric() : arr.append(int(val)) # Input sanitization
    
print('\nOriginal array is', arr, '\n')
for i in range(len(arr)):
    least = arr[i]
    index = i
    for x in range(i, len(arr)):
        current = arr[x]
        if current < least: 
            least = current
            index = x
    if least != arr[i]:
        print('Moving', arr[i], 'to index', index,'and', arr[index], 'to index', i)
        arr[index] = arr[i]
        arr[i] = least
        print('Current array is', arr, '\n')
        
print('Final array is',arr)