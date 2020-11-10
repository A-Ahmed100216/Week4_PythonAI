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
# Inside the random library we have a function called random which we can execute to return a float between 0 and 1
print(random.random())

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

3. ```datetime```
* We can use the datetime library to get the date and time of this exact moment. 
```python
import datetime
print(datetime.datetime.today())
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
3. CPU Count- Counts the number of CPUs in our system OS. This is useful in determinng whether the system meets any pre-requisites for a certain software. 
```python
print(os.cpu_count()) # Returns 4
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
#### What is pip
* Package manager for Python.
* We use it to install external packages such as requests. 
* syntax: ```pip install <name_of_package>```

## Request
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

### Implement DRY
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

### Why use the requests library?
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

## Task 2 - Postcode Task 
1. Get a user to input their postcode
2. Concatenate the postcode onto the postcode API and determine the status code.
3. If the postcode is valid, return the result and longitude and latitude of the postcode. 

```python
# Import relevant libraries
import requests
import json
from emoji import emojize

# Get a user to input their postcode
argument=input("Please enter your postcode: ")
# Concatenate onto the get request
live_response=requests.get("http://api.postcodes.io/postcodes/" + argument)

# Create a function to check the status code
def check_response_code():
    # If the function code is 200, postcode has been identified
    if live_response.status_code==200:
        print("Status Code: " + str(live_response.status_code) +". This postcode exists." +  emojize(" :thumbs_up:"))
    # If status code is 400 or 404, postcode is incorrect or has not been entered
    elif live_response.status_code==404 or live_response.status_code==400:
        print("Status Code: "+ str(live_response.status_code) + ". This postcode is incorrect. Please try again." + emojize(" :thumbs_down:"))
    else:
        print("Oops something went wrong, please try later")

# create a function that returns the longitude and latitude of the given postcode
def long_and_lat():
    # Convert bytes into dictionary format
    content_dictionary = json.loads(live_response.content)
    # If the status code is 200, contents can be retrieved
    if live_response.status_code==200:
        # Dictionary indexing to identify the result, longitude and latitude.
        result = content_dictionary['result']
        longitude = content_dictionary['result']['longitude']
        latitude = content_dictionary['result']['latitude']
        # Return as a formatted string
        return ("RESULT: {} \n"
                "Longitude: {}\n"
                "Latitude: {}".format(result,longitude,latitude))
    # Otherwise, return error message.
    else:
        return "Cannot determine latitude and longitude from an invalid input"


# Call the functions
check_response_code()
print(long_and_lat())
```

# JSON Basics
* Java Script Object Notation
* JSON is used heavily in industry. 
* Uses Case- browser data is typically in JSON format
* Data is in key, value pairs
* Reading files, writing to files, parsing and covering data are the most commonly utilised options.
* JSON encoding - from a Dictionary
* JSON decoding - into a dictionary
## JSON Methods
JSON like other libraries has many functions including:
1. json.dump() - serialises json to a formatted string
2. json.dump() - creates a stream object and accepts a file object to write to.

```python
# Import the json module 
import json

# Creating a dictionary and stored in variable called car_data
car_data = {"name":"tesla", "engine":"electric"}
print(type(car_data)) # This will return dictionary


# Using the dumps() method- converts dictionary to string
car_data_json_string = json.dumps(car_data)
print(car_data_json_string)
print(type(car_data_json_string)) # Return string
```
3. Encoding - We can encode from a dictionary and write to a new file with the dump()

```python
with open("new_json_file.json","w") as jsonfile:
     json.dump(car_data,jsonfile)
```
4. Decoding - We can decode and read a file using Load() which copies the data and stores in a variable. 
```python
with open("new_json_file.json") as jsonfile:
    # Load() - copies the data and stores into a variable.
    car = json.load(jsonfile) 
    print(car)
    print(type(car))
    print(car['name'])
    print(car['engine'])
```

## Exception Handling
* We can use ```try```, ```except```, and ```finally``` keywords for the purposes of handling errors and reporting back in a user-friendly fashion.
* Common use cases for these are error testing and resolving.
* We use these block when we expect an exception from the python interpreter.
* Why - This helps us handle the errors or exceptions and add customised message as well as make a decision based on customer needs. 
* **Try** - Lets you test for errors
* **Except** - Handle the error
* **Raise** - Raises an error
* **Finally** - Execute the code, regardless of the try and except blocks.
* Syntax:
```python
try:
    <action>
except:
    <action>
```

### Examples - Iteration 1
* We will have a look at the practical use cases and implementation of ```try```, ```except```, ```raise```, and ```finally```.
* We can use ```try``` block when we know an error will be thrown. In this example, the file does not exist so this will throw an error. 
* A ```try``` must be used in conjunction with an ```except```
```python

# try:
#     file = open("orders.text")
# except:
#     print("Error")
```

### Examples - Iteration 2
* Once we know the error, we can use this in the ```except``` block.
```python


try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
    print("Sorry the file you are looking for does not exist.\n" + str(errmsg))

```

### Examples - Iteration 3
* If we still want user to know actual exception together with our customer message, we can raise. This will return the exact error message. 
* Finally will execute regardless of the previous conditions. 
```python
try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
    print("Alert something went wrong.\n" + str(errmsg))
    raise #Will send back the actual exception
finally: 
    print("Hope you had a good customer experience ")
```
