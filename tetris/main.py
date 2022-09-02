import pygame
import math
from game import Game

RED = (255, 0, 0)

pygame.init()
window = pygame.display.set_mode((450, 600))
pygame.display.set_caption("TETRIS")
run = True
time = pygame.time.Clock()

game = Game()

while run:

    pygame.time.delay(int(game.speed)) #predkosc gry

    pygame.font.init()
    instruction_font = pygame.font.SysFont('instruction font', 25)
    instruction_text = instruction_font.render('A/D -rotate brick            L-arrow/R-arrow - move brick', True, RED) #wyswietlanie instrukcji
    window.blit(instruction_text, (10, 580))

    for x in range(15):
        for y in range(19):
            if game.game_board.board[y, x] == 0:
                pygame.draw.rect(window, (152, 245, 255), (x*30, y*30, 30, 30))
            if game.game_board.board[y, x] == 2:
                pygame.draw.rect(window, (102, 205, 0), (x * 30, y * 30, 30, 30))
            if game.game_board.board[y, x] == 1:
                pygame.draw.rect(window, (255, 185, 15), (x * 30, y * 30, 30, 30))

    if game.current_brick is None:
        game.new_brick()

    for i in game.current_brick.brick_fields:
        pygame.draw.rect(window, game.current_brick.color, (i[0], i[1], 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                game.current_brick.rotate_left()
            if event.key == pygame.K_d:
                game.current_brick.rotate_right()
            if event.key == pygame.K_LEFT:
                game.current_brick.move_left()
            if event.key == pygame.K_RIGHT:
                game.current_brick.move_right()
            if event.key == pygame.K_DOWN:
                game.current_brick.move_down(30)

    game.current_brick.move_down(1)
    for i in game.current_brick.brick_fields:
        if game.game_board.board[math.floor(i[1] / 30) + 1, math.floor(i[0]/30)] == 1 or game.game_board.board[math.floor(i[1] / 30) + 1, math.floor(i[0]/30)] == 2:
            for j in game.current_brick.brick_fields:
                game.game_board.board[math.floor(j[1] / 30), math.floor(j[0]/30)] = 1
            game.current_brick = None
            break

    if game.game_board.update_board():
        game.score += 15
        game.speed = 40 - game.score * 0.2

    score_font = pygame.font.SysFont('score font', 35)
    score_text = score_font.render("Score = " + str(game.score), True, RED)  # wyswietlanie wyniku
    window.blit(score_text, (10, 10))

    if game.game_over():
        game_over_font = pygame.font.SysFont('game over font', 50)
        game_over_text = game_over_font.render("GAME OVER", True, RED)
        window.blit(game_over_text, (125, 200))


    pygame.display.update()
    window.fill((0, 0, 0))
