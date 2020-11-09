# Contents 
* ***Python Library and Built-in Functions****
* ***What is pip and how do we use it?***
* ***API's with Python***


# Python Modules
* Built in functions which help us accelerate our development of software. 
* We access and use libraries by importing them in. 
* Syntax: 
```python
import <library_name>
``` 
* For example
```python
import math
```
* We can import specific modules within a library
``` from <library_name> import <module_name>```
* For example:
```python
from random import random
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

* To find out the system path
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
[API Diagram](/API%20diagram.png)
#£ What is pip
* Package manager for Python.
* We use it to install external packages such as requests. 
* syntax: ```pip install <name_of_package>```




