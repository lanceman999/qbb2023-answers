#!/usr/bin/env python

import os
import numpy as np
from fasta import readFASTA
import sys
import pandas as pd

# $ wget --content-disposition "https://www.dropbox.com/scl/fi/cq6mj7h34pnzkkabgz4ks/needleman-wunsch.tar.gz?rlkey=00wi3ypsfcfnml1psfyl7p9vu&dl=0"
# tar -zxvf needleman-wunsch.tar
# $ cd needleman-wunsch
# $ ../../../../cmdb-quantbio/resources/code/fasta.py


###################### 1.1 ############################################

input_sequences = readFASTA(open(sys.argv[1]))
scoring_matrix = sys.argv[2]
gap_penalty = float(sys.argv[3])
output_file = sys.argv[4]

#sequence1 = 'TACGATTA'
#sequence2 = 'ATTAACTTA'
seq1_id, sequence1 = input_sequences[0]
seq2_id, sequence2 = input_sequences[1]


###################### 1.2 ############################################

scoring_matrix = pd.DataFrame(pd.read_csv(scoring_matrix, sep = "\s+"))
#print(scoring_matrix)

# $ python HW3.py needleman-wunsch/CTCF_38_M27_AA.faa needleman-wunsch/BLOSUM62.txt  

F_matrix = np.zeros((len(sequence1)+1,len(sequence2)+1))
traceback_matrix = np.zeros((len(sequence1)+1,len(sequence2)+1), dtype = str)
#
for i in range(F_matrix.shape[0]): #or range(len(sequence1)+1)
    F_matrix[i,0] = i * gap_penalty
    traceback_matrix[i,0] = 'v'
    for j in range(F_matrix.shape[1]):
        F_matrix[0,j] = j * gap_penalty
        traceback_matrix[0,j] = 'h'

###################### 1.3 ############################################

for i in range(1, F_matrix.shape[0]): # starting at row_index 1 becuase the first row is already filled in
    for j in range(1, F_matrix.shape[1]):
        d = F_matrix[i-1,j-1] + float(scoring_matrix.loc[sequence1[i-1], sequence2[j-1]])
        h = F_matrix[i,j-1] + gap_penalty
        v = F_matrix[i-1,j] + gap_penalty

        F_matrix[i,j] = max(d,h,v)

        if F_matrix[i,j] == d:
            traceback_matrix[i,j] = 'd'
        elif F_matrix[i,j] == h:
            traceback_matrix[i,j] = 'h'
        else:
            traceback_matrix[i,j] = 'v'

print(F_matrix)
print(traceback_matrix)
print("Score of alignment: ", F_matrix[i,j]) # 3801 for AA; 
###################### 1.4 ############################################


align1 = ''
align2 = ''

while i != 0 or j != 0:
    if traceback_matrix[i,j] == 'd':
        align1 = sequence1[i-1] + align1
        align2 = sequence2[j-1] + align2
        i -= 1
        j -=1
    elif traceback_matrix[i,j] == 'h':
        align1 = '-' + align1
        align2 = sequence2[j-1] + align2
        j -= 1
    else: 
        align1 = sequence1[i-1] + align1
        align2 = '-' + align2
        i -= 1

#print(align1)
#print(align2)
print("Number of gaps in Sequence 1: ", align1.count('-'))
print("Number of gaps in Sequence 2: ", align2.count('-'))

###################### 1.5 ############################################

f = open(output_file, "w")
L = ["Sequence 1 alignment: ", align1,"\nSequence 2 alignment: ", align2]
f.writelines(L)
f.close()


# $ python HW3.py needleman-wunsch/CTCF_38_M27_AA.faa needleman-wunsch/BLOSUM62.txt -10 DNA_alignment.txt 
# $ python HW3.py needleman-wunsch/CTCF_38_M27_DNA.fna needleman-wunsch/HOXD70.txt -300 AA_alignment.txt


