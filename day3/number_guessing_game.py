#number guessing game
import random
NUM = random.randint(1,100)
attempt = 0
while True:
    guess = int(input("GUESS A NUMBER (1-100)= "))
    attempt+=1
    if guess>NUM:
        print("Too High..")
    elif guess<NUM:
        print("Too Low..")
    else:
        print("CORRECT..")
        break
print(" you guesss a nunmber in ",attempt," attempt(s).")