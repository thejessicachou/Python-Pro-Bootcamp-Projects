rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

rps = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice >= 0 and user_choice < 3:
  print("You chose:" + rps[user_choice])
else:  
  print("You chose: Invalid choice!")

computer_choice = random.randint(0,2)

if computer_choice == 0:
  print("Computer chose:" + rock)
elif computer_choice == 1:
  print("Computer chose:" + paper)
elif computer_choice == 2:
  print("Computer chose:" + scissors)

if user_choice == computer_choice:
  print("Draw!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice > user_choice:
  print("You lose!")
elif user_choice > 2 or user_choice < 0:
  print("You entered an invalid number. You lose!")
else: 
  print("You win!")
