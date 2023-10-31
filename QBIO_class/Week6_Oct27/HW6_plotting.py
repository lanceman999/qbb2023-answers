#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

#### 1.1 ####

# $ plink --vcf genotypes.vcf --pca 10 --out PCA_genotypes - ASK DYLAN!

#### 1.2 ####

PCA1 = []
PCA2 = []

for line in open("PCA_genotypes.eigenvec"):
    lines = line.rstrip('\n').split()
   
    PCA1.append(float(lines[2]))
    PCA2.append(float(lines[3]))


fig,ax = plt.subplots()

ax.scatter(PCA1, PCA2, color = "red")
ax.set_xlabel("PCA1")
ax.set_ylabel("PCA2")
ax.set_title("GWAS")

plt.tight_layout()
plt.show()

fig.savefig("GWAS.png")


#### 2.1 ####

# $ plink --vcf genotypes.vcf --freq --out genotypes_AF

#### 2.2 ####
AF = []

with open("genotypes_AF.frq", 'r') as file:
    for line_num, line in enumerate(file):
        if line_num == 0:
            continue        
        col = line.rstrip('\n').split()
        AF.append(float(col[4]))

#print(AF)

fig,ax = plt.subplots()

ax.hist(AF, color = "red", edgecolor = 'black')
ax.set_xlabel("Allele Frequency")
ax.set_ylabel("Appearance Frequency")
ax.set_title("Allele Frequency from Genotype VCF File")

plt.tight_layout()
plt.show()

fig.savefig("AF.png")


#### 3.1 ####

# $ plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar PCA_genotypes.eigenvec --allow-no-sex --out CB1908_GWAS
# $ plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar PCA_genotypes.eigenvec --allow-no-sex --out GS451_GWAS

#### 3.2 ####
p_values_GS451 = []
chromosomes_GS451 = []
p_values_CB1908 = []
chromosomes_CB1908 = []
with open("GS451_GWAS.assoc.linear", 'r') as file:
    for line_num, line in enumerate(file):
        if line_num == 0:
            continue        
        col = line.rstrip('\n').split()
        if col[4] == "ADD":
            p_values_GS451.append(float(col[8]))
            chromosomes_GS451.append(int(col[0]))

with open("CB1908_GWAS.assoc.linear", 'r') as file:
    for line_num, line in enumerate(file):
        if line_num == 0:
            continue        
        col = line.rstrip('\n').split()
        if col[4] == "ADD":
            p_values_CB1908.append(float(col[8]))
            chromosomes_CB1908.append(int(col[0]))

#print(p_values_GS451)
p_values_final_GS451 = -1*np.log10(p_values_GS451)

#print(p_values_CB1908)
p_values_final_CB1908 = -1*np.log10(p_values_CB1908)

colors_GS451 = ['red' if p > 5 else 'gray' for p in p_values_final_GS451]
colors_CB1908 = ['red' if p > 5 else 'gray' for p in p_values_final_CB1908]

fig, (ax1,ax2) = plt.subplots(2,1, figsize = (10,8))

ax1.scatter(range(0,len(p_values_CB1908)), p_values_final_GS451, color = colors_GS451, s=10)
ax2.scatter(range(0,len(p_values_GS451)), p_values_final_CB1908, color = colors_CB1908, s=10)

ax1.axhline(y = 5, color='black', linestyle='--')
ax2.axhline(y = 5, color='black', linestyle='--')
ax1.set_title("GWAS of GS451")
ax2.set_title("GWAS of CB1908")
ax1.set_xlabel("SNP index")
ax2.set_xlabel("SNP index")
ax1.set_ylabel("-log10(p-value)")
ax2.set_ylabel("-log10(p-value)")
#ax1.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])
#ax2.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])

plt.tight_layout()
plt.show()

fig.savefig("Manhattan_plot.png")


#### 3.3 ####

pvalues_GS = []
smallest_GS = 1
SNP_GS = ''
with open("GS451_GWAS.assoc.linear", 'r') as file:
    for line_num, line in enumerate(file):
        if line_num == 0:
            continue        
        col = line.rstrip('\n').split()
        if col[4] == "ADD":
            pvalues_GS.append(float(col[8]))
            if float(col[8]) < smallest_GS:
                smallest_GS = float(col[8])
                SNP_GS = col[1]
        else:
            continue
print(SNP_GS)

pvalues_CB = []
smallest_CB = 1
SNP_CB = ''
with open("CB1908_GWAS.assoc.linear", 'r') as file:
    for line_num, line in enumerate(file):
        if line_num == 0:
            continue        
        col = line.rstrip('\n').split()
        if col[4] == "ADD":
            pvalues_CB.append(float(col[8]))
            if float(col[8]) < smallest_CB:
                smallest_CB = float(col[8])
                SNP_CB = col[1]
        else:
            continue
print(SNP_CB)

for line in open("genotypes.vcf",'r'):
    if line.startswith('#'):
        continue
    cols = line.rstrip().split()
    if cols[2] == SNP_CB:
        CB_genotype_info = (cols[9:])
#print(CB_genotype_info)
#print(len(CB_genotype_info))

zero_zero = []
zero_one = []
one_one = []
phenotype = []
for line in open("CB1908_IC50.txt", "r"):
    cols = line.rstrip().split()
    if cols[2] != 'CB1908_IC50':
        if cols[2] == "NA":
            phenotype.append("NA")
        else:
            phenotype.append(float(cols[2]))
    else:
        continue

#print(phenotype)

for i in range(0, len(CB_genotype_info)):
    if CB_genotype_info[i] == "0/0":
        zero_zero.append(phenotype[i])
    elif CB_genotype_info[i] == "0/1":
        zero_one.append(phenotype[i])
    elif CB_genotype_info[i] == "1/1":
        one_one.append(phenotype[i])

zero_zero_filtered = [item for item in zero_zero if item != "NA"]
zero_one_filtered = [item for item in zero_one if item != "NA"]
one_one_filtered = [item for item in one_one if item != "NA"]


alldata = []
alldata.append(zero_zero_filtered)
alldata.append(zero_one_filtered)
alldata.append(one_one_filtered)

x = ['0/0', '0/1', '1/1']

fig, ax = plt.subplots()

ax.boxplot(alldata, labels = x)
ax.set_xlabel('Genotypes')
ax.set_ylabel('Phenotype Values')
ax.set_title('Box Plot of Phenotypes per Genotypes for CB451 rs10876043')
fig.savefig("boxplot_PT_GT.png")
#plt.show()

