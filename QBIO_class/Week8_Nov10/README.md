# Week 8 November 10th

1.1)

pwd: /Users/cmdb/qbb2023-answers/QBIO_class/Week8_Nov10/raw

Rscript runChicago.R --design-dir ./raw/Design/ --en-feat-list ./raw/Features/featuresGM.txt --export-format washU_text ./raw/PCHIC_Data/GM_rep1.chinput,./raw/PCHIC_Data/GM_rep2.chinput,./raw/PCHIC_Data/GM_rep3.chinput ./ANALYSIS

1.2)
Do these enrichments make sense to you? Are any surprising? Explain your reasoning briefly for each feature.
Yes for the most part, all of the targets are much more enriched than the nubmer due to random chance. 
CTCF: This doesn't make a lot of sense as CTCF are TAD boundaries so I don't know why they would be enriched
H3K4me1: It would make sense for their to be more interaction at H3K4me1 when compared to enrichment due to random chance if the gene is epxressed
H3K4me3: It would make sense for their to be more interaction at H3k4me3 when compared to enrichment due to random chance if the gene is expressed
H3k27me3c: This would make snese in accordance to the other data 
H3K9me3: THIS DOESN"T MAKE SENSE! Why would constitutive chromatin be enriched at an active gene.....?

