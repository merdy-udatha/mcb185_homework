# 36codon.py by merdy 

seq = 'ATGCTGTAA'

for i in range(0, len(seq) - 2): 
    codon = seq[i:i+3]
    print(i + 1,codon)