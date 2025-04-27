
from typing import List, Tuple
import pygame
from pet import Pet
from habitat import Habitat
from viewer import TamaScreen
import config

class TamaModel:
    viewer: TamaScreen
    pet: Pet
    habitat: Habitat

    def build_viewer(self, screen_size: Tuple[int, int]):
        tama_screen = TamaScreen(screen_size)
        tama_screen.set_background(
            _background = pygame.image.load("assets/garden.jpg").convert_alpha()
        )
        tama_screen.set_tamagotchi_model(
            _tamagotchi_model = pygame.transform.scale(
                pygame.image.load("assets/device-export.png").convert_alpha(),
                (800, 800)
            ).convert_alpha()
        )
        tama_screen.set_habitat(
            _habitat = Habitat(
                _background = pygame.transform.scale(
                    pygame.image.load("assets/flowers.png").convert_alpha(),
                    (600, 600)
                ).convert_alpha()
            )
        )

        tama_screen.habitat.add_pet(config.load_config())

        self.viewer = tama_screen

    def update(self):
        self.viewer.display()