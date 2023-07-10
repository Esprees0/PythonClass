print("Hello Korn")
print("INE INET Class")

import random
S = random.randrange(1,100)
t = int(input("Let's try: "))

while True:
    
    if t == S :
        print("correct")
    elif t <= S :
        print("It's less")
    elif t >= S :
        print("It's to much")
    else :
        print("Wrong")