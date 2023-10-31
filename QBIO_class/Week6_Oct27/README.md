## QBIO Week 6

1.1) Compute genotype PCs

$ ~/bin/plink --vcf genotypes.vcf --pca 10 --out PCA_genotypes - ASK DYLAN!

2.1) Compute allele frequencies

$ plink --vcf genotypes.vcf --freq --out genotypes_AF

3.1) Running the GWAS
$ plink --vcf genotypes.vcf --linear --pheno CB1908_IC50.txt --covar PCA_genotypes.eigenvec --allow-no-sex --out CB1908_GWAS
$ plink --vcf genotypes.vcf --linear --pheno GS451_IC50.txt --covar PCA_genotypes.eigenvec --allow-no-sex --out GS451_GWAS

3.4) What gene could it be????
GS451: rs7257475
    Description: Homo sapiens cDNA FLJ44894 fis, clone BRAMY3000692, moderately similar to Zinc finger protein 91 - seems important!
CB1908: rs10876043
    Description: DIP2 disco-interacting protein 2 homolog B - involved in DNA methylation




