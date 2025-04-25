import pygame
from model import TamaModel

class Button:
    rect: pygame.Rect
    pressed: bool = False

    def __init__(self, _rect: pygame.Rect):
        self.rect = _rect

class Controller:
    tama_model: TamaModel
    buttons = [
        Button(pygame.Rect(238, 660, 122, 115)),
        Button(pygame.Rect(375, 655, 122, 115)),
        Button(pygame.Rect(510, 655, 122, 115))
    ]
    
    def set_model(self, _model: TamaModel = None):
        if _model is None:
            self.tama_model = TamaModel()
        else:
            self.tama_model = _model

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    mx, my = event.pos
                    if mx >= button.rect.left and mx <= button.rect.left + button.rect.width and\
                    my >= button.rect.top and my <= button.rect.top + button.rect.height:
                        button.pressed = True
                    else:
                        button.pressed = False

        
        for idx, button in enumerate(self.buttons):
            print(f'BUTTON[{idx}]: pressed = {button.pressed}')
                    # print(button.left, button.right, button.width, button.height)

        for button in self.buttons:
            button.pressed = False
        self.tama_model.update()

# Button One
# (238, 660)
# (239, 770)
# (359, 775)
# (362, 670)
# b1 = [238,]

# Button Two
# (377, 657)
# (488, 661)
# (487, 775)
# (376, 770)

# Button Three
# (512, 656)
# (626, 659)
# (626, 779)
# (511, 776)

