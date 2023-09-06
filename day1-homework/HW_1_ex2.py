#!/usr/bin/env python

f = open("inflammation-01.csv", "r")
lines = f.readlines()

### EXERCISE 2
average_list = []

for i in range(60):
  patient = lines[i].split(",")
  int_list = []
  for i in patient:
  	i = int(i)
  	int_list.append(i)	
  average_list.append(sum(int_list)/len(int_list))

print(average_list[0:10])