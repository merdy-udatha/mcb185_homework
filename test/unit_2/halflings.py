# halflfings.py by merdy (modified version of 25deathsaves.py) 
import random 


def deathsaves(): 
    iterations = 100
    total = 0 
    died = 0 
    stabilized = 0 
    revived = 0 
    for i in range(iterations): 
        failure = 0 
        stable = 0 
        status = False
        while status == False: 
            roll_1 = random.randint(1, 20)
            roll = random.randint(1, 20)
            if roll_1 > roll: roll = roll_1 
            if roll == 20: 
                revived += 1 
                total += 1 
                break 
            if roll == 1: 
                failure += 1             
            if roll < 10:    failure += 1 
            elif roll >= 10: stable += 1 
            if stable == 3: 
                status = True
                stabilized += 1 
                total += 1 
            if failure == 3: 
                status = True
                died += 1
                total += 1 
    return f"Died:{100 * died/total}%, Stabilized:{100 * stabilized/total}%, Revived:{100 * revived/total}%"

    
        
        
print(deathsaves())
    