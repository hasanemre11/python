from logo import logo
import random

print(logo)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
dif = input("Choose difficulty. Type 'easy' or 'hard': ")

number = random.randint(1,101)

attempts = 0

if dif == "easy":
    attempts = 10
elif dif == "hard":
    attempts = 5


guess = 0

while attempts > 0 and guess != number:
    print(f"You have {attempts} attempts remaining to guess the number.")
    attempts += -1
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
    elif guess < number:
        print("Too low.")
        print("Guess again.")
    elif guess > number:
        print("Too high.")
        print("Guess again.")

if attempts == 0:
    print(f"You've run out of guesses, you lose. Answer was {number}.")