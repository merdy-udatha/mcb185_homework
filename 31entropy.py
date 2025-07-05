# 31entropy.py by merdy 
import sys 
import math 

for arg in sys.argv[1:]: 
    if float(arg) == 0 or float(arg) == 1: 
        sys.exit('You entered invalid probabilities') 
        
total = 0 
for arg in sys.argv[1:]: 
    total += float(arg)
if math.isclose(total, 1.0) == False: 
    sys.exit('The probabilities you entered must add up to 1') 

h = 0 
for arg in sys.argv[1:]: 
    k = float(arg) 
    h -= k * math.log2(k) 

print(f'The total entropy is {h:.4f}') 
