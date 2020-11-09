# Contents 
* ***Python Library and Built-in Functions****
* ***What is pip and how do we use it?***
* ***API's with Python***


# Python Modules
Built in functions help us accelerate our development of software. 

# Task 1
1. Get user input as float
2. Check if number is lower than 0.5 and round to lower end.
3. Check if number is greater than 0.51, round up
```python
# Import the math library
import math
# Take user input 
user_input=input("Please enter you number: ")
# Idenitfy the number after the decimal using split. 
user_dec=float(user_input.split(".")[-1])
# Convert the user input to float 
user_num=float(user_input)
# If the number after the decimal is lower than 50, use floor to round down 
if user_dec<50:
    print(math.floor(user_num))
# Otherwise, round up using ceil() 
else:
    print(math.ceil(user_num))
```


# APIs in Python
