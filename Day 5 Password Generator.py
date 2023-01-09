#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
ez_password = []

for x in range(nr_letters):
  ez_password.append(random.choice(letters))

for y in range(nr_symbols):
  ez_password.append(random.choice(numbers))

for z in range(nr_numbers):
  ez_password.append(random.choice(symbols))

print(*ez_password, sep='')

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_password = []

for x in range(nr_letters):
  hard_password.append(random.choice(letters))

for y in range(nr_symbols):
  hard_password.append(random.choice(numbers))

for z in range(nr_numbers):
  hard_password.append(random.choice(symbols))

random.shuffle(hard_password)

password = ""
for char in hard_password:
  password += char

print(f"Your password is: {password}")
