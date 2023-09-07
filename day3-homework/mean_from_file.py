#!/usr/bin/env python

import sys

fname = sys.argv[1] #fname is my_integers.txt"
data = open(fname).readlines()
#print(data)

def mean_int(a):
	int_list = []
	for i in data:
		i = i.rstrip("\n")
		int_list.append(int(i))
		total = sum(int_list)
		mean = total/len(a)
	return mean

print(mean_int(data))

# type "./mean_from_file.py my_integers.txt" into command line
