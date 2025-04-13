
from typing import List
import pygame

class Habitat:
    items: List["HabitatItem"]
    background: pygame.Surface


    def __init__(self, _background: pygame.Surface):
        self.background = _background