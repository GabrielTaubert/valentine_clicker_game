"""
items are consumables in the game.

this is just the basis/parent class.

vars like price, name, image are standard

every item can just be pruchased once.

after the buy of a item, a costum message should appear.
"""

import pygame

class Item:

    def __init__(self, image):
        self.price = 0
        self.name = ""
        self.image = image
        self.rect = self.image.get_rect()
        self.is_bought = False
        self.font = pygame.font.Font("assets/font/Minecraft.ttf", 30)

    def set_position(self, position):
        self.rect.center = position

    def draw(self, screen, is_buyable):
        screen.blit(self.image, self.rect)


        if not self.is_bought:
            if is_buyable:
                text = self.font.render(f"{self.price}", True, (148, 27, 45))
            else:
                text = self.font.render(f"{self.price}", True, (128, 128, 128))

            text_x = self.rect.centerx + 15
            text_y = self.rect.centery + 35

            screen.blit(text, (text_x, text_y))

    def buy(self, base_dict):
        self.is_bought = True
        self.apply_effect(base_dict)

    def apply_effect(self, base_dict):
        pass

    def message(self):
        pass