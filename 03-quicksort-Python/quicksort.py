"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
	# Your code goes here
	if(len(array) == 1):
		return array
	low = 1
	high = len(array) - 1
	return partition(array,low,high)


def partition(array,low,high):
	if(len(array) == 1):
		return array
	if(low == high):
		return array
	pivot = 0
	while True:
		if(low >= high):
			temp = array[pivot]
			array[pivot] = array[low]
			array[low] = temp
			high = low - 1
			low = 1
			pivot = 0
			break
		if(array[low] < array[pivot]):
			low +=1
		if(array[high] > array[pivot]):
			high -= 1
		if(array[low] > array[pivot] > array[high]):
			temp = array[low]
			array[low] = array[high]
			array[high] = temp
			low =+ 1
			high -= 1
	return partition(array,low,high)