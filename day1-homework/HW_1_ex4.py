#!/usr/bin/env python

f = open("inflammation-01.csv", "r")
lines = f.readlines()

### EXERCISE 4

patient_1 = lines[0].split(",")
patient_5 = lines[4].split(",")

difference = []
for i in range(len(patient_1)):
	diff = int(patient_5[i]) - int(patient_1[i])
	difference.append(diff)
print(difference)