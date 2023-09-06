#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Get dataset to recreate Fig 3B from Lott et al 2011 PLoS Biology https://pubmed.gov/21346796
# wget https://github.com/bxlab/cmdb-quantbio/raw/main/assignments/lab/bulk_RNA-seq/extra_data/all_annotated.csv

transcripts = np.loadtxt( "/Users/cmdb/Downloads/Bootcamp_HW/Day2/all_annotated.csv", delimiter=",", usecols=0, dtype="<U30", skiprows=1 )
print( "transcripts: ", transcripts[0:5] )

samples = np.loadtxt( "/Users/cmdb/Downloads/Bootcamp_HW/Day2/all_annotated.csv", delimiter=",", max_rows=1, dtype="<U30" )[2:]
print( "samples: ", samples[0:5] )

data = np.loadtxt( "/Users/cmdb/Downloads/Bootcamp_HW/Day2/all_annotated.csv", delimiter=",", dtype=np.float32, skiprows=1, usecols=range(2, len(samples) + 2) )
print( "data: ", data[0:5, 0:5] )

# Find row with transcript of interest
for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row = i

for i in range(len(transcripts)):
    if transcripts[i] == 'FBtr0073461':
        row_m = i

# Find columns with samples of interest
cols = []
for i in range(len(samples)):
    if "female" in samples[i]:
        cols.append(i)

cols_m = []
for i in range(len(samples)):
    if "male" in samples[i] and "female" not in samples[i]:
        cols_m.append(i)

# Subset data of interest
expression = data[row, cols]
expression_m = data[row_m, cols_m]

# Prepare data
#x = samples[cols]
y = expression
y_m = expression_m


x = [10, 11, 12, 13, "14A","14B", "14C", "14D"]

# Plot data
fig, ax = plt.subplots()
ax.set_title("sisA(FBtr0073461) Female & Male")
ax.plot(x,y, c = "red")
ax.plot(x,y_m, c = "blue")
#ax.plot(x,y_m2, c = "light blue")
ax.set_xlabel("Developmental Stage")
ax.set_ylabel("mRNA Expression")
ax.set_ylim(0,250)

ax.legend()
plt.xticks(rotation = 90)
plt.tight_layout()
plt.show()


fig.savefig("FBtr0073461_addedMaleData.png")
plt.close(fig)