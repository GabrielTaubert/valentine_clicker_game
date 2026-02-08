"""
fourth consumable item

add's +2 to the heart gen
"""
from game.item import Item


class DiamondRing(Item):

    def __init__(self, image):
        Item.__init__(self, image)
        self.price = 500
        self.name = "Diamond Ring"
        self.amount = 2

    def apply_effect(self, base_dict):
        heart = base_dict.get("heart")

        if heart:
            heart.upgrade_hearts_per_click(self.amount)