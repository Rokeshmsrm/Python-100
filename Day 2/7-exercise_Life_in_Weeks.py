# Instructions

# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.

# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x weeks left.

# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input
# 56

# Example Output

# You have 1768 weeks left.

age = input()
Current_age_in_weeks = int(age) * 52.1775
total_years = 90
total_years_in_weeks = total_years * 52.1775
total_weeks = round(float(total_years_in_weeks)- float(Current_age_in_weeks))
print(f"You have {total_weeks} weeks left.")



#another method from udemy.

age = input()
# Your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")