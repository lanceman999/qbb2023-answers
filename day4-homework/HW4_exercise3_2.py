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

alleleFreq = []
avTimeFix = []
for i in range(10):
	rNumber = np.random.uniform(0,1)
	alleleFreq.append(rNumber)
	tfixation = []
	for i in range(50):
		results = fixation(rNumber,1000)
		tfixation.append(results[1])
	average = sum(tfixation) / len(tfixation)
	avTimeFix.append(average)

ax.scatter(alleleFreq, avTimeFix, c = 'red')
ax.set_xlabel("Allele Frequences")
ax.set_ylabel("Time to Fixation")
ax.set_xlim(0,1)
ax.set_title("Time to Fixation for Different Allele Frequencies")
fig.savefig("Exercise_3_2.png")
plt.show()