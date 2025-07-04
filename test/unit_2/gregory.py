# gregory-leibniz series by merdy 

pi_over_4 = 1
counter = 1 
sign = 1 
while True: 
    counter += 2
    sign *= -1 
    pi_over_4 += sign/counter
    print(pi_over_4)