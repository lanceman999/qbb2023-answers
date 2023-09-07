#!/usr/bin/env python

import sys

def infl_diff(patient_id1, patient_id2, filename = ""):
	f = open(filename, "r")
	lines = f.readlines()
	patient_line1 = lines[patient_id1]
	patient_line2 = lines[patient_id2]
	line1 = patient_line1.rstrip("\n")
	line2 = patient_line2.rstrip("\n")
	line_list1 = line1.split(",")
	line_list2 = line2.split(",")
	final_patient1 = []
	final_patient2 = []
	for i in line_list1:
		i = int(i)
		final_patient1.append(i)
	for i in line_list2:
		i = int(i)
		final_patient2.append(i)
	difference = []
	for i in range(40):
		difference.append(final_patient2[i] - final_patient1[i])	
	return difference

print(infl_diff(5, 6, sys.argv[1]))
