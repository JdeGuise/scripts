#! /usr/bin/env python

def recur_fact(root_factorial):
	if root_factorial == 1:
		return root_factorial

	else:
		result = root_factorial * recur_fact(root_factorial - 1)

	return result
recur_fact(10)
