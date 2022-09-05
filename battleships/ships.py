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

class Patrol_boat:
    pass

class Carrier:
    pass

class Destroyer:
    pass

class Frigate:
    pass



