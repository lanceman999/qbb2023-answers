#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import sys


def simulate_coverage(coverage, genome_len, read_len, figname):
    coverage_arr = np.zeros(genome_len)
    num_reads = int(coverage * genome_len / read_len)
    low = 0
    high = genome_len - read_len
    start_positions = np.random.randint(low = 0, high = high+1, size = num_reads) #high value is exclusive
    for start in start_positions:
        coverage_arr[start: start+read_len] += 1
    
    x = np.arange(0, max(coverage_arr)+1)  #becuase ranges are exclusive
    
    sim_0cov = genome_len - np.count_nonzero(coverage_arr)
    print(f'In the simulation, there are {sim_0cov} bases with 0 coverage') ###### COOL TRICK!!!!!!!!

    sim_0cov_pct = 100 * (sim_0cov / genome_len)
    print(f'This is {sim_0cov_pct}% of the genome')

    # Get poisson distribution
    y_poisson = stats.poisson.pmf(x, mu = coverage) * genome_len

    # Get normal distribution
    y_normal = stats.norm.pdf(x, loc = coverage, scale = np.sqrt(coverage)) * genome_len #loc = mean and scale = std.dev

    fig, ax = plt.subplots()
    ax.hist(coverage_arr, bins = x, align = 'left', label = 'Simulation')
    ax.plot(x, y_poisson, label = 'Poisson')
    ax.plot(x, y_normal, label = 'Normal')
    ax.set_xlabel("Coverage")
    ax.set_ylabel("Frequency (bp)")
    fig.savefig(figname)
    fig.tight_layout()
    ax.legend()
    plt.show()

simulate_coverage(30,1000000,100, 'ex1_30x_cov.png')


reads = ['ATTCA', 'ATTGA', 'CATTG', 'CTTAT', 'GATTG', 'TATTT', 'TCATT', 'TCTTA', 'TGATT', 'TTATT', 'TTCAT', 'TTCTT', 'TTGAT']

graph = set()

k = 3

for read in reads:
    for i in range(len(read)-k):
        kmer1 = read[i: i+k]
        kmer2 = read[i+1: i+1+k]
        graph.add(f'{kmer1} -> {kmer2}')  # f line to execute command

print("digraph {")
for edge in graph:
	    print(edge)
print("}")

#with open('graph.txt', 'w') as file:
#    sys.stdout = file #redircting output to a file
#
#    print("digraph {")
#    for edge in graph:
#        print(edge)
#    print("}")
#sys.stdout = sys.__stdout__ #restoring std output

## conda create -n graphviz -c conda-forge graphviz
## conda activate graphviz

# dot -Tpng graph.txt > ex2_digraph.png





