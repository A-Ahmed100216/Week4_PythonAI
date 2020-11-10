# EXCEPTION HANDLING

# ITERATION 1
# Create a variable to store a file data using open method.
# Lets try using try block when we know an error will be thrown.
try:
    file = open("orders.text")
except:
    print("Error")

# ITERATION 2
# If we know the error name, we can address it directly.
try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
    print("Sorry the file you are looking for does not exist.\n" + str(errmsg))

# ITERATION 3
# If we still want user to know actual exception together with out customer message, we can raise.
try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
    print("Alert something went wrong.\n" + str(errmsg))
    raise #Will send back the actual exception
finally: # Will execute regardless of the above conditions
    print("Hope you had a good customer experience ")


# TASK 1 - Implement exception handling to determine whether a file exists and if not, return an error message.
try:
    file = open("new_json_file.json")
    print("Success")
except FileNotFoundError as errmsg:
    print("Sorry the file you are looking for does not exist.\n" + str(errmsg))
