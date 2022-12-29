# Python3 program for Fibonacci search.


# Returns index of x if present, else
# returns -1


def fibMonaccianSearch(arr, x, n):

	# Initialize fibonacci numbers
	fib0 = 0 # (m-2)'th Fibonacci No.
	fib1 = 1 # (m-1)'th Fibonacci No.
	fibM = fib0 + fib1 # m'th Fibonacci

	# fibM is going to store the smallest
	# Fibonacci Number greater than or equal to n
	while (fibM < n):
		fib0 = fib1
		fib1 = fibM
		fibM = fib0 + fib1

	# Marks the eliminated range from front
	offset = -1

	# while there are elements to be inspected.
	# Note that we compare arr[fib0] with x.
	# When fibM becomes 1, fib0 becomes 0
	while (fibM > 1):

		# Check if fib0 is a valid location
		i = min(offset+fib0, n-1)

		# If x is greater than the value at
		# index fib0, cut the subarray array
		# from offset to i
		if (arr[i] < x):
			fibM = fib1
			fib1 = fib0
			fib0 = fibM - fib1
			offset = i

		# If x is less than the value at
		# index fibMm2, cut the subarray
		# after i+1
		elif (arr[i] > x):
			fibM = fib0
			fib1 = fib1 - fib0
			fib0 = fibM - fib1

		# element found. return index
		else:
			return i

	# comparing the last element with x */
	if(fib1 and arr[n-1] == x):
		return n-1

	# element not found. return -1
	return -1


# Driver Code
arr = []
size =int(input('size of array'))

for i in range(size):
    temp = int(input(f'{i}:>'))
    arr.append(temp)

x = int(input('Enter the element:'))
n = len(arr)
#x = 235
ind = fibMonaccianSearch(arr, x, n)
if ind>=0:
    print("Found at index:",ind)
else:
    print(x,"isn't present in the array");

# This code is contributed by rishabh_jain
