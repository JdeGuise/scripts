#! /usr/bin/env python
import time
start_time = time.clock()

A = [10, 9, 8, 7, 6, 5, 4, 3, 2, 99]

def quick_sort(A):
	quick_sort_aligner(A, 0, len(A)-1)
	print A

def quick_sort_aligner(A, f, l):
	if f < l:
		split = partition(A, f, l)
		
		quick_sort_aligner(A, f, split-1)
		quick_sort_aligner(A, split+1, l)


def partition(A, f, l):
	pivot = A[f]    # pivot starts as first value
	
	left = f+1  # left barrier starts 1 after pivot
	right = l	# right barrier starts at end

	done = False
	while not done:
		while left <= right and A[left] <= pivot:  # while left_value < right_value AND A[left_value] <= the pivot value
			left += 1    # move left barrier right by 1

		while A[right] >= pivot and right >= left:   # while A[right_value] >= pivot AND right >= left
			right -= 1

		if right < left:
			done = True

		else:
			temp = A[left]
			A[left] = A[right]
			A[right] = temp

	temp = A[f]
	A[f] = A[right]
	A[right] = temp

	return right


quick_sort(A)

end_time = time.clock()
print str((end_time - start_time)*1000) + " milliseconds elapsed."
