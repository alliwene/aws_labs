lower = 1
upper = 250 

for num in range(2, upper):
    # if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num) 
