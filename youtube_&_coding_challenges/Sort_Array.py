arr = [5,2,7,8,1,4]
temp = 0

for i in range(0,len(arr)):
    for j in range(i+1, len(arr) ):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print('Array Sorted in assending order: ')

for i in range(0, len(arr)):
    print(arr[i], end= ' ')

