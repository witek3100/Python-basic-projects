import pygame
from game import Game

RED = (255, 0, 0)

pygame.init()
window = pygame.display.set_mode((450, 600))
pygame.display.set_caption("TETRIS")
run = True
time = pygame.time.Clock()

game = Game()

while run:
    pygame.time.delay(100)

    pygame.font.init()
    instruction_font1 = pygame.font.SysFont('instruction font', 25)
    instruction_text1 = instruction_font1.render('A/D rotate brick             L-arrow/R-arrow - move brick', True, RED)
    window.blit(instruction_text1, (10, 580))

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
    pygame.display.update()
    window.fill((0, 0, 0))
