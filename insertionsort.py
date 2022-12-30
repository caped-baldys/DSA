'''insertion sort O(n2)'''


def insertion_sort(array):

    n = len(array)

    for i in range(1,n):

        key = array[i]

        j = i-1
        while (j>=0 and key < array[j]):
            #increase the postion of the current element by 1
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    return array


array = [12,1,23,12,3,2,7]
array = insertion_sort(array)
print(array)