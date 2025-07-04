# fizzbuzz assessment by merdy: start 11:53 - 11:55

for i in range(101): 
    if i % 5 == 0 and i % 3 == 0: print('fizzbuzz')
    elif i % 3 == 0: print('Fizz')
    elif i % 5 == 0: print('Buzz')
    else: print(i)