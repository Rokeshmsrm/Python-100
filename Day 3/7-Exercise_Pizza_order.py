# Instructions
# Congratulations, you've got a job at Python Pizza! Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small pizza (S): S15
# Medium pizza (M): $20
# Large pizza (L): $25
# Add pepperoni for small pizza (Y or N): $2
# Add pepperoni for medium or large pizza (Y or N): $3
# Add extra cheese for any size pizza (Y or N): $1
# Example Input
# L
# Y
# N
# Example Output
# Thank you for choosing Python Pizza Deliveries !
# Your final bill is: $28.

pizza = input("Welcome! Place your oreder S or M or L?\n")
S = 15
M = 20
L = 25
bill = 0
# input("Add pepperoni for small pizza (y or N):\n")
# add_pep_M_or_L = input("Add pepperoni for medium or large pizza (y or N):\n")
add_pep_S = 2
add_pep_M_or_L = 3
add_extra_cheese = 1
if pizza == S:
    bill = 15
    print("You should pay 15.")
    want_pep_s = input("Want pepperoni for small pizza (Y or N):\n")
    bill += 2
    print(f"Your total is {bill}.")
elif pizza == M:
    bill = 20
    print("You should pay 20.")
else:
    bill = 25
    print("you should pay 25.")
