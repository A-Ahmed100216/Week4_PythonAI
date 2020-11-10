import json


car_data = {"name":"tesla", "engine":"electric"}


with open("new_json_file.json", "w") as jsonfile:
    json.dump(car_data, jsonfile)


if open("new_json_file.json", "r") == True:
    try:
        print("file exists")
    except FileNotFoundError:
        print("no such file exists")


