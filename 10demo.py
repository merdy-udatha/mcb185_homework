# 10demo.py by merdy 
import math
print("hello, again") # greeting
print(1.5e-2)

print(math.factorial(10))
print(0.1 * 1)
print(0.1 * 3) 
a = 4 
b = 4
c = math.sqrt(a**2 + b**2)
print(c)
print(type(a), type(b), type(c), sep=', ', end=' !\n')

def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2) 
    return c 
    
hyp = pythagoras(3, 4)
print(hyp)

def square_area(b): return b**2
def circle_circum(r): return 2 * math.pi * r 
def sphere_volume(r): return (4/3) * math.pi * (r**3)

def is_even(x): 
    if x % 2 == 0: 
        return True
    return False 

print(is_even(2))
print(is_even(3))

c = a == b 
print(c)
print(type(c))

a = 0.3 
b = 0.1 * 3 
if   a < b: print('a < b') 
elif a > b: print('a > b')
else:       print('a == b')

diff = abs(a - b) 
if diff < 1e-9: print('close enough')
if math.isclose(a, b): print('is close enough')


def is_integer(x): 
    y = x % 2                       # y is the remainder
    if y != 1 and y != 0: 
        return False
    return True

print(is_integer(2))
print(is_integer(3))
print(is_integer(0.5))

def is_valid_prob(x):
    if x <= 1 and x >= 0: 
        return True
    return False

print(is_valid_prob(.5))

def nucleotide_pair(base):
    if   base == 'A': return 'T'
    elif base == 'T': return 'A'
    elif base == 'C': return 'G'
    elif base == 'G': return 'C'
    else: return
    
print(nucleotide_pair('R'))

def max_of3(a, b, c): 
    if   a > b and a > c: return a 
    elif b > a and b > c: return b 
    else: return c 
    
print(max_of3(1, 1289, 3))

def distance(a, b, c, d): 
    return math.sqrt((c - a)**2 + (d - b)**2)
    
print(distance(1, 2, 3, 4))