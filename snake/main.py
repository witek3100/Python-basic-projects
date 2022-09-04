import pygame
from game import Game

GRAY = (48, 48, 48)
GREEN = (124, 252, 0)

pygame.init()
window = pygame.display.set_mode((750, 750))
pygame.display.set_caption("SNAKE")

game = Game()

run = True
while run:

    pygame.time.delay(500)

    pygame.draw.rect(window, GRAY, (0, 0, 30, 750))
    pygame.draw.rect(window, GRAY, (0, 0, 750, 30))
    pygame.draw.rect(window, GRAY, (720, 0, 30, 750))
    pygame.draw.rect(window, GRAY, (0, 720, 750, 30))

    run = game.controls()

    pygame.draw.rect(window, GREEN, (game.sneak.x * 30, game.sneak.y * 30, 30, 30))
    for i in game.sneak.snake_fields:
        pygame.draw.rect(window, GREEN, (i[0]*30, i[1]*30, 30, 30))

    game.sneak.move()
    game.sneak.extend_snake = False
    if :
        game.sneak.extend_snake = True

    pygame.display.update()
    window.fill((0,0,0))