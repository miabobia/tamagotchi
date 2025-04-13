
# logic of tamagotchi game


# daily checkins

# minigames:
# - states

# what does model need to keep track of?
# pet
# enclosure


from typing import List, Tuple
import pygame
from pet import Pet
from habitat import Habitat
from viewer import TamaScreen
class TamaModel:

    viewer: TamaScreen

    pet: Pet
    habitat: Habitat