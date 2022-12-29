#binary works on sorted array
#O(log n)
#divide conqure

size =int(input('size of array'))

list_a = [] 

for i in range(size):
    temp = int(input(f'{i}:>'))
    list_a.append(temp)

search = int(input('Enter the element:'))




def binarySearch(start, end, search):
    mid = int((start+end)/2)
    if(list_a[mid]== search):
        print('found at index :',mid)
        return
    elif(list_a[mid]>search):
        end = mid
        binarySearch(start, end,search)
    else:
        start = mid
        binarySearch(start, end,search)

start = 0
end = len(list_a)

binarySearch(start, end, search)


