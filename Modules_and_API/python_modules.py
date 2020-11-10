import random
import math
# The random method is a python library which we can use for importing.
print(random.random()) # This will generate a float number between 0 and 1.

# We can use another method randint to get a random integer between a specified range, in this case 1 and 100
print(random.randint(1,100))

# We can also import the math library to make use of a method called the floor method which rounds down.
num_float = 23.24
# floor() method rounds down
print(math.floor(num_float)) #Prints 23
# ceil() method rounds up
print(math.ceil(num_float)) #Prints 24


# # TASK
# # get user input as float
# # check if number is lower than 0.5 and round to lower end
# # Check if number is greater than 0.51, round up
#
# # Import the math library
# import math
# # Take user input
# user_input=input("Please enter you number: ")
# # Identify the number after the decimal using split.
# user_dec=float(user_input.split(".")[-1])
# # Convert the user input to float
# user_num=float(user_input)
# # If the number after the decimal is lower than 50, use floor to round down
# if user_dec<50:
#     print(math.floor(user_num))
# # Otherwise, round up using ceil()
# else:
#     print(math.ceil(user_num))
#

# Pi method
print(math.pi) # Returns pi



# Can help us find out system configuration or system related information
# based on information provide,d we can handle user request.
import os
import math, datetime,sys

# # When we download something, we need path to create an environment variable so using ths command helps us idenitfy our current working directory.
# working_dir=os.getcwd() # see current path
# print(working_dir)
#
# # Lets find the name of our OS - This only works on linux and mac
# print(os.uname())
#
# # Lets count the number of CPUs in our system OS
# # To download, we have pre-requisites
# print(os.cpu_count()) # Returns 4
#
# # We have imported datetime
# # We can get the date and time of today using the command below.
# print(datetime.datetime.today())

# To find out the system path
# We can create a customised method and utilise the built in functionality at the same time.
# Why? Not everyone is technical, we need to explain in laymen terms exactly what they are looking at.
def current_system_path():
    print(" This is your current directory ")
    return sys.path

print(current_system_path())



