#!/usr/bin/env python

import sys

from Lecture_liveCoding import load_bedgraph, bin_array
import numpy
import scipy.stats
import matplotlib.pyplot as plt

### add keep dims argument for when working with count and frequency matrixes)

def main():
    # Load file names and fragment width
    forward_fname, reverse_fname, ctrl_fwd, ctrl_rev, frag_size, out_fname = sys.argv[1:]

    # Define what genomic region we want to analyze
    target = "chr2R"
    chromstart = 10000000
    chromend =   12000000
    chromlen = chromend - chromstart

    # Load the sample bedgraph data, reusing the function we already wrote    
    forward_sample = load_bedgraph(forward_fname, target, chromstart, chromend)
    reverse_sample = load_bedgraph(reverse_fname, target, chromstart, chromend) 

    # Load the control bedgraph data, reusing the function we already wrote
    forward_ctrl = load_bedgraph(ctrl_fwd, target, chromstart, chromend)
    reverse_ctrl = load_bedgraph(ctrl_rev, target, chromstart, chromend) 
   
    # Combine tag densities, shifting by our previously found fragment width
    frag_size = int(frag_size)
    combined_sample = numpy.zeros(chromlen, float)
    combined_sample[frag_size//2:] += forward_sample[:-frag_size//2]
    combined_sample[:-frag_size//2] += reverse_sample[frag_size//2:]

    # Combine tag densities for contol
    combined_ctrl = numpy.zeros(chromlen, float)
    combined_ctrl[frag_size//2:] += forward_ctrl[:-frag_size//2]
    combined_ctrl[:-frag_size//2] += reverse_ctrl[frag_size//2:]
    
    # Adjust the control to have the same coverage as our sample
    sample_coverage = numpy.sum(combined_sample)
    control_coverage = numpy.sum(combined_ctrl)
    adj_combined_ctrl = combined_ctrl * (sample_coverage/control_coverage)

    # Create a background mean using our previous binning function and a 1K window
    # Make sure to adjust to be the mean expected per base
    binsize = 1000
    global_score = bin_array(adj_combined_ctrl, binsize)/binsize

    # Find the mean tags/bp and make each background position the higher of the
    # the binned score and global background score
    mean_control_score = numpy.mean(adj_combined_ctrl)
    background_score = numpy.maximum(global_score, mean_control_score)

    # Score the sample using a binsize that is twice our fragment size
    # We can reuse the binning function we already wrote
    sample_score = bin_array(combined_sample, 2*frag_size)

    # Find the p-value for each position (you can pass a whole array of values
    # and and array of means). Use scipy.stats.poisson for the distribution.
    # Remeber that we're looking for the probability of seeing a value this large
    # or larger
    # Also, don't forget that your background is per base, while your sample is
    # per 2 * width bases. You'll need to adjust your background
    pValue_matrix =  1 - (scipy.stats.poisson.cdf(sample_score, (2*frag_size*background_score)))

    # Transform the p-values into -log10
    # You will also need to set a minimum pvalue so you doen't get a divide by
    # zero error. I suggest using 1e-250
    log_pValue_matrix = -(numpy.log10(pValue_matrix + 1e-250)) 

    # Write p-values to a wiggle file
    # The file should start with the line
    # "fixedStep chrom=CHROM start=CHROMSTART step=1 span=1" where CHROM and
    # CHROMSTART are filled in from your target genomic region. Then you have
    # one value per line (in this case, representing a value for each basepair).
    # Note that wiggle files start coordinates at 1, not zero, so add 1 to your
    # chromstart. Also, the file should end in the suffix ".wig"
    write_wiggle(log_pValue_matrix, target, chromstart, f"{out_fname}.wig")

    # Write bed file with non-overlapping peaks defined by high-scoring regions 
    write_bed(log_pValue_matrix, target, chromstart, chromend, frag_size, f"{out_fname}.bed")

###################################
# $ bedtools intersect -a sample1_analysis_output.bed -b sample2_analysis_output.bed > combined_peaks.bed
###################################

def write_wiggle(pvalues, chrom, chromstart, fname):
    output = open(fname, 'w')
    print(f"fixedStep chrom={chrom} start={chromstart + 1} step=1 span=1",
          file=output)
    for i in pvalues:
        print(i, file=output)
    output.close()

def write_bed(scores, chrom, chromstart, chromend, width, fname):
    chromlen = chromend - chromstart
    output = open(fname, 'w')
    while numpy.amax(scores) >= 10:
        pos = numpy.argmax(scores)
        start = pos
        while start > 0 and scores[start - 1] >= 10:
            start -= 1
        end = pos
        while end < chromlen - 1 and scores[end + 1] >= 10:
            end += 1
        end = min(chromlen, end + width - 1)
        print(f"{chrom}\t{start + chromstart}\t{end + chromstart}", file=output)
        scores[start:end] = 0
    output.close()


if __name__ == "__main__":
    main()