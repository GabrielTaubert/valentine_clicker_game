"""
the heart ist the main component of the game.

it should be clickable, by clicking generate hearts.

amount of generated hearts should be upgradeable.

maybe an animation would be nice.
"""

class Heart:

    def __init__(self):
        self.hearts_per_click = 1

    def get_hearts_per_click(self):
        return self.hearts_per_click

    def upgrade_hearts_per_click(self, amount):
        self.hearts_per_click += amount