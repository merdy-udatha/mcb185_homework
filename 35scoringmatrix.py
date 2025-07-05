# 35scoringmatrix.py by merdy 
import sys 

alphabet = sys.argv[1]
match = sys.argv[2]
mismatch = sys.argv[3]

print()
for char in alphabet: 
    print(f'\t{char}', end='')

for char in range(0, len(alphabet)): 
    print(f'\n\n{alphabet[char]}', end='')
    for nt in range(0, len(alphabet)):
        if alphabet[char] == alphabet[nt]: 
            print(f'\t{match}', end='', sep='   ')
        else: 
            print(f'\t{mismatch}', end='', sep='   ')
       
