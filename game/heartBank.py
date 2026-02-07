"""
the heartBank is the storage for earned hearts.

it should be possible to get the amount of hearts in the bank.

it should be possible to add or remove hearst from the bank.

maybe an text fond with text color would be nice.
"""

import pygame

class HeartBank:

    def __init__(self, image, position):
        self.hearts = 0
        self.image = image
        self.position = position
        self.rect = self.image.get_rect(center=position)
        self.font = pygame.font.Font("assets/font/Minecraft.ttf", 50)

    def draw(self, screen, heart):
        screen.blit(self.image, self.rect)

        text_heart = self.font.render(f"Hearts: {self.hearts}", True, (148, 27, 45))

        text_heart_x = self.position[0] - 230
        text_heart_y = self.position[1] - 53

        text_hpc = self.font.render(f"HPC: +{heart.hearts_per_click}", True, (148, 27, 45))

        text_hpc_x = self.position[0] - 230
        text_hpc_y = self.position[1] + 16

        screen.blit(text_heart, (text_heart_x, text_heart_y))
        screen.blit(text_hpc, (text_hpc_x, text_hpc_y))

    def addHearts(self, amount ):
        self.hearts += amount
        print(self.hearts)

    def removeHearts(self, amount):
        self.hearts -= amount