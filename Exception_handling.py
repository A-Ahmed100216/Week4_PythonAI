# import json
#
#
# car_data = {"name":"tesla", "engine":"electric"}
#
#
# with open("new_json_file.json", "w") as jsonfile:
#     json.dump(car_data, jsonfile)
#
#
# if open("new_json_file.json", "r") == True:
#     try:
#         print("file exists")
#     except FileNotFoundError:
#         print("no such file exists")


# We will have a look at the practical use cases and implementation of try, except, raise, and finally.
# Create a variable to store a file data using open method.
# Lets try using try block when we know an error will be thrown.
# ITERATION 1
# try:
#     file = open("orders.text")
# except:
#     print("Error")

# ITERATION 2
try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
    print("Sorry the file you are looking for does not exist.\n" + str(errmsg))


# If we still want user to know actual exception together with out customer message, we can raise.
try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
    print("Alert something went wrong.\n" + str(errmsg))
    raise #Will send back the actual exception
finally: # Will execute regardless of the above conditions
    print("Hope you had a good customer experience ")