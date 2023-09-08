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


results = fixation(0.3,300)

x = range(0,results[1])
y = results[0]

fig, ax = plt.subplots()
ax.plot(x,y, c = "red")
ax.set_xlabel("Generations")
ax.set_ylabel("Allele Frequency")
ax.set_title("Allele Freq over Time")
plt.show()