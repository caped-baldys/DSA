# Selection sort in Python
# time complexity O(n*n)
#sorting by finding min_index

def selectionSort(arr,size):
    
    for i in range(size):

        min_index = i

        for j in range(i+1,size):
            if arr[j]<arr[min_index]:
                min_index = j
        #swaping to sort the array
        (arr[i],arr[min_index]) = (arr[min_index],arr[i])
    return arr


array = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(array)
array = selectionSort(array, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(array)
