import pygame
from typing import Tuple

# tamagotchi screen
class TamaScreen:

    screen: pygame.Surface
    inner_screen: pygame.Surface
    outer_surface: pygame.Surface
    background: pygame.Surface

    def __init__(self, screen_size: Tuple[int], outer_screen_image: str):
        self.screen = pygame.display.set_mode(screen_size)
        self.outer_surface = pygame.image.load(outer_screen_image).convert_alpha()
    
    def display(self):
        self.screen.fill((0, 200, 50))
        self.screen.blit(self.outer_surface, (250, 250))
        pygame.display.flip()