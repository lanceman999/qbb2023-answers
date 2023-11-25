#!/usr/bin/env python

import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
# from statsmodels.stats import multitest
from statsmodels.stats.multitest import fdrcorrection
from pydeseq2 import preprocessing
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats
import csv
import matplotlib.pyplot as plt


### Exercise 1 ###
counts_df = pd.read_csv("gtex_whole_blood_counts_formatted.txt", index_col = 0)
metadata = pd.read_csv("gtex_metadata.txt", index_col = 0)

counts_df_normed = preprocessing.deseq2_norm(counts_df)[0]
counts_df_normed = np.log2(counts_df_normed + 1)
full_design_df = pd.concat([counts_df_normed, metadata], axis=1)

model = smf.ols(formula = 'Q("DDX11L1") ~ SEX', data=full_design_df) # don't care about the intercept. Not DE, p-value of 0.28, coef is slope
results = model.fit()

slope = results.params[1]
pval = results.pvalues[1]

output_file = "./DE_results.csv"
with open(output_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Gene', 'Coefficient(Slope)', 'P-Value'])
    
    de_results = {}
    for gene in counts_df_normed.columns:
        formula = f'Q("{gene}") ~ SEX'  # Replace SEX with your relevant grouping variable

        model = smf.ols(formula=formula, data=full_design_df)
        results = model.fit()

        writer.writerow([gene, results.params['SEX'], results.pvalues['SEX']])


final_table = pd.read_csv("DE_results.csv", index_col = 0)
final_table['P-Value'] = final_table['P-Value'].fillna(1.0)
final_table['Q-Value'] = fdrcorrection(final_table['P-Value'], method='indep', alpha=0.1)[1]

final_table.to_csv("./FINAL_table.csv")
# ls -1 | wc -l FINAL_table.csv
# 54593 rows (# of genes)


# Exercise 2
dds = DeseqDataSet(
    counts=counts_df,
    metadata=metadata,
    design_factors="SEX",
    n_cpus=4,
)

dds.deseq2()
stat_res = DeseqStats(dds)
stat_res.summary()
results = stat_res.results_df
results_FINAL = results.dropna(subset=['padj'])
#print(len(results_FINAL))
# 23877 rows (number of genes)

jaccard_index = ((54593 + (len(results_FINAL))) / (len(results_FINAL))) * 100
print(jaccard_index)


# Exercise 3 

fig,ax = plt.subplots()

log2FoldChange = results_FINAL['log2FoldChange']
p_values = results_FINAL['pvalue']
padj_values = results_FINAL['padj']

negLog10Pvalue = -1 * (np.log10(p_values))
DEGs = (padj_values < 0.1) & (abs(log2FoldChange) > 1)

plt.scatter(log2FoldChange, negLog10Pvalue, color='grey', alpha=0.5, label='Not DE')
plt.scatter(log2FoldChange[DEGs], negLog10Pvalue[DEGs], color='red', alpha=0.7, label='DEGs')
ax.set_xlabel("Log2FC")
ax.set_ylabel("-log10 (P-Value)")
ax.set_title("DEGs Volcano Plot")

plt.tight_layout()
plt.show()

fig.savefig("volcano_plot.png")
