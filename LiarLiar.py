# uhm...
import random

# a3 is necessarilly true
# a2, d1 and d3 determine the convict 

def only_one(a2, d1, d3):
    """checks how many of the arguements are "true"
    Note: only one of the arguements can be logically true
    """
    Ts = 0
    for i in [a2, d1, d3]:
        if i == 1:
            Ts +=1

    if Ts <= 1:
        return True
    else:
        return False

# 1s are True and -1s are False
def logic(a2, d1, d3):
    b3 = -a2
    c2 = -a2
    b1 = -d1
    b2 = -d3

    c3 = d1
    d2 = -c3
    
    a1 = a2
    c1 = -a1

    Ts = 0
    Fs = 0
    for i in [a1, a2, b1, b2, b3, c1, c2, c3, d1, d2, d3]:
        if i == 1:
            Ts += 1
        elif i == -1:
            Fs += 1

    if Ts == 5 and Fs == 6:
        return True

while True:
    a2 = random.choice([-1, 1])
    d1 = random.choice([-1, 1])
    d3 = random.choice([-1, 1])
    
    if only_one(a2, d1, d3):
        a3 = logic(a2, d1, d3)

        if a3 == True:
            if a2 == 1:
                print("B is the thief")     
            elif d1 == 1:
                print("D is the thief")   
            elif d3 == 1:
                print("A is the thief")    
            else:
                print("C is the thief") 
            
            break