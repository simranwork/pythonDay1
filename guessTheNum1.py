
#It is a random number guessing game
import random

def guess(x):
    randomNumber = random.randint(1,x)
    
    guess = 0

    while guess != randomNumber:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess > randomNumber:
            print("Sorry! You are guessing too high.")
        elif guess< randomNumber:
            print("Sorry! You are guessing too low.")
    print("Yayy! you guessed it right. ")        

guess(10)
