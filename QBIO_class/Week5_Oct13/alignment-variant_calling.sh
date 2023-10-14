#!/bin/bash

#### 1.1 ####
bwa index sacCer3.fa  -  ONLY DO ONCE

#### 1.2 ####
for sample in A01*.fastq
do
    echo "Aligning sample: " ${sample}
    bwa mem -t 4 -R "@RG\tID:${sample}\tSM:${sample}" \
        sacCer3.fa \
        ${sample} > ${sample}.SAM
done

#### 1.3 ####
for sample in A01*.SAM
do
    samtools sort ${sample} -O BAM -o ${sample}.BAM 
done

for sample in A01*.BAM
do
    samtools index ${sample} -b
done

#### 2.1 ####
mkdir BAM_files 
cp A01*.BAM BAM_files
ls BAM_files/*.BAM > BAM_list.txt
freebayes -p 1 -f sacCer3.fa -L BAM_list.txt --genotype-qualities --vcf all.vcf

#### 2.2 ####
mamba deactivate
brew install brewsci/bio/vcflib

vcffilter all.vcf -f "QUAL > 20" > filtered.vcf

#### 2.3 ####
vcfallelicprimitives filtered.vcf -k -g > decomposed.vcf

#### 2.4 ####
snpEff download R64-1-1.105

snpEff ann R64-1-1.105 decomposed.vcf  > final.vcf

head -n 100 final.vcf > sample_final.vcf