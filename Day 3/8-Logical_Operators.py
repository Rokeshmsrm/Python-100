# Syntax

# Logical Operators
# A and B   here both A and B should be True if any one is False then the whole statment is false! eg a=12, a > 10 and a < 13 hence it is true
# C or D    Here unlike And operator any one condition should be true for the statment to become true. Here either C can be true or D can be true.
# not E     It reverse the statement for example not a > 15 the terminal will give output as true.


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:                                   # We have used AND condition here!
        print("Everything is going to be ok. Have a free ride on us!") 
    else:
        bill = 12
        print("Please pay $12.")
    wants_photo = input("Do you want a photo taken? Y or N.\n")
    if wants_photo == "Y":
        bill = bill + 3 # or bill += 3
    
    print(f"Your final bill is {bill}") #try indenting to check the changes
else:
    print("Sorry, you have to grow taller before you can ride.")