#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt


fname = sys.argv[1]
read_depth = []
GenoQ = []
AlleleFreq = []
effects_list = []
for line in open(fname, 'r'):
    if line.startswith('#'):
        continue
    fields = line.rstrip('\n').split('\t')
    for i in fields[9:]:
        dp = i.split(':')[2]
        if dp == '.':
            continue
        else:
            read_depth.append(int(dp))
    for i in fields[9:]:
        gc = i.split(':')[1]
        if gc == '.':
            continue
        else:
            GenoQ.append(float(gc))
    for i in fields:
        i = fields[7].split(';')[3]
        af = i.split('=')[1]
        if "," in af:
            af_1 = af.split(",")[0]
            AlleleFreq.append(float(af_1))
        else:
            AlleleFreq.append(float(af))
    effects = fields[7].split('|')[1]
    if '&' in effects:
        effects_list.append(effects.split('&')[0])
        effects_list.append(effects.split('&')[1])
    else:
        effects_list.append(effects)

X = []
Counts = []
for i in set(effects_list):
    X.append(i)
    Counts.append(effects_list.count(i))
        
#print(len(read_depth))

#print(GenoQ)
#print(AlleleFreq)
#print(len(AlleleFreq))


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharey = False)
ax1.set_xlabel("Read Depth")
ax2.set_xlabel("Genotype Quality")
ax3.set_xlabel("Allele Frequency")
ax1.set_ylabel("Frequency")
ax2.set_ylabel("Frequency")
ax3.set_ylabel("Frequency")
ax4.set_ylabel("Frequency")
ax4.set_xlabel("Predicted Variant Effects")
ax1.set_xlim(0,100)
ax1.hist(read_depth, color = 'green', edgecolor = 'black', bins = 500)
ax2.hist(GenoQ, color = 'red', edgecolor = 'black')
ax3.hist(AlleleFreq, color = 'orange', edgecolor = 'black')
ax4.bar(range(len(X)), Counts, width = 0.8, align = 'center', edgecolor = 'black')
ax4.set_xticks(range(len(X)))
ax4.set_xticklabels(X, rotation = 'vertical', fontsize = 7)

fig.suptitle("Parsing VCF File")
plt.tight_layout()
plt.show()
plt.savefig('finalVCFsubplots.png')


# $ python HW5.py final.vcf

