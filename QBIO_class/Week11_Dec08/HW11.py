#!/usr/bin/env python

import sys
import scanpy as sc
import numpy
import matplotlib.pyplot as plt

#### Exercise 1 ####

# Read the 10x dataset filtered down to just the highly-variable genes

adata = sc.read_h5ad("/Users/cmdb/qbb2023-answers/QBIO_class/Week11_Dec08/variable_data.h5")
adata.uns['log1p']['base'] = None # This is needed due to a bug in scanpy 

sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)

sc.tl.leiden(adata)

sc.tl.umap(adata,maxiter=900)

sc.tl.tsne(adata)

fig, (ax1,ax2) = plt.subplots(ncols=2)

sc.pl.umap(adata, color = 'leiden', show=False, title = 'UMAP', ax = ax1)
sc.pl.tsne(adata, color = 'leiden', show=False, title = 'TSNE', ax = ax2)

plt.tight_layout()
fig.savefig("UMAP_tsne.png")



#### Exercise 2 ####

wolcoxon_adata = sc.tl.rank_genes_groups(adata, groupby='leiden', key = 'wilcoxon', copy=True, use_raw=True)

logreg_adata = sc.tl.rank_genes_groups(adata, groupby='leiden', key = 'logreg', copy=True, use_raw=True)




sc.pl.rank_genes_groups(wolcoxon_adata, title = "Ranked via Wolcoxon", n_genes=25, show=False, use_raw=True, save="ranked_genes_wolcoxon.png")

sc.pl.rank_genes_groups(logreg_adata, title = "Ranked via Log-Regression", n_genes=25 ,show=False, use_raw=True, save="ranked_genes_logRegression.png")

#### Exercise 3 ####
leiden = adata.obs['leiden']
umap = adata.obsm['X_umap']
tsne = adata.obsm['X_tsne']
adata = sc.read_h5ad('filtered_data.h5')
adata.obs['leiden'] = leiden
adata.obsm['X_umap'] = umap
adata.obsm['X_tsne'] = tsne

adata.write('/Users/cmdb/qbb2023-answers/QBIO_class/Week11_Dec08/filtered_clustered_data.h5')





