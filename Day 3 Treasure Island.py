print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input("You arrive at a fork in the road. Do you go left or right? ")

if choice1.lower() == "left":
  choice2 = input("You stumble upon a lake with treacherous waters. Do you swim or wait? ")
  if choice2.lower() == "wait":
    choice3 = input("As you wait, a boat arrives and ferries you safely across the lake. As dusk settles, you stumble upon a building with 3 doors. Which do you take: red, blue, or yellow? ")
    if choice3.lower() == "red":
      print("A dangerous fire suddenly engulfs you. Game Over.")
    elif choice3.lower() == "blue":
      print("A gang of beasts jump through the darkness and maul you. Game Over.")
    elif choice3.lower() == "yellow":
      print("Congratulations! You've found the treasure!")
    else: 
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("As you swim across the waters, you are attacked by a giant trout. Game Over.")

else:
  print("The road suddenly curves into a sharp cliff. You slip and fall. Game Over.")    