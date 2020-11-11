# Import JSON library
import json

# Creating a dictionary and stored in variable called car_data
car_data = {"name":"tesla", "engine":"electric"}

# json.dumps() - serialises json to a formatted string
car_data_json_string = json.dumps(car_data)
print(car_data_json_string)
print(type(car_data_json_string))  #Returns string

# json.dump() - creates a stream object and accepts a file object to write to
with open("new_json_file.json", "w") as jsonfile:
     json.dump(car_data,jsonfile)

# # Load() - copies the data and stores into a variable.
with open("JSON/new_json_file.json") as jsonfile:
    car = json.load(jsonfile) # Load() - copies the data and stores into a variable.
    print(car)
    print(type(car))
    print(car['name'])
    print(car['engine'])



# TASK 1 - Implement exception handling to determine whether a file exists and if not, return an error message.
try:
    file = open("JSON/new_json_file.json")
    print("Success")
except FileNotFoundError as errmsg:
    print("Sorry the file you are looking for does not exist.\n" + str(errmsg))