"""
the heartBank is the storage for earned hearts.

it should be possible to get the amount of hearts in the bank.

it should be possible to add or remove hearst from the bank.

maybe an text fond with text color would be nice.
"""

class HeartBank:

    def __init__(self):
        self.hearts = 0

    def addHeart(self, amount):
        self.hearts += amount

    def removeHeart(self, amount):
        self.hearts -= amount