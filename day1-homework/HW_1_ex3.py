#!/usr/bin/env python

f = open("inflammation-01.csv", "r")
lines = f.readlines()

### EXERCISE 3

average_min_max = []

int_list = []
for i in range(10):
	patient = lines[i].split(",")
	int_list = []
	for i in patient:
		i = int(i)
		int_list.append(i)	
	average_min_max.append(sum(int_list)/len(int_list))
print(max(average_min_max),min(average_min_max))

