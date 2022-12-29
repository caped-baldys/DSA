
size =int(input('size of array'))

#unsorted array 
list_a = [] 
#O(n)

for i in range(size):
    temp = int(input(':>'))
    list_a.append(temp)

search = int(input('Enter the element:'))

for i in range(len(list_a)):
    if list_a[i] == search:
        print('found at index ',i)
    