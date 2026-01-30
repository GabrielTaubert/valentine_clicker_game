"""
the heart ist the main component of the game.

it should be clickable, by clicking generate hearts.

amount of generated hearts should be upgradeable.

maybe an animation would be nice.
"""

import pygame

class Heart:

    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.hearts_per_click = 1

    def upgrade_hearts_per_click(self, amount):
        self.hearts_per_click += amount

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # linke Maustaste
                if self.rect.collidepoint(event.pos):
                    return self.hearts_per_click
        return 0