# 33birthday.py by merdy 
import random 
import sys 

trials = int(sys.argv[1]) 
days = int(sys.argv[2])
people = int(sys.argv[3]) 

total = 0 
success = 0 
for trial in range(trials): 
    birthdays = []
    total += 1 
    c = 3
    for i in range(people): 
        date = random.randint(1, days)
        for number in birthdays[0:len(birthdays):]:        
            if date == number:
                if c == 3:
                    success += 1 
                c = 2
        birthdays.append(date) 


print(f'{(100 * success)/total}')
        
