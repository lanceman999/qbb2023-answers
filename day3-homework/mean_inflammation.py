#!/usr/bin/env python

import sys

def mean_inf(patient_id, filename = ""):
	f = open(filename, "r")
	lines = f.readlines()
	patient_line = lines[patient_id]
	line = patient_line.rstrip("\n")
	#print(line)
	line_list = line.split(",")
	#print(line_list)
	final = []
	for i in line_list:
		i = int(i)
		final.append(i)
	#print(final)
	mean = sum(final) / len(final)
	return mean

print(mean_inf(5, sys.argv[1]))
