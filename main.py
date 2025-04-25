#!/usr/bin/env python2

import pygame
from typing import Tuple
from controller import Controller

# def init_viewer(screen_size: Tuple[int, int]) -> TamaScreen:
#     tama_screen = TamaScreen(screen_size)
#     tama_screen.set_background(
#         _background = pygame.image.load("assets/garden.jpg").convert_alpha()
#     )
#     tama_screen.set_tamagotchi_model(
#         _tamagotchi_model = pygame.transform.scale(
#             pygame.image.load("assets/device-export.png").convert_alpha(),
#             (800, 800)
#         ).convert_alpha()

#     )
#     tama_screen.set_habitat(
#         _habitat = Habitat(
#             _background = pygame.image.load("assets/smileyy.png").convert_alpha()
#         )
#     )

#     return tama_screen


WIDTH = 1000
HEIGHT = 1000
FPS = 30

## initialize pygame and create window
pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TAMAGOTCHI")
clock = pygame.time.Clock()     ## For syncing the FPS

# viewer = init_viewer((WIDTH, HEIGHT))
conch = Controller()
conch.set_model(None)
conch.tama_model.build_viewer((WIDTH, HEIGHT))
## Game loop
running = True
while running:

    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    # for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
    #     if event.type == pygame.QUIT:
    #         running = False
    conch.update()

pygame.quit()