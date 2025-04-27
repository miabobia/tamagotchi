

# game loads up
# check if save.json exists
# if it doesn't exist:
# prompt user for input:
# - name
# - pet type?
# - fav color

# whats in save.json?
# creation date
# last time interacted with date
# pets stats:
# - evolution state (training level)
# - health 
# - hunger
# - happiness
# - tiredness
# - enclosure cleanliness

import os
import json
from pet import Pet

def create_config(save_file: str) -> str:
    # prompt user for input

    name = str(input("What's your lil guys name?: "))
    fav_colour = str(input("What's your favorite colour?: "))

    pet_data = {
        "name": name,
        "fav_colour": fav_colour
    }

    with open(save_file, 'w', encoding='utf-8') as f:
        json.dump(pet_data, f, ensure_ascii=False, indent=4)


def load_config(save_file='save.json') -> Pet:
    if not os.path.exists(save_file):
        create_config(save_file)

    pet_data: dict

    with open(save_file, 'r') as f:
        pet_data = json.load(f)

    pet_data["type"] = "default"
    pet_data["evolution_state"] = 0
    pet_data["health"] = 0
    pet_data["hunger"] = 0
    pet_data["happiness"] = 100
    pet_data["tiredness"] = 0

    return Pet(pet_data=pet_data)

if __name__ == '__main__':
    load_config()