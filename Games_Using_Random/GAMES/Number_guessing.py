import random
num=random.randint(1,10)

while True:
    guess=int(input("Guess a number between 1-10:"))

    if guess==num:
        print("CONGRATS!!! YOUR GUESS WAS CORRECT!")
        break
    elif guess>num:
        print("The number you have guessed is too high!!")
        continue
    elif guess<num:
        print("The number you have guessed is too low!!") 
        continue