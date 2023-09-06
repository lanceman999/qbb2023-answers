#!/usr/bin/env python

f = open("inflammation-01.csv", "r")
lines = f.readlines()


### EXERCISE 1

patient_5 = lines[4].split(",")
print(patient_5)
print("first day:",patient_5[0])
print("10th day:", patient_5[9])
print("Last day:", patient_5[-1])
