#! /usr/bin/env python
import time

A = [2, 3, 4, 5, 6, 7, 8, 9, 10, 99]
A = [3, 9, 432, 8]

start_time = time.clock()
def merge_sort(A):

	if len(A) > 1:
		mid = len(A) / 2
		left = A[:mid]
		right = A[mid:]
		
		merge_sort(left)
		merge_sort(right)

		i = 0
		j = 0
		k = 0

		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				A[k] = left[i]
				i += 1
			else:
				A[k] = right[j]
				j += 1
			k += 1

		while i < len(left):
			A[k] = left[i]
			i += 1
			k += 1
		
		while j < len(right):
			A[k] = right[j]
			j += 1
			k += 1
	print A
merge_sort(A)
end_time = time.clock()
print("Sorted list in " + str((end_time - start_time)*1000) + " milliseconds.")	
