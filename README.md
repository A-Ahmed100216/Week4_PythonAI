# Contents 
* ***Python Library and Built-in Functions****
* ***What is pip and how do we use it?***
* ***API's with Python***


# Python Modules
* Built in functions which help us accelerate our development of software. 
* We access and use libraries by importing them in. 
* Import is the keyword we use to call modules from Python Libraries.

* Syntax: 
```python
import <library_name>
``` 
* For example
```python
import math
```
* We can also import specific modules within a library
``` from <library_name> import <module_name>```
  * For example:
```python
from random import random
```
## Python Libraries
1. ```random```
  * The ```random``` library is typically used when we need a fair way to generate random variables, whether that is integers, strings etc. 
  * A typical use case would be lottery numbers.
```python
import random
# Inside the random library we have a function called random which we can execute.
print(random.random()) # This will print a random number

# We can use another method randint to get a random integer between a specified range, in this case 1 and 100
print(random.randint(1,100))
 ```

2. ```math```
* We can also import the math library to make use of a method called the floor method which rounds down.
```python

import math

num_float = 23.24
print(" floor method rounds the figure to lower end ")
print(math.floor(num_float)) #Prints 23
print("ceil() method rounds the figure up. ")
print(math.ceil(num_float)) #Prints 24
```
* Within math, we also have ```pi``` which as the name suggests, return the value of pi.
```python
print(math.pi) # Returns pi
```

# Task 1
1. Get user input as float
2. Check if number is lower than 0.5 and round to lower end.
3. Check if number is greater than 0.51, round up
```python
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
```

## System-Based Libraries
* These can help us find out our system configuration or system related information.
* Based on information provided, we can handle user request.
* To access this information, we import the ```os``` and ```sys``` libraries.
* We also import datetime and math as these will be used in the examples. 
```python
import os
import math, datetime,sys
```

### Example Methods
1. Working Directory - When we download something, we need path to create an environment variable so using ths command helps us identify our current working directory.
```python
# working_dir=os.getcwd() # see current path
# print(working_dir)
```

2. OS - Find the name of our operating system. NB: This only works on Linux and Mac
```python
print(os.uname())
```
3. 
```python

#
# # Lets count the number of CPUs in our system OS
# # To download, we have pre-requisites
# print(os.cpu_count()) # Returns 4
#
# # We have imported datetime
# # We can get the date and time of today using the command below.
# print(datetime.datetime.today())
```




* To find out the system path.
* We can create a customised method and utilise the built in functionality at the same time.
* Why? Not everyone is technical, we need to explain in laymen terms exactly what they are looking at. 
```python
      def current_system_path():
            print(" This is your current directory ")   
            return sys.path                                               
print(current_system_path())  
```











# APIs in Python          
* Application Programming Interface     
* Packages help us use the code internally, connect to web APIs. APIs provide us with a connection interfaces.  
![API Diagram](/API%20diagram.png)
## What is pip
* Package manager for Python.
* We use it to install external packages such as requests. 
* syntax: ```pip install <name_of_package>```

# Request
An example of a package we can install is the requests package. This enables us to scrape live data from a website.
```python

import requests
from emoji import emojize

live_response=requests.get("https://www.bbc.co.uk/")
print(live_response.status_code)  
```
* This will return an integer as the response code.
* 200 tells us that the website is live and working.
* 404 tells us that the website is not working. 
* Many more status codes exist but these can easily be looked up. 
* We can use an if statement to add more detail and tell the user what the 200 means.
* Note, the emoji package has also been installed and imported. This allows us to use emojis. 
```python
if live_response.status_code==200:
    print("This website is live. Status code: " + str(live_response.status_code) + emojize((" :thumbs_up:")))
else:
    print("Ooops something went wrong, please try later")
```

## Implement DRY
* A key principle of Python is Don't Repeat Yourself. Therefore we can create a function to store the above code. This simply entails encapsulating the block of code in a a def statement:
```python
def check_response_code():
    if live_response.status_code==200:
        print("This website is live. Status code: " + str(live_response.status_code) + emojize(" :thumbs_up:"))
    elif live_response.status_code==404:
        print(" This site is unavailable until further notice. Please contact support")
    else:
        print("Oops something went wrong, please try later")
 
# This is a function so it needs to be called. 
check_response_code()
```

## Why use the requests library?
In the status code example, we can get rid of the numbers and the code will still run.
* This is because the requests module is designed such that it will evaluate to **True if the status code is between 200-400**, otherwise False. 
* This is the built in functionality provided within the requests library.
```python
# Why do we use the requests module?
def check_response_code():
    if live_response.status_code:
        print("This website is live. Status code: " + str(live_response.status_code) + emojize(" :thumbs_up:"))
    elif live_response.status_code:
        print(" This site is unavailable until further notice. Please contact support")
    else:
        print("Oops something went wrong, please try later")
check_response_code()
```