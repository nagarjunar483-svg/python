import random
num=random.randint(1,50)
while True:
    guess = int(input("enter number:"))
    if guess==num:
        print("guessed it")
        break
    elif guess<num:
        print("low")
    else:
        print("high")
