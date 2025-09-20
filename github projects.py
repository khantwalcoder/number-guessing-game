#number guessing game 
import random

number = random.randint(1, 100)

while True:
    guess = input("Guess a number between 1 and 100: ")
    guess = int(guess)

    if guess == number:
        print("You are right!")
        break
    elif guess > number:
        print("Your guess is high. Try again!")
    else:
        print("Your guess is low. Try again!")
