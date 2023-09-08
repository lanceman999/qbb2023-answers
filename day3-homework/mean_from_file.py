#!/usr/bin/env python

import sys

def mean_int(filename):
	fname = open(filename, 'r') #fname is my_integers.txt"
	data = fname.readlines()
	print(data)
	int_list = []
	for i in data:
		i = i.rstrip("\n")
		int_list.append(int(i))
		total = sum(int_list)
		mean = total/len(data)
	return mean

print(mean_int(sys.argv[1])) # type "./mean_from_file.py my_integers.txt" into command line
