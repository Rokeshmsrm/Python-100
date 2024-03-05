#round function used to round up the value.

print(round((8/3)))
print(round(int(8/3)))

#if you want it to round up with two decimal point we can do this as shown in below

print(round(8/3, 2))
print(round(2.66666666, 2))

print(8//3) #here if we use two  '//' then this will give the answer as round value not a float value.

#use of operators

result = 4/2
result /= 2
print(result)

#another method

score = 0
#User score a point
score *= 1
score += 4
score /= 2

print(score)

#f-string concept
scores = 0
height = 1.8
isWinning = True

print(f"Your score is {scores}, your height is {height}, you are winning is {isWinning}.")