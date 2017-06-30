import os

def bubbleSort(array, n):

	for i in range(0, n-1):

		#last i items are in order, inner loop doesnt need to look at them
		for j in range(0,n-1-i):
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
				print(array)



array = [2,1,6,4, 8, 10, 100, -24]
n = len(array)
print(array)
bubbleSort(array, n)