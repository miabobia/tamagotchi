#!/usr/bin/env python2

import pygame
from viewer import TamaScreen
from typing import Tuple

def init_viewer(screen_size: Tuple[int, int], outer_screen_image: str) -> TamaScreen:
    return TamaScreen(screen_size, outer_screen_image)


WIDTH = 1000
HEIGHT = 1000
FPS = 30

## initialize pygame and create window
pygame.init()
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TAMAGOTCHI")
clock = pygame.time.Clock()     ## For syncing the FPS

viewer = init_viewer((WIDTH, HEIGHT), 'assets/outer_screen.png')

## Game loop
running = True
while running:

    clock.tick(FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        if event.type == pygame.QUIT:
            running = False

    viewer.display()

pygame.quit()