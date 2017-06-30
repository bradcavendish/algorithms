import os

def insertionSort(array, n):
	#start from secnd element
	for i in range (1, n):

		value = array[i]
		j = i

		#find the index j within the sorted subset array[0..i-1]
		#where element array[i] belongs

		while (j > 0 and array[j-1] > value):
			array[j] = array[j-1]
			print(array)
			j -= 1
		
		array[j] = value
		print(array)



array = [2,1,6,4, 8, 10, 100, -24]
n = len(array)
print(array)
insertionSort(array, n)

print(array)