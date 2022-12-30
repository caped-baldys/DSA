'''O(n2)'''

array = [12,1,23,12,3,2,7]
n = len(array)
flag = -1
for i in range(n-1):

    for j in range(0,n-i-1):
        if array[j]>array[j+1]:
            #swaping
            array[j], array[j + 1] = array[j + 1], array[j]
            flag = 1
    if flag == -1:
        break

print(array)