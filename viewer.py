import pygame
from typing import Tuple
from habitat import Habitat

# tamagotchi screen
class TamaScreen:

    screen: pygame.Surface
    background: pygame.Surface
    tamagotchi_model: pygame.Surface
    habitat: Habitat

    def __init__(self, screen_size: Tuple[int]):
        self.screen = pygame.display.set_mode(screen_size)

    def set_background(self, _background: pygame.Surface):
        """
        background can change depending on outside factors
        eg: time of day, event triggers
        """
        self.background = _background
    
    def set_tamagotchi_model(self, _tamagotchi_model: pygame.Surface):
        """
        shouldn't change often besides user input
        """
        self.tamagotchi_model = _tamagotchi_model
    
    def set_habitat(self, _habitat: Habitat):
        self.habitat = _habitat

    def display_background(self, coords: Tuple[int, int]):
        self.screen.blit(self.background, coords)

    def display_tamagotchi_model(self, coords: Tuple[int, int]):
        self.screen.blit(self.tamagotchi_model, coords)

    def display_habitat(self, coords: Tuple[int, int]):
        # This needs to change to habitat's surface component!
        self.screen.blit(self.habitat, coords)

    def display(self):
        """
        takes our three visual components and displays them seperately
        doing this because we might want to apply filters to some surfaces and not others
        """
        self.display_background((0, 0))
        self.display_tamagotchi_model((250,250))
        self.display_habitat((250, 250))
        pygame.display.flip()


"""
What does viewer need to display?
background image
tamagotchi model
habitat
pet
filter

should the model compile these things together `pre-render` them?

"""