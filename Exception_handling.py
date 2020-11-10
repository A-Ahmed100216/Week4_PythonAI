import json


car_data = {"name":"tesla", "engine":"electric"}


with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)


if open("new_json_file.json") ==True:
    try:
        print("file exists")
        # car = json.load("new_json_file.json") # Load() - copies the data and stores into a variable.
        # print(car)
        # print(type(car))
        # # print(car['name'])
        # print(car['engine'])
    except FileNotFoundError:
        print("no such file exists")


