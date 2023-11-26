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

2.2 (1))
chr20	44438565	44565593	.	1000	34.77	.	0	chr20	44562442	44565593	PCIF1	+	chr20	44438565	44442365	UBE2C	+
chr20	44438565	44607204	.	986	34.29	.	0	chr20	44596299	44607204	FTLP1;ZNF335	+	chr20	44438565	44442365	UBE2C	+
chr21	26837918	26939577	.	978	34.02	.	0	chr21	26837918	26842640	snoU13	+	chr21	26926437	26939577	MIR155HG	+
chr20	44452862	44565593	.	974	33.89	.	0	chr20	44562442	44565593	PCIF1	+	chr20	44452862	44471524	SNX21;TNNC2	+
chr20	17660712	17951709	.	973	33.85	.	0	chr20	17946510	17951709	MGME1;SNX5	+	chr20	17660712	17672229	RRBP1	+
chr20	24972345	25043735	.	973	33.84	.	0	chr20	24972345	24985047	APMAP	+	chr20	25036380	25043735	ACSS1	+

2.2 (2))
chr21	26797667	26939577	.	952	33.13	.	0	chr21	26926437	26939577	MIR155HG	+	chr21	26797667	26799364	.	-
chr20	55957140	56074932	.	928	32.29	.	0	chr20	55957140	55973022	RBM38;RP4-800J21.3	+	chr20	56067414	56074932	.	-
chr21	26790966	26939577	.	838	29.17	.	0	chr21	26926437	26939577	MIR155HG	+	chr21	26790966	26793953	.	-
chr20	5585992	5628028	.	830	28.88	.	0	chr20	5585992	5601172	GPCPD1	+	chr20	5625693	5628028	.	-
chr21	26793954	26939577	.	754	26.23	.	0	chr21	26926437	26939577	MIR155HG	+	chr21	26793954	26795680	.	-
chr20	5515866	5933156	.	750	26.08	.	0	chr20	5929472	5933156	MCM8;TRMT6	+	chr20	5515866	5523933	.	-

2.3) Does it make sense for this gene to be interacting with enhancers in GM12878? Explain.
glycerophosphocholine phosphodiesterase 1: Predicted to be involved in glycerophospholipid catabolic process. Predicted to act upstream of or within skeletal muscle tissue development. Predicted to be located in cytosol

Highly expressed in bone marrow, spleen, and lungs (highest in bone marrow). This makes sense as B-cells are produced in the bone marrow and GM12878 is a B-cell line.

