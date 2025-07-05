# 34birthday.py by merdy 
import random 
import sys 

trials = int(sys.argv[1]) 
days = int(sys.argv[2]) 
people = int(sys.argv[3]) 

success = 0 
total = 0 

for trial in range(trials): 
    total += 1 
    calendar = []
    for day in range(1, days): 
        calendar.append(day)

    for person in range(people): 
        birthday = random.randint(1, days)
        calendar[birthday] += 1
        
    for i, date in enumerate(calendar): 
        if date - (i + 1) == 2: 
            print('Happy Birthday to both of you!!!!')
            success += 1 
        else: print(i + 1 , date)
        
print(success/total)