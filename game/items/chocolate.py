"""
first consumable item -> least expensive item

add's a buff to the heart gen with +1
"""
from game.item import Item


class Chocolate(Item):

    def __init__(self, image):
        Item.__init__(self, image)
        self.price = 100
        self.name = "Chocolate"
        self.amount = 1

    def apply_effect(self, base_dict):
        heart = base_dict.get("heart")

        if heart:
            heart.upgrade_hearts_per_click(self.amount)