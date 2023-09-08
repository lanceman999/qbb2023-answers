#!/usr/bin/env python

import numpy as np 
import matplotlib.pyplot as plt

def fixation(AF,pop):
	
	AF_time = []

	while 0 < AF < 1:
		success = np.random.binomial(2*pop, AF)
		AF = success / (2*pop)
		AF_time.append(AF)

	num_gen = len(AF_time)
	return [AF_time, num_gen]

fig, ax = plt.subplots()
tfixation = []
for i in range(1002):
	results = fixation(0.3,700)
	tfixation.append(results[1])

ax.hist(tfixation)
ax.set_xlabel("Generations to Fixation for Wright Fisher Model")
ax.set_ylabel("Allele Frequency")
ax.set_title("Occurance")
fig.savefig("Exercise_2_2.png")
plt.show()
