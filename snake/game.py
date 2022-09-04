from snake import Snake
import pygame
import random

class Game:

    def __init__(self):
        self.sneak = Snake()
        self.score = 0
        self.point = self.new_point()

    def controls(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.sneak.move_direction != [0, 1]:
                    self.sneak.move_direction = [0, -1]
                if event.key == pygame.K_LEFT and self.sneak.move_direction != [1, 0]:
                    self.sneak.move_direction = [-1, 0]
                if event.key == pygame.K_RIGHT and self.sneak.move_direction != [-1, 0]:
                    self.sneak.move_direction = [1, 0]
                if event.key == pygame.K_DOWN and self.sneak.move_direction != [0, -1]:
                    self.sneak.move_direction = [0, 1]
        return True

    def new_point(self) -> []:
        while True:
            x = random.randint(1, 22)
            y = random.randint(1, 22)
            cnt = False
            for i in self.sneak.snake_fields:
                if i == [x, y]:
                    cnt = True
            if cnt:
                continue
            else:
                break
        return [x, y]

    def point_earned(self):
        if self.point == [self.sneak.x, self.sneak.y]:
            self.score += 10
            self.point = None
            return True
        return False

    def game_over(self) -> bool:
        for i in self.sneak.snake_fields:
            if i == [self.sneak.x, self.sneak.y]:
                return True
        if self.sneak.x < 1 or self.sneak.x > 23:
            return True
        if self.sneak.y < 1 or self.sneak.y > 23:
            return True
        return False