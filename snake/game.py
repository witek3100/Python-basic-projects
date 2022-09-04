from snake import Snake
import pygame

class Game:

    def __init__(self):
        self.sneak = Snake()
        self.score = 0

    def controls(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.sneak.move_direction = [0, -1]
                if event.key == pygame.K_LEFT:
                    self.sneak.move_direction = [-1, 0]
                if event.key == pygame.K_RIGHT:
                    self.sneak.move_direction = [1, 0]
                if event.key == pygame.K_DOWN:
                    self.sneak.move_direction = [0, 1]
        return True

    def update_score(self):
        self.score = len(self.sneak.snake_fields) - 2
