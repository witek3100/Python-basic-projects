import pygame
from game import Game
RED = (255, 0, 0)       #kolor wszystkich wyswietlanych informacji

pygame.init()
window = pygame.display.set_mode((450, 600))        #inicjalizacja okna gry
pygame.display.set_caption("TETRIS")

time = pygame.time.Clock()

game = Game()       #tworzenie gry

run = True
while run:

    pygame.time.delay(int(game.speed))      #predkosc gry

    pygame.font.init()
    instruction_font = pygame.font.SysFont('instruction font', 25)
    instruction_text = instruction_font.render('A/D -rotate brick            L-arrow/R-arrow - move brick', True, RED)        #wyswietlanie instrukci
    window.blit(instruction_text, (10, 580))

    for x in range(15):
        for y in range(19):
            if game.game_board.board[y, x] == 0:
                pygame.draw.rect(window, (152, 245, 255), (x*30, y*30, 30, 30))
            if game.game_board.board[y, x] == 2:                                        #rysowanie tla i klockow ktore spadly
                pygame.draw.rect(window, (102, 205, 0), (x * 30, y * 30, 30, 30))
            if game.game_board.board[y, x] == 1:
                pygame.draw.rect(window, (255, 185, 15), (x * 30, y * 30, 30, 30))

    if game.current_brick is None:         #tworzenie nowego kolcka jesli poprzedni jest juz na dole
        game.new_brick()

    for i in game.current_brick.brick_fields:
        pygame.draw.rect(window, game.current_brick.color, (i[0], i[1], 30, 30))      #rysowanie aktualnie spadajacego kolcka

    run = game.controls()       #sterowanie klockem / wylaczanie gry

    game.current_brick.move_down(2)                 #spadanie klocka

    game.brick_fell()         #spradzenie czy klocek spadl

    game.update_board()         #usuwanie wypelnionych klockami rzedow i zwiekszanie wyniku

    score_font = pygame.font.SysFont('score font', 35)
    score_text = score_font.render("Score = " + str(game.score), True, RED)  # wyswietlanie wyniku
    window.blit(score_text, (10, 10))

    if max(game.game_board.board[0]):
        game_over_font = pygame.font.SysFont('game over font', 50)
        game_over_text = game_over_font.render("GAME OVER", True, RED)
        window.blit(game_over_text, (125, 200))                                     #wyswietlanie 'game over'
        play_again_font = pygame.font.SysFont('play again', 50)
        play_again_text = play_again_font.render("press enter to play again", True, RED)
        window.blit(play_again_text, (30, 230))

    pygame.display.update()
    window.fill((0, 0, 0))

