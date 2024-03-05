#Multiple If syntax
#if condition1:
#   do A
#if condition2:
#   do B
#if condition3:
#    do C

# Copy day 3 3rd file and re-write the program according to multiple if syntax

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
    else:
        bill = 12
        print("Please pay $12.")
    wants_photo = input("Do you want a photo taken? Y or N.\n")
    if wants_photo == "Y":
        bill = bill + 3 # or bill += 3
    
    print(f"Your final bill is {bill}") #try indenting to check the changes
else:
    print("Sorry, you have to grow taller before you can ride.")