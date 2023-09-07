#!/usr/bin/env python

list = [1,2,3,4,5]
def mean_int(a):
	sum = 0
	for i in a:
		sum += i
		mean = sum/len(a)
	return mean

print(mean_int(list))
