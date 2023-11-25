# Week 9 November 17th

Exercise 2)
((number of genes that were significant in steps 1 and 2) / (number of genes that were significant in steps 1 or 2)) * 100%
30.427801353366213*


firstgenelist = []
for line in open("FINAL_table.txt"):
	genes = line.rstrip().split('\t')[0]
	firstgenelist.append(genes)
#print(firstgenelist)


des2genelist = []
for line1 in open("FINAL_table_deseq2.txt"):
	deseqGenes = line1.rstrip().split('\t')[0]
	des2genelist.append(deseqGenes)
#print(des2genelist)

firstgeneset = set(firstgenelist)
#print(firstgeneset)
des2genelistset = set(des2genelist)
#print(des2genelistset)

intersect = firstgeneset.intersection(des2genelistset)
#print(intersect)
jaccard_index = (len(intersect)/(len(firstgenelist)+len(des2genelist))) * 100
print(jaccard_index)
