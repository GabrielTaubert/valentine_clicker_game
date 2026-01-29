"""
items are consumables in the game.

this is just the basis/parent class.

vars like price, name, image are standard

every item can just be pruchased once.

after the buy of a item, a costum message should appear.
"""

class Item:

    def __init__(self, price, name, image):
        self.price = price
        self.name = name
        self.image = image
        self.is_bought = False

    def buy(self):
        self.is_bought = True

    def message(self):
        pass