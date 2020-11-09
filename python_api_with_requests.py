# Importing requests to make an api call to the web
import requests
# Importing emoji library
from emoji import emojize

# Create a variable to get data from a website
live_response=requests.get("https://www.bbc.co.uk/")
# Print the status code. Returns an integer
print(live_response.status_code)
# We can also return the headers on this websits and the content.
print(live_response.headers)
print(type(live_response.content))

# # ITERATION 1 - Using an if statement
# We can use an if statement to print a string notifying the user of the status code.
# We have almost imported the emoji module.

if live_response.status_code==200:
    print("This website is live. Status code: " + str(live_response.status_code) + emojize((" :thumbs_up:")))
elif live_response.status_code==404:
    print(" This site is unavailable until further notice. Please contact support")
else:
    print("Oops something went wrong, please try later")

# # ITERATION 2 - Create a function
# Implement DRY by putting the if statement into a function.
def check_response_code():
    if live_response.status_code==200:
        print("This website is live. Status code: " + str(live_response.status_code) + emojize(" :thumbs_up:"))
    elif live_response.status_code==404:
        print(" This site is unavailable until further notice. Please contact support")
    else:
        print("Oops something went wrong, please try later")

check_response_code()


# ITERATION 3 - Why do we use the requests module?
# If we get rid of the status codes, the code still works because of the request method.
# It will evaluate to True if the status code is between 200-400, otherwise False.
# This is the built in functionality provided within the requests library.
def check_response_code():
    if live_response.status_code:
        print("This website is live. Status code: " + str(live_response.status_code) + emojize(" :thumbs_up:"))
    elif live_response.status_code:
        print(" This site is unavailable until further notice. Please contact support")
    else:
        print("Oops something went wrong, please try later")
check_response_code()


