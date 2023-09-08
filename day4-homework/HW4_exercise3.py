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

popsize = []
avTimeFix = []
for i in range(5):
	rNumber = np.random.randint(50,300)
	popsize.append(rNumber)
	tfixation = []
	for i in range(50):
		results = fixation(0.3,rNumber)
		tfixation.append(results[1])
	average = sum(tfixation) / len(tfixation)
	avTimeFix.append(average)
ax.scatter(popsize, avTimeFix, c = 'red')
ax.set_xlabel("Population Sizes")
ax.set_ylabel("Time to Fixation")
ax.set_xlim(50,300)
ax.set_title("Time to Fixation for Different Pop Sizes")
fig.savefig("Exercise_3_1.png")
plt.show()