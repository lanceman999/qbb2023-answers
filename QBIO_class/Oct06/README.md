QBIO October 6th Class:
# STEP 2:
1)What fraction of peaks were retained when intersected compared to sample1? Sample2?
$ wc -l combined_peaks.bed

172 intersecting peaks in combined  
181 peaks in sample1
193 peaks in smaple2

# STEP 3:
1) How reproducible are the peaks called between the two samples? Is the p-value range of a peak indicative of reproducibility? Is it completely consistent?
Decently reporoducible as most of the peaks for sample 1 and 2 are present in refernce to the refseq peaks. And p-value is indicative of reproducability as the p-value corresponds to the probability of obtaining a result due to random chance. Therefore, a low p-value corresponding with an output means that there is a very low chance of obtaining said result due to random chance. It is not completely consistent as not all of the peaks are exactly the same, as quantified in step 2, and as shown in the igv image, even for those with a low p-value.