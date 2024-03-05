# len(4837)  #this lenght function doesn't work with the integer. It works only with the string
#TypeError: Object of type 'int' has no len()

num_char = len(input("What is your name?\n"))
# print("Your name has " + num_char + "charecters.") # end up in error saying can only concatenate str (not "int") to str

# print(type(num_char)) # type checking

#To make this work we can convert int to str which is called as type conversion # print("Your name has " + num_char + "charecters.")

new_num_char = str(num_char)
print("Your name has " + new_num_char + " charecters.")


#another method to find type function

a = float (123)
print(type(a))


