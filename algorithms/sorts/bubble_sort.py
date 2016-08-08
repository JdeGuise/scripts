#! /usr/bin/env python
import time

start_time = time.clock()

A = [2, 3, 4, 5, 6, 7, 8, 9, 10, 99]
A = [9, 3, 432, 7]
def bubble_sort(A):
	n = len(A)
	
	for passnumber in range(len(A)-1, 0, -1):
		for i in range(passnumber):
			if A[i] > A[i + 1]:
				# swap them, remember something changed.
				temp = A[i]
				A[i] = A[i + 1]
				A[i+1] = temp
	print(A)	

bubble_sort(A)

end_time = time.clock()

print "Sort took " + str((end_time - start_time)*1000) + " milliseconds."
