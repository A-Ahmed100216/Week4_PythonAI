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
