import pygame
import math
from game import Game


GREY = (51, 51, 51)
BLUE = (16,78,139)
BRIGHTER_BLUE = (24,116,205)
BRIGHTER_GRAY = (105, 105, 105)
EVEN_BRIGHTER_BLUE = (30, 144, 255)
DARKER_GRAY = (41, 41, 41)
RED = (139,35,35)

ships = ['patrol_boat', 'frigate', 'destroyer', 'carrier']

pygame.init()
window = pygame.display.set_mode((720, 840))
pygame.display.set_caption("BATTLESHIPS")

run = True

game = Game()

while run:

    window.fill(GREY)
    pygame.draw.rect(window, BLUE, (330, 30, 360, 360))
    pygame.draw.rect(window, BLUE, (330, 450, 360, 360))
    pygame.draw.rect(window, DARKER_GRAY, (30, 30, 270, 90))

    for i in range(12):
        for j in range(26):
            if j < 12 or j > 13:
                pygame.draw.rect(window, BRIGHTER_BLUE, (331 + 30 * i, 31 + 30 * j, 28, 28))

    your_ships_font = pygame.font.SysFont('your ships', 30)
    your_ships_text = your_ships_font.render("YOUR SHIPS ", True, BRIGHTER_GRAY)
    window.blit(your_ships_text, (440, 428))

    enemy_ships_font = pygame.font.SysFont('your ships', 30)
    enemy_ships_text = enemy_ships_font.render("ENEMY SHIPS ", True, BRIGHTER_GRAY)
    window.blit(enemy_ships_text, (440, 8))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    if 330 < mouse_x < 690 and (30 < mouse_y < 390 or 450 < mouse_y < 810):
        pygame.mouse.set_visible(False)
        pygame.draw.rect(window, EVEN_BRIGHTER_BLUE, (math.floor(mouse_x/30) * 30, math.floor(mouse_y/30) * 30, 30, 30))
    else:
        pygame.mouse.set_visible(True)

    for i in ships:
        select_ships_positions_font = pygame.font.SysFont('select positions for ships', 20)
        select_ships_positions_text = select_ships_positions_font.render("SELECT POSITIONS FOR YOUR SHIPS...", True, RED)
        window.blit(select_ships_positions_text, (35, 45))





    pygame.display.update()

