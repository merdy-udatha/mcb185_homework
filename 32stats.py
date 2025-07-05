# 32stats.py by merdy 
import sys 
import math 

numbers = []
counter = 0 
for arg in sys.argv[1:]: 
    f = float(arg)
    numbers.append(f)
    counter +=1 
    
mini = numbers[0]
max = numbers[0]
sum = 0 
for n in numbers[:]: 
    if n < mini: mini = n 
    if n > max:  max  = n 
    sum += n 
    
mean = sum/counter
std = 0 
for n in numbers [:]: 
    std += (n - mean) ** 2

std /= counter 
final_std = math.sqrt(std)

def median(list):
    if counter % 2 == 0: 
        median = (list[(counter//2) - 1] + list[(counter//2)]) / 2
    else: median = numbers[counter // 2] 
    return median
    

print(f'You provided {counter} values')
print(f'The minimum value is {mini} and the maximum value is {max}') 
print(f'The mean value is {mean}')
print(f'The standard deviation is {final_std:.3f}') 
print(f'The median value is {median(numbers)}')