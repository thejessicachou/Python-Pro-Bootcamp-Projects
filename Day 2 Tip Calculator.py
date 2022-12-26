#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")

bill = input("What was the total bill? $")
tip = input("What percent tip would you like to leave? 10, 12, or 15? ")
group = input("How many people will split the bill? ")

split = round((float(bill) + (float(bill) * int(tip))/100)/int(group),2)

message = f"Each person should pay: ${split}"

print(message)