import math

from ship_field import Ship_Field


class Ship:

    def __init__(self, sf):
        self.ship_fields = sf

    def is_sunk(self):
        if [1 for i in self.ship_fields if i.was_shot == True] == [1 for i in self.ship_fields]:
            return True
        return False



