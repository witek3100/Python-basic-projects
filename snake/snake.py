

class Snake:

    def __init__(self):
        self.x = 12
        self.y = 12
        self.move_direction = [0, -1]
        self.snake_fields = [[self.x, self.y+1]]
        self.extend_snake = False

    def move(self):
        self.snake_fields.insert(0, [self.x, self.y])
        self.x += self.move_direction[0]
        self.y += self.move_direction[1]
        if self.extend_snake == False:
            self.snake_fields.pop()

