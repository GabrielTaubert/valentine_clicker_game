"""
last consumable item

opens the last message, player wins and get invitation to a date
"""
from game.item import Item


class Letter(Item):

    def __init__(self, image):
        Item.__init__(self, image)
        self.price = 1000
        self.name = "Letter"