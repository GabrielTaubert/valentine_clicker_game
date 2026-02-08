"""
second consumable item -> second least expensive item

automatic heart gen without clicking +1
"""
from game.item import Item


class HouseKey(Item):

    def __init__(self, image):
        Item.__init__(self, image)
        self.price = 300
        self.name = "House Key"
        self.amount = 1

    def apply_effect(self, base_dict):
        heart = base_dict.get("heart")

        if heart:
            heart.upgrade_automatic_hearts_per_second(self.amount)