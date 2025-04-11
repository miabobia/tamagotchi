

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

def create_config(save_file: str) -> str:
    # prompt user for input

    name = str(input("What's your lil guys name?: "))
    fav_colour = str(input("What's your favorite colour?: "))

    pet_data = {
        "name": name,
        "color": fav_colour
    }

    with open(save_file, 'w', encoding='utf-8') as f:
        json.dump(pet_data, f, ensure_ascii=False, indent=4)


def load_config(save_file='save.json'):
    if not os.path.exists(save_file):
        create_config(save_file)
    
    pet_data: dict

    with open(save_file, 'r') as f:
        pet_data = json.load(f)

    print(pet_data)


if __name__ == '__main__':
    load_config()