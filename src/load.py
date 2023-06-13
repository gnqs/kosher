import os 
import json

game_level_folder = "./level/game_level"

file_list = os.listdir(game_level_folder)

def get_key_value(body, key, error_message=None):
    err = "KeyError: " + key + " is not found."
    if error_message != None:
        err = error_message
    if key in body:
        return body[key]
    else:
        raise ValueError(err)

for file_name in file_list:
    with open(os.path.join(game_level_folder, file_name), "r") as f:
        level_data = json.load(f)
        print(level_data["name"])