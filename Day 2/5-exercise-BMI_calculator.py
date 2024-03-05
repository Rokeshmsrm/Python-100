# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# BMI Wikipedia Page

# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# BMI = weight(kg)/height^2 

# NOTE: You should convert the bmi to a whole number and print out
# a whole number in order to pass all the tests. See examples below.
# Example Input 1
# 1.75
# 80
# means: weight = 80 and height = 1.75

height = input()
weight = input()

h = float(height)
w = float(weight)

print(int(w / (h ** 2)))