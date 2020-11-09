# importing requests to make an api call to the web
import requests
# Importing emoji library
from emoji import emojize

# # Create a variable to get data from a website
live_response=requests.get("https://www.bbc.co.uk/")
# # Print the status code. Returns an integer
# print(live_response.status_code)
#
# print(live_response.headers)
# print(type(live_response.content))
# # We can use an if statement to return a print statement.

# # ITERATION 1
# if live_response.status_code==200:
#     print("This website is live. Status code: " + str(live_response.status_code) + emojize((" :thumbs_up:")))
# elif live_response.status_code==404:
#     print(" This site is unavailable until further notice. Please contact support")
# else:
#     print("Oops something went wrong, please try later")

# # ITERATION 2
# def check_response_code():
#     if live_response.status_code==200:
#         print("This website is live. Status code: " + str(live_response.status_code) + emojize(" :thumbs_up:"))
#     elif live_response.status_code==404:
#         print(" This site is unavailable until further notice. Please contact support")
#     else:
#         print("Oops something went wrong, please try later")
#
# check_response_code()


# THIRD ITERATION
# Why do we use the requests module?
# If we get rid of the stats codes, the code still works because of the request method
def check_response_code():
    if live_response.status_code:
        print("This website is live. Status code: " + str(live_response.status_code) + emojize(" :thumbs_up:"))
    elif live_response.status_code:
        print(" This site is unavailable until further notice. Please contact support")
    else:
        print("Oops something went wrong, please try later")
check_response_code()
# It will evaluate to True if the status code is between 200-400, otherwise False. This is the built in functionality provided within the requests library.

