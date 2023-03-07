#Import artwork 
import random
from replit import clear
from game_data import data
from art import logo, vs

def format_data(account):
    """Format account data so it's in a printable format"""
    account_name = account["name"]
    account_desc = account["description"]
    account_country = account["country"]
    return f"{account_name}, a(n) {account_desc}, from {account_country}."

def check_answer(user_guess, a_followers,b_followers):
    """Use if statement to check if user is correct"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

#Display Art
print(logo)
score = 0
should_continue = True
account_b = random.choice(data)

#Make the game repeatable
while should_continue:
    #Generate random choices from the data
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    
    
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")
    
     #Ask user for a guess
    user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    #Check if user is correct
    
    ##Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(user_guess, a_follower_count, b_follower_count)

    #Clear the screen between rounds.
    clear()
    print(logo)
    
    #Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        should_continue = False
        print(f"Sorry, you're wrong. Final score: {score}")

    
 
