import os

def selectionSort(array, n):
	for i in range(0, n-1):
		#find minimum element in unsorted array[i..n-1]
		#and swap it with array[i]
		min = i

		for j in range(i + 1, n):
			#if array[j] is less then it is new minumum
			if array[j] < array[min]:
				min = j

		array[min], array[i] = array[i], array[min]
		print(array)



array = [2,1,6,4, 8, 10, 100, -24]
n = len(array)
print(array)
selectionSort(array, n)

