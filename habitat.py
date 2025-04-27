
from typing import List, Tuple
import pygame
from pet import Pet

class Habitat:
    items: List["HabitatItem"]
    background: pygame.Surface

    def __init__(self, _background: pygame.Surface):
        self.background = _background

    def add_pet(self, _pet: Pet):
        self.pet = _pet
    
    def set_pet_position(self, _pos: Tuple[int, int]):
        self.pet.pos = _pos