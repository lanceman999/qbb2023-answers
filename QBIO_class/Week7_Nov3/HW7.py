#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

# igv - double click on read - color alignment by - base modification (5mC)
# igv - double click on read - cluster - want 2

##### Question 3A ##### 
ONT = []
BI = []
for line in open("ONT.cpg.chr2.bedgraph"):
	col = line.rstrip().split()
	ONT.append(float(col[1]))

for line in open("bisulfite.cpg.chr2.bedgraph"):
	col = line.rstrip().split()
	BI.append(float(col[1]))


# Find reads that appear more than once in datasets
ONT_set = set()
for i in range(len(ONT)):
    if ONT[i] not in ONT_set:
        ONT_set.add(ONT[i])

BI_set = set()
for i in range(len(BI)):
    if BI[i] not in BI_set:
        BI_set.add(BI[i])

diff_ONT = ONT_set.difference(BI_set)
diff_BI = BI_set.difference(ONT_set)

BOTH = ONT_set.intersection(BI_set)

# Print statistics about unique vs multimapping reads
# print(f"ONT unique reads: {len(diff_ONT)} ({len(diff_ONT)/len(ONT) * 100})%")
# print(f"BI unique reads: {len(diff_BI)} ({len(diff_BI)/len(BI) * 100})%")
# print(f"Shared sites: {len(BOTH)} ({len(BOTH)/(len(BI)+len(ONT)) * 100})%")

ONT_coverage = []
BI_coverage = []
for line in open("ONT.cpg.chr2.bedgraph"):
	col = line.rstrip().split()
	ONT_coverage.append(float(col[4]))

for line in open("bisulfite.cpg.chr2.bedgraph"):
	col = line.rstrip().split()
	BI_coverage.append(float(col[4]))

fig, ax1= plt.subplots()
ax1.hist(ONT_coverage, bins = 2000, color = 'blue', alpha = 0.5, label = "ONT coverage")
ax1.set_xlabel("Read Coverage")
ax1.set_ylabel("Frequency (site)")
ax1.hist(BI_coverage, bins = 2000, color = 'green', alpha = 0.5, label = "BI coverage")
ax1.set_title("Coverage Distribution of ONT and Bisulfite Reads")
ax1.set_xlim(0,100)
ax1.legend()

fig.savefig("Read_coverage_for_BI_ONT.png")
fig.tight_layout()
#plt.show()

#### 3C ####

ONT_meth = []
BI_meth = []
for line in open("ONT.cpg.chr2.bedgraph"):
	col = line.rstrip().split()
	ONT_meth.append(float(col[3]))

for line in open("bisulfite.cpg.chr2.bedgraph"):
	col = line.rstrip().split()
	BI_meth.append(float(col[3]))

ONT_score = []
BI_score = []

for i in range(len(ONT)):
	if ONT[i] in BOTH:
		ONT_score.append(ONT_meth[i])

for j in range(len(BI)):
	if BI[j] in BOTH:
		BI_score.append(BI_meth[j])

correlation = np.corrcoef(ONT_score, BI_score)

fig = plt.figure()
plt.imshow(np.log10(1+ np.histogram2d(ONT_score, BI_score, bins =100)[0]))
plt.xlabel("ONT methylation score")
plt.ylabel("BI methylation score")
plt.title(f'Correlation of ONT and BI methylation scores (R= {correlation[0,1]:0.3f})')
plt.show()
fig.savefig("Correlation_meth_BI_ONT.png")
