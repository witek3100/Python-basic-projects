import random
import math
import pygame

from board import Board
from brick import Brick

class Game:

    def __init__(self):
        self.speed = 50
        self.score = 0
        self.game_board = Board()
        self.current_brick = None

    def new_brick(self):
        self.current_brick = Brick(30 * random.randint(1,13), 0)

    def brick_fell(self):
        for i in self.current_brick.brick_fields:
            m = self.game_board.board[math.floor(i[1] / 30) + 1, math.floor(i[0] / 30)]
            if m == 1 or m == 2:
                for j in self.current_brick.brick_fields:
                    self.game_board.board[math.floor(j[1] / 30), math.floor(j[0] / 30)] = 1
                self.current_brick = None
                break

    def controls(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.current_brick.rotate_left()
                if event.key == pygame.K_d:  # sterowanie ruchem klocka
                    self.current_brick.rotate_right()
                if event.key == pygame.K_LEFT:
                    self.current_brick.move_left()
                if event.key == pygame.K_RIGHT:
                    self.current_brick.move_right()
                if event.key == pygame.K_DOWN:
                    self    .current_brick.move_down(30)
        return True

    def update_board(self):
        if self.game_board.update_board():
            self.score += 15
            self.speed = 40 - self.score * 0.2