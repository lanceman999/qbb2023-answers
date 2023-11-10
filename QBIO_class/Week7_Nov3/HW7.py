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


#### 3D ####
#!/usr/bin/env python

ONT_norm = []
ONT_tumor = []
ONT_cov = []
ONT_tum_cov = []
ONT_score = []
ONT_tum_score = []

ontsite = []
ont1site = []
ontcoverage = []
ont1coverage = []
ontmeth = []
ont1meth = []

for line in open("normal.ONT.chr2.bedgraph"):
	col = line.rstrip().split()
	ONT_norm.append(float(col[1]))
	ONT_score.append(float(col[3]))
	ONT_cov.append(int(col[4]))

for line in open("tumor.ONT.chr2.bedgraph"):
	col = line.rstrip().split()
	ONT_tumor.append(float(col[1]))
	ONT_tum_score.append(float(col[3]))
	ONT_tum_cov.append(int(col[4]))

ONT_set = set()
for i in range(len(ONT_norm)):
    if ONT_norm[i] not in ONT_set:
        ONT_set.add(ONT_norm[i])


ONT_tum_set = set()
for i in range(len(ONT_tumor)):
    if ONT_tumor[i] not in ONT_tum_set:
        ONT_tum_set.add(ONT_tumor[i])

bothsite = ONT_set.intersection(ONT_tum_set)


ONT_meth_normal = []
ONT_meth_tum = []
for i in range(len(ONT_norm)):
	if ONT_norm[i] in bothsite:
		ONT_meth_normal.append(ONT_score[i])

for j in range(len(ONT_tumor)):
	if ONT_tumor[j] in bothsite:
		ONT_meth_tum.append(ONT_tum_score[j])

change_ONT = []
for i in range(len(ONT_meth_normal)):
	change = ONT_meth_normal[i] - ONT_meth_tum[i]
	if change != 0:
		change_ONT.append(change)


BI_norm = []
BI_tumor = []
BI_cov = []
BI_tum_cov = []
BI_score = []
BI_tum_score = []


for line in open("normal.bisulfite.chr2.bedgraph"):
	col = line.rstrip().split()
	BI_norm.append(float(col[1]))
	BI_score.append(float(col[3]))
	BI_cov.append(int(col[4]))

for line in open("tumor.bisulfite.chr2.bedgraph"):
	col = line.rstrip().split()
	BI_tumor.append(float(col[1]))
	BI_tum_score.append(float(col[3]))
	BI_tum_cov.append(int(col[4]))

BI_set = set()
for i in range(len(BI_norm)):
    if BI_norm[i] not in BI_set:
        BI_set.add(BI_norm[i])


BI_tum_set = set()
for i in range(len(BI_tumor)):
    if BI_tumor[i] not in BI_tum_set:
        BI_tum_set.add(BI_tumor[i])

bothsite = BI_set.intersection(BI_tum_set)

BI_meth_normal = []
BI_meth_tum = []
for i in range(len(BI_norm)):
	if BI_norm[i] in bothsite:
		BI_meth_normal.append(BI_score[i])

for j in range(len(BI_tumor)):
	if BI_tumor[j] in bothsite:
		BI_meth_tum.append(BI_tum_score[j])

change_BI = []
for i in range(len(BI_meth_normal)):
	change_BI_stuff = BI_meth_normal[i] - BI_meth_tum[i]
	if change_BI_stuff != 0:
		change_BI.append(change_BI_stuff)

fig, ax1= plt.subplots()
ax1.violinplot([change_ONT, change_BI])
ax1.set_xticks([1,2])
ax1.set_xticklabels(['ONT', 'Bisulfite'])
ax1.set_xlabel("Sequencing Type")
ax1.set_ylabel("Methylation Change")
ax1.set_title('Distribution of Methylation Changes')
fig.savefig("violin_plot.png") 
fig.tight_layout()
plt.show()
plt.close





