# Lets have a look at some built in functions

# Import is the keyword we use to call modules from Python Libraries
# The random library is used for lucky draws and really just to generate random

import random
import math
# Inside the random library we have a function called random which we can execute.
# The random method is a python library which we can use for importing.
# Generate a float number between 0 and 1.
# print(random.random()) # This will print a random number
#
# # We can use another method randint to get a random integer between a specified range, in this case 1 and 100
# print(random.randint(1,100))
#
# # We can also import the math library to make use of a method called the floor method which rounds down.
# num_float = 23.24
# print(" floor method rounds the figure to lower end ")
# print(math.floor(num_float)) #Prints 23
# print("ceil() method rounds the figure up. ")
# print(math.ceil(num_float)) #Prints 24
#

# TASK
# get user input as float
# check if number is lower than 0.5 and round to lower end
# Check if number is greater than 0.51, round up

# Import the math library
import math
# Take user input
user_input=input("Please enter you number: ")
# Identify the number after the decimal using split.
user_dec=float(user_input.split(".")[-1])
# Convert the user input to float
user_num=float(user_input)
# If the number after the decimal is lower than 50, use floor to round down
if user_dec<50:
    print(math.floor(user_num))
# Otherwise, round up using ceil()
else:
    print(math.ceil(user_num))