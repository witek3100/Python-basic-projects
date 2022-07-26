import random

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
colors = [RED, GREEN, BLUE]

class Brick:

    brick_types = ['one', 'square', 'L', 'P', '3inrow']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotation = random.randint(0, 3)
        self.brick_type = random.choice(self.brick_types)
        self.update_brick_fields()
        self.color = random.choice(colors)

    def rotate_right(self):
        if self.rotation < 3:
            self.rotation += 1
        else:
            self.rotation = 0
        self.update_brick_fields()

    def rotate_left(self):
        if self.rotation == 0:
            self.rotation = 4
        else:
            self.rotation -= 1
        self.update_brick_fields()

    def move_right(self):
        max = 0
        for i in self.brick_fields:
            if i[0] > max:
                max = i[0]

        if max < 420:
            self.x += 30
            self.update_brick_fields()

    def move_left(self):
        min = 420
        for i in self.brick_fields:
            if i[0] < min:
                min = i[0]

        if min > 0:
            self.x -= 30
            self.update_brick_fields()

    def move_down(self, y):
        self.y += y
        self.update_brick_fields()

    def update_brick_fields(self):
        if self.brick_type == 'one':
            self.brick_fields = [[self.x, self.y]]
        if self.brick_type == 'square':
            self.brick_fields = [[self.x, self.y], [self.x, self.y - 30], [self.x + 30, self.y], [self.x + 30, self.y - 30]]
        if self.brick_type == '3inrow':
            if self.rotation == 0 or self.rotation == 2:
                self.brick_fields = [[self.x, self.y], [self.x, self.y - 30], [self.x, self.y + 30]]
            if self.rotation == 1 or self.rotation == 3:
                self.brick_fields = [[self.x, self.y], [self.x - 30, self.y], [self.x + 30, self.y]]
        if self.brick_type == 'L':
            if self.rotation == 0:
                self.brick_fields = [[self.x, self.y], [self.x, self.y - 30], [self.x, self.y + 30], [self.x + 30, self.y - 30]]
            if self.rotation == 2:
                self.brick_fields = [[self.x, self.y], [self.x, self.y - 30], [self.x, self.y + 30], [self.x - 30, self.y + 30]]
            if self.rotation == 1:
                self.brick_fields = [[self.x, self.y], [self.x - 30, self.y], [self.x + 30, self.y], [self.x - 30, self.y - 30]]
            if self.rotation == 3:
                self.brick_fields = [[self.x, self.y], [self.x - 30, self.y], [self.x + 30, self.y], [self.x + 30, self.y + 30]]
        if self.brick_type == 'P':
            if self.rotation == 0:
                self.brick_fields = [[self.x, self.y], [self.x, self.y - 30], [self.x, self.y + 30], [self.x + 30, self.y + 30]]
            if self.rotation == 2:
                self.brick_fields = [[self.x, self.y], [self.x, self.y - 30], [self.x, self.y + 30], [self.x - 30, self.y - 30]]
            if self.rotation == 1:
                self.brick_fields = [[self.x, self.y], [self.x - 30, self.y], [self.x + 30, self.y], [self.x + 30, self.y - 30]]
            if self.rotation == 3:
                self.brick_fields = [[self.x, self.y], [self.x - 30, self.y], [self.x + 30, self.y], [self.x - 30, self.y + 30]]
