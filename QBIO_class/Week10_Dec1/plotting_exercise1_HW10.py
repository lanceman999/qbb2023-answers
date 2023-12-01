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


#### Step 1.2 ####
final_data_male_df = full_design_df.loc[full_design_df['SEX']==1, 'MXD4']
final_data_female_df = full_design_df.loc[full_design_df['SEX']==2, 'MXD4']
print(final_data_male_df)

fig,ax = plt.subplots()

plt.hist(final_data_female_df, color = 'red', alpha = 0.5,  bins = 20, label = 'Female')
plt.hist(final_data_male_df, color = 'blue', alpha = 0.5, bins = 20, label = 'Male')
ax.set_xlabel("Gene Expression (logged normalized) for MXD4")
ax.set_ylabel("Number of Samples")
ax.legend()

plt.tight_layout()
plt.show()

fig.savefig("exercise_one_two_MXD4.png")


#### Step 1.3 ####

age_counts = full_design_df['AGE'].value_counts()

age_ranges = age_counts.index
counts = age_counts.values

fig,ax = plt.subplots()

plt.bar(age_ranges, counts, color = 'blue')
ax.set_xlabel("Age Range")
ax.set_ylabel("Number of Samples")

plt.tight_layout()
plt.show()

fig.savefig("age_counts.png")


#### Step 1.4 ####
male_df = full_design_df.loc[full_design_df['SEX']==1, ['LPXN', 'AGE']]
female_df = full_design_df.loc[full_design_df['SEX']==2, ['LPXN', 'AGE']]

median_expression_male = male_df.groupby('AGE')['LPXN'].median()
median_expression_female = female_df.groupby('AGE')['LPXN'].median()

age_ranges = median_expression_male.index


fig,ax = plt.subplots()

plt.plot(age_ranges, median_expression_male, color = 'green', label = 'Male')
plt.plot(age_ranges, median_expression_female, color = 'pink', label = 'Female')
ax.set_xlabel("Age Range")
ax.set_ylabel("Median expression of LPXN")
ax.legend()

plt.tight_layout()
plt.show()

fig.savefig("LPXN_age_sex_stuff.png")








