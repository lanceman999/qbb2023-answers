#!/usr/bin/env python

import numpy as np
import sys

#pwd: /Users/cmdb/qbb2023-answers/QBIO_class/Week8_Nov10/raw

#Rscript runChicago.R ./raw/PCHIC_Data/ ./ANALYSIS/ --design-dir ./raw/Design/ --en-feat-list ./raw/Features/ --export-format washU_test

baitfile, washU, output_name = sys.argv[1:4]

bait_dict = {}
for line in open(baitfile):
	cols = line.rstrip().split()
	bait_dict[str(cols[1]+','+cols[2])] = cols[4]

print(bait_dict)

frag1 = []
frag2 = []
interaction = []
for line in open(washU):
	cols = line.rstrip().split()
	frag1.append(cols[0])
	frag2.append(cols[1])
	interaction.append(float(cols[2]))

chrom = []
chromStart = []
chromEnd = []
name = []
score = []
value = []
exp = []
color = []
sourceChrom = []
sourceStart = []
sourceEnd = []
sourceName = []
sourceStrand = []
targetChrom = []
targetStart = []
targetEnd = []
targetName = []
targetStrand = []

for i in range(len(frag1)):
	chrom.append(frag1[i].split(',')[0])
	chromStart.append(min(int(frag1[i].split(',')[1]),int(frag1[i].split(',')[2]),int(frag2[i].split(',')[1]),int(frag2[i].split(',')[2])))
	chromEnd.append(max(int(frag1[i].split(',')[1]),int(frag1[i].split(',')[2]),int(frag2[i].split(',')[1]),int(frag2[i].split(',')[2])))
	name.append('.')
	score.append(int(interaction[i]/max(interaction)*1000))
	value.append(interaction[i])
	exp.append('.')
	color.append('0')
	if (frag1[i][6:] in bait_dict.keys()) and (frag2[i][6:] in bait_dict.keys()):
		sourceChrom.append(frag1[i].split(',')[0])
		sourceStart.append(int(frag1[i].split(',')[1]))
		sourceEnd.append(int(frag1[i].split(',')[2]))
		sourceName.append(bait_dict.get(frag1[i][6:]))
		sourceStrand.append('+')
		targetChrom.append(frag2[i].split(',')[0])
		targetStart.append(int(frag2[i].split(',')[1]))
		targetEnd.append(int(frag2[i].split(',')[2]))
		targetName.append(bait_dict.get(frag2[i][6:]))
		targetStrand.append('+')
	elif (frag1[i][6:] in bait_dict.keys()) and (frag2[i][6:] not in bait_dict.keys()):
		sourceChrom.append(frag1[i].split(',')[0])
		sourceStart.append(int(frag1[i].split(',')[1]))
		sourceEnd.append(int(frag1[i].split(',')[2]))
		sourceName.append(bait_dict.get(frag1[i][6:]))
		sourceStrand.append('+')
		targetChrom.append(frag2[i].split(',')[0])
		targetStart.append(int(frag2[i].split(',')[1]))
		targetEnd.append(int(frag2[i].split(',')[2]))
		targetName.append('.')
		targetStrand.append('-')
	elif (frag1[i][6:] not in bait_dict.keys()) and (frag2[i][6:] in bait_dict.keys()):
		sourceChrom.append(frag2[i].split(',')[0])
		sourceStart.append(int(frag2[i].split(',')[1]))
		sourceEnd.append(int(frag2[i].split(',')[2]))
		sourceName.append(bait_dict.get(frag2[i][6:]))
		sourceStrand.append('+')
		targetChrom.append(frag1[i].split(',')[0])
		targetStart.append(int(frag1[i].split(',')[1]))
		targetEnd.append(int(frag1[i].split(',')[2]))
		targetName.append('.')
		targetStrand.append('-')

YUP = [chrom,chromStart,chromEnd,name,score,value,exp,color,sourceChrom,sourceStart,sourceEnd,sourceName,sourceStrand,targetChrom,targetStart,targetEnd,targetName,targetStrand]

file = open(output_name, "w")

file.write('track type=interact name="pCHIC" description="Chromatin interactions" useScore=on maxHeightPixels=200:100:50 visibility=full\n')

for i in range(len(YUP[0])): 
	file.write("\t".join([str(y[i]) for y in YUP]) + "\n")

file.close()

# [chrom[x],chromStart[x],chromEnd[x],name[x],score[x],value[x],exp[x],color[x],sourceChrom[x],sourceStart[x],sourceEnd[x],sourceName[x],sourceStrand[x],targetChrom[x],targetStart[x],targetEnd[x],targetName[x],targetStrand[x]


# python washU_convert_bed_HW8.py /Users/cmdb/qbb2023-answers/QBIO_class/Week8_Nov10/raw/Design/h19_chr20and21.baitmap /Users/cmdb/qbb2023-answers/QBIO_class/Week8_Nov10/ANALYSIS/data/ANALYSIS_washU_text.txt /Users/cmdb/qbb2023-answers/QBIO_class/Week8_Nov10/BED_OUTPUT.bed