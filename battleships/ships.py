import pygame
from field import Field

class Ship:

    def __init__(self, x, y):
        self.position = [x, y]
        self.ship_fields = [Field(x, y)]

    def is_sunk(self):
        for i in self.ship_fields:
            if i.was_shot == False:
                return False
        return True

class Patrol_boat(Ship):
    pass

class Carrier(Ship):
    pass

class Destroyer(Ship):
    pass

class Frigate(Ship):

    def __init__(self, x, y):
        self.position = [x, y]
        self.ship_fields = [Field(x, y), Field(x + 1, y)]



