import os

#naive approach - O(n^2)
def findPair1(arr, n, sum):

	#consider each element but last
	for i in range(0,n-1):
		#start from element i til last element
		for j in range(i + 1,n):
			if arr[i] + arr[j] == sum:
				print(f"Pair found at index {i} and {j}.")
				return

	print("No pair found")


#apprach 2 - O(nlogn)
def findPair2(arr, n, sum):

	#sort array into ascending order
	arr = sorted(arr)
	print(f"Sorted array = {arr}")

	#hold and index for high and low
	low = 0
	high = n - 1

	#reduce search space [low..high] on each iteration
	#loop til low is greater than high
	while low < high:
		if arr[low] + arr [high] == sum:
			print(f"Pair found at index {low} and {high}.")
			return

		if arr[low] + arr[high] > sum:
			high -= 1
		else:
			low += 1
	print("No pair found")


#apprach 3 - O(n)
def findPair3(arr, sum):
	#create empty dictionary
	myMap = {}

	for i in range (0,n):
		#check if a pair (arr[i], sum - arr[i]) exists, if so, print pair
		if (sum - arr[i]) in myMap:
			index = myMap[sum-arr[i]]
			print(f"Pair found at index {index} and {i}")
			return

		#if it hasnt been seen before, put it in the dict
		myMap[arr[i]] = i

	print("Pair not found")

arr = [3,2,6,8,5,1]
sum = 4
n = len(arr)

print("Array =", arr)
print("Sum =", sum)

print("\nUsing apprach 1:")
findPair1(arr, n, sum)

print("\nUsing apprach 2:")
findPair2(arr,n,sum)

print("\nUsing apprach 3:")
findPair3(arr, sum)