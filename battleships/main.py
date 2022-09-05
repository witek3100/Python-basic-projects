import pygame
import math
from game import Game
from ships import Patrol_boat


GREY = (51, 51, 51)
BLUE = (16,78,139)
BRIGHTER_BLUE = (24,116,205)
BRIGHTER_GRAY = (105, 105, 105)
EVEN_BRIGHTER_GRAY = (139, 129, 76)
EVEN_BRIGHTER_BLUE = (30, 144, 255)
DARKER_GRAY = (41, 41, 41)
RED = (139,35,35)


ships = ['patrol_boat', 'patrol_boat', 'patrol_boat', 'frigate', 'frigate']

pygame.init()
window = pygame.display.set_mode((720, 840))
pygame.display.set_caption("BATTLESHIPS")

run = True

game = Game()

while run:

    ev = pygame.event.get()

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

    for event in ev:
        if event.type == pygame.QUIT:
            run = False

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]
    if 330 < mouse_x < 690 and (30 < mouse_y < 390 or 450 < mouse_y < 810):
        pygame.mouse.set_visible(False)
        pygame.draw.rect(window, EVEN_BRIGHTER_BLUE, (math.floor(mouse_x/30) * 30, math.floor(mouse_y/30) * 30, 30, 30))
    else:
        pygame.mouse.set_visible(True)

    for i in game.player_ships:
        for j in i.ship_fields:
            pygame.draw.rect(window, EVEN_BRIGHTER_GRAY, (333 + j.position[0] * 30, 33 + j.position[1] * 30, 25, 25))

    if len(ships) > 0:

        select_ships_positions_font = pygame.font.SysFont('select positions for ships', 21)
        select_ships_positions_text = select_ships_positions_font.render("SELECT POSITIONS FOR YOUR SHIPS", True, RED)
        window.blit(select_ships_positions_text, (35, 45))
        if ships[0] == 'patrol_boat':
            select_patrol_boat_position_font = pygame.font.SysFont('select position for patrol boat', 23)
            select_patrol_boat_position_text = select_patrol_boat_position_font.render("select position for patrol boat...", True, RED)
            window.blit(select_patrol_boat_position_text, (35, 80))
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    if 330 < mouse_x < 690 and 30 < mouse_y < 390:
                        ship_x = math.floor((mouse_x-330)/30)
                        ship_y = math.floor((mouse_y-30)/30)
                        new_ship = Patrol_boat(ship_x, ship_y)
                        game.player_ships_board[ship_x][ship_y].ship = new_ship
                        game.player_ships.append(new_ship)
                        ships.pop(0)
        if ships[0] == 'frigate':
            select_frigate_position_font = pygame.font.SysFont('select position for frigate', 23)
            select_frigate_position_text = select_frigate_position_font.render("select position for frigate...", True, RED)
            window.blit(select_frigate_position_text, (35, 80))
            if 330 < mouse_x < 690 and 30 < mouse_y < 390:
                pygame.draw.rect(window, EVEN_BRIGHTER_BLUE, ((math.floor(mouse_x / 30) + 1) * 30, (math.floor(mouse_y / 30)) * 30, 30, 30))
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP:
                        ship_x = math.floor((mouse_x - 330) / 30)
                        ship_y = math.floor((mouse_y - 30) / 30)
                        new_ship = Patrol_boat(ship_x, ship_y)
                        game.player_ships_board[ship_x][ship_y].ship = new_ship
                        game.player_ships_board[ship_x + 1][ship_y] = new_ship
                        game.player_ships.append(new_ship)
                        ships.pop(0)

    else:
        pygame.time.delay(1)


    pygame.display.update()

