
from typing import List
import pygame
from pet import Pet

class Habitat:
    items: List["HabitatItem"]
    background: pygame.Surface


    def __init__(self, _background: pygame.Surface):
        self.background = _background

    def add_pet(self, _pet: Pet):
        self.pet = _pet
