#!/usr/bin/env python

import numpy as np
import pandas as pd
from pydeseq2 import preprocessing
from matplotlib import pyplot as plt

# read in data
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)

# read in metadata
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

# normalize
counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]

# log
counts_df_logged = np.log2(counts_df_normed + 1)

# merge with metadata
full_design_df = pd.concat([counts_df_logged, metadata], axis=1)


#### Step 1.1 ####

data_df = full_design_df.loc['GTEX-113JC']
final_data_df_0 = data_df[data_df != 0]
final_data_df = final_data_df_0.iloc[:-3]

fig,ax = plt.subplots()

plt.hist(final_data_df, color = 'red', bins = 20)
ax.set_xlabel("Gene Expression (normalized & log) for GTEX-113JC")
ax.set_ylabel("Number of Genes")

plt.tight_layout()
plt.show()

fig.savefig("exercise_one_GTEX-113JC.png")

