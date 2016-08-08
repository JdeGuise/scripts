#! /usr/bin/env python
import time
start_time = time.clock()
A = [2, 3, 4, 5, 6, 7, 8, 9, 10, 99]

def binary_search(A, item):
	f = 0
	l = len(A) - 1
	found = False

	while f <= l and not found:
		mid = (f + l) / 2
		if A[mid] == item:
			found = True
		else:
			if item < A[mid]:
				l = mid - 1
			else:
				f = mid + 1
	print "Was the item found?"
	print found
	return found

binary_search(A, 100)
end_1 = time.clock()

print str((end_1 - start_time) * 1000) + " milliseconds."
