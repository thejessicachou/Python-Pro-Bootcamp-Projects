#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

EASY_MODE = 10
HARD_MODE = 5

def check_answer(user_guess, answer, turns):
    """Checks answer against user's guess. Returns the numbe rof turns remaining."""
    if user_guess == answer:
        print(f"You got it right! The answer was {answer}.")
    elif user_guess > answer:
        print("Too high")
        return turns - 1
    elif user_guess < answer:
        print("Too Low")       
        return turns - 1


def difficulty():
    level = input("Choose a difficult. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_MODE
    else:
        return HARD_MODE


def game():
    print(logo)
    answer = random.randint(1,100)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    turns = difficulty()

    user_guess = 0
    while user_guess != answer:
        print(f"You have {turns} attempts remaining to guess the numer.")

        #Letting the user guess the answer.
        user_guess = int(input("Enter your guess: ")) 
        
        #Track the number of turns and reduce by 1 if they get it incorrect
        turns = check_answer(user_guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses. You lose!")
            return
        elif user_guess != answer:
            print("Guess again.")


game()