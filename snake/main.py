import time

import pygame
from game import Game


GRAY = (48, 48, 48)
GREEN = (124, 252, 0)
RED =(255, 0, 0)

pygame.init()
window = pygame.display.set_mode((750, 750))
pygame.display.set_caption("SNAKE")

game = Game()

run = True

while run:

    pygame.time.delay(200)

    pygame.draw.rect(window, GRAY, (0, 0, 30, 750))
    pygame.draw.rect(window, GRAY, (0, 0, 750, 30))
    pygame.draw.rect(window, GRAY, (720, 0, 30, 750))
    pygame.draw.rect(window, GRAY, (0, 720, 750, 30))

    run = game.controls()

    if game.point == None:
        game.point = game.new_point()
    pygame.draw.circle(window, RED, (game.point[0]*30 + 15, game.point[1]*30 + 15), 15, 0)

    pygame.draw.rect(window, GREEN, (game.sneak.x * 30, game.sneak.y * 30, 30, 30))
    for i in game.sneak.snake_fields:
        pygame.draw.rect(window, GREEN, (i[0]*30, i[1]*30, 30, 30))

    game.sneak.move()
    game.sneak.extend_snake = False
    if game.point_earned():
        game.sneak.extend_snake = True

    score_font = pygame.font.SysFont('score font', 25)
    score_text = score_font.render("SCORE = " + str(game.score), True, RED)
    window.blit(score_text, (10, 10))

    if game.game_over():
        game_over_font = pygame.font.SysFont('game over font', 100)
        game_over_text = game_over_font.render("GAME OVER", True, RED)
        window.blit(game_over_text, (156, 200))
        play_agian_font = pygame.font.SysFont('play again font', 30)
        play_again_text = play_agian_font.render("your score: " + str(game.score) + "     press enter to play again...", True, RED)
        window.blit(play_again_text, (165, 300))
        pygame.display.update()
        time.sleep(5)
        run = False

    pygame.display.update()
    window.fill((0,0,0))