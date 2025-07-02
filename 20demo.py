# 20demo.py by merdy 

t = 1, 2 # this is a tuple
print(t)
print(type(t))

person = 'Steve', 21, 57891.50 # name, age, yearly income
print(person)

def midpoint(x1, y1, x2, y2): 
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y 
   
print(midpoint(1, 2, 3, 4))
m = midpoint(1, 2, 3, 4)
mx, my = midpoint(1, 2, 3, 4)
print(mx, my)

print(m[0], m[1])

i = 0 
while True: 
    i = i + 1
    print('hey', i) 
    if i == 3: break
    
i = 1 
while i < 10: 
    print(i) 
    i = i + 3
print('the final value of i is', i)

for i in range(1, 10, 3): 
    print(i)
    
for i in range(0, 5): 
    print(i)
    
basket = 'milk', 'eggs', 'bread'
for thing in basket: 
    print(thing) 
    
for i in range(len(basket)): 
    print(basket[i])

for i in range(7): 
    if i % 2 == 0: print(i, 'is even') 
    else: print(i, 'is odd')
    
def triangular(n):             # triangular sum function
    sum = 0
    for i in range(n + 1): 
        sum = sum + i 
    return sum

print(triangular(4))

def factorial(n):              # factorial function
    fact = 1 
    for i in range(1, n + 1): 
        fact = fact * i 
    return fact

print(factorial(10))

def nchoosek(n, k):            # n chooose k function
    return factorial(n) / (factorial(k) * factorial(n-k))

print(nchoosek(6, 5))


def euler(iterations): 
    sum = 0
    for i in range(iterations): 
       sum = sum + (1/factorial(i))
    return sum
print(euler(10))

def is_prime(n): 
    for i in range(2, 11): 
        rem = n % i
        if rem == 0: return False 
    else: return True

print(is_prime(88))

def pi_estimate(iterations):              # Nilakantha series function
    pi = 3 
    for i in range(2, iterations, 4): 
        pi = pi + 4/ ((i)*(i+1)*(i+2)) 
        pi = pi - 4/ ((i+2)*(i+3)*(i+4))
    return pi 

import math
import random 

for i in range(5): 
    print(random.random())

for i in range(3): 
    print(random.randint(1, 6))

"""
inside = 0 
total = 0 
while True: 
    x = random.random()
    y = random.random()
    d = math.sqrt(x**2 + y**2)
    total += 1 
    if d < 1: inside += 1 
    print(inside/total)
    break
"""
    
total = 0     
iterations = 100000
for i in range(iterations + 1): 
    roll_1 = random.randint(1, 6)
    roll_1_alt = random.randint(1, 6)
    if roll_1_alt >= roll_1: roll_1 = roll_1_alt
    roll_2 = random.randint(1, 6)
    roll_2_alt = random.randint(1, 6)
    if roll_2_alt >= roll_2: roll_2 = roll_2_alt
    roll_3 = random.randint(1, 6)
    roll_3_alt = random.randint(1, 6)
    if roll_3_alt >= roll_3: roll_3 = roll_3_alt
    total += roll_1 + roll_2 + roll_3
print(total/iterations)
    
    