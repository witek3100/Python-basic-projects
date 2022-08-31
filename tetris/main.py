import pygame
import board


pygame.init()
win = pygame.display.set_mode((500, 600))
pygame.display.set_caption("TETRIS")

board = board()
