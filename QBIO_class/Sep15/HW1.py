#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import scipy.stats as sps
import statsmodels.formula.api as smf
import statsmodels.api as sm

""" 
/Users/cmdb/qbb2023-answers/
ls -a
code .gitignore
(add *.csv)
"""
#can use "less -S FILENAME" to see sneakpeak of data

############################# 1.1 ######################################
df_DNM_0 = pd.read_csv("/Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_dnm.csv")
df_DNM = df_DNM_0.sort_values("Proband_id")
#print(df_DNM)

############################# 1.2 ######################################
q_df_DNM = df_DNM.groupby(['Proband_id','Phase_combined']).size().reset_index(name='Count')
print(q_df_DNM)

deNovoCount = {}
for i in range(0,len(q_df_DNM),2):
    deNovoCount[q_df_DNM.loc[i, "Proband_id"]] = [q_df_DNM.loc[i+1, "Count"],q_df_DNM.loc[i,"Count"]]
#print(deNovoCount)

############################# 1.3 ######################################
deNovoCountDF = pd.DataFrame.from_dict(deNovoCount, orient = 'index', columns = ['maternal_dnm', 'paternal_dnm'])
#print(deNovoCountDF)

############################# 1.4 ######################################
df_PA = pd.read_csv("/Users/cmdb/cmdb-quantbio/assignments/bootcamp/statistical_modeling/extra_data/aau1043_parental_age.csv", index_col = "Proband_id")
#print(df_PA)

############################# 1.5 ######################################
final_df = pd.concat([deNovoCountDF,df_PA], axis = 1, join = 'inner')
#print(final_df)

############################# 2.1 ######################################
fig, ax = plt.subplots()
ax.scatter(final_df['Mother_age'],final_df['maternal_dnm'], c = "blue")
ax.set_xlabel("Mother Age")
ax.set_ylabel("Maternal De Novo Mutations")
ax.set_title("Mothers age and mutations")
fig.savefig("ex2_a.png")
plt.show()


fig, ax = plt.subplots()
ax.scatter(final_df['Father_age'],final_df['paternal_dnm'], c = "red")
ax.set_xlabel("Father Age")
ax.set_ylabel("Paternal De Novo Mutations")
ax.set_title("Fathers age and mutations")
fig.savefig("ex2_b.png")
plt.show()

############################# 2.2 ######################################
model_mother = smf.ols(formula = "maternal_dnm ~ 1 + Mother_age", data = final_df)
results_m = model_mother.fit()
print(results_m.summary())
print(results_m.pvalues)


############################# 2.3 ######################################
model_father = smf.ols(formula = "paternal_dnm ~ 1 + Father_age", data = final_df)
results_f = model_father.fit()
print(results_f.summary())
print(results_f.pvalues)

############################# 2.4 ######################################

############################# 2.5 ######################################

#Shouldn't this be a bar graph? How do we visualize the corresponding DNMs for EACH proband?
fig, ax = plt.subplots()
ax.hist(q_df_DNM.loc[q_df_DNM['Phase_combined'] == 'father','Count'], bins = 20, label = "Father", alpha = 0.5) # 396 probands but they aren't evenly spaced because probands are not evenly ascending
ax.hist(q_df_DNM.loc[q_df_DNM['Phase_combined'] == 'mother','Count'], bins = 20, label = "Mother", alpha = 0.5)
ax.set_xlabel("DNMs")
ax.set_ylabel("Frequency")
ax.set_title("Number of DNMs per Probeband ID")
fig.savefig("ex2_c.png")
ax.legend()
plt.show()

############################# 2.6 ######################################
print(sps.ttest_ind(
q_df_DNM.loc[q_df_DNM['Phase_combined'] == 'father','Count'],
q_df_DNM.loc[q_df_DNM['Phase_combined'] == 'mother','Count']
))
#TtestResult(statistic=53.40356528726923, pvalue=2.198603179308129e-264, df=790.0)