import random
import pygame
import math
from ships import Ship
from ship_field import Ship_Field

GREY = (51, 51, 51)
BLUE = (16,78,139)
BRIGHTER_BLUE = (24,116,205)
BRIGHTER_GRAY = (105, 105, 105)
EVEN_BRIGHTER_GRAY = (139, 129, 76)
EVEN_BRIGHTER_BLUE = (30, 144, 255)
DARKER_GRAY = (41, 41, 41)
RED = (139,35,35)

player_ships = []
enemy_ships = []
e_shot_fields = []
p_shot_fields = []

fields_to_shot = []
for x in range(12):
    for y in range(12):
        fields_to_shot.append((random.randint(0, 100), [x, y]))
fields_to_shot.sort(reverse=True)

def computer_shot():

    shot = fields_to_shot.pop()[1]
    for i in player_ships:
        for j in i.ship_fields:
            if j.position == shot:
                j.was_shot = True
                fields_to_shot[fields_to_shot.index(j.position)][0] += 100


    p_shot_fields.append(shot)


def area_empty(ship_fields, b):
    not_empty_fields = []
    not_empty_fields1 = [[x, -1] for x in range(11)]
    not_empty_fields2 = [[x, 12] for x in range(12)]
    not_empty_fields3 = [[-1, y] for y in range(12)]
    not_empty_fields4 = [[12, y] for y in range(12)]
    not_empty_fields = not_empty_fields1 + not_empty_fields2 + not_empty_fields3 + not_empty_fields4
    if b:
        for i in player_ships:
            for j in i.ship_fields:
                not_empty_fields.extend([[j.position[0], j.position[1]], [j.position[0], j.position[1] + 1], [j.position[0], j.position[1] - 1], [j.position[0] + 1, j.position[1]], [j.position[0] - 1, j.position[1]]])
    if b == False:
        for i in enemy_ships:
            for j in i.ship_fields:
                not_empty_fields.extend([[j.position[0], j.position[1]], [j.position[0], j.position[1] + 1],
                                         [j.position[0], j.position[1] - 1], [j.position[0] + 1, j.position[1]],
                                         [j.position[0] - 1, j.position[1]]])

    for x in ship_fields:
        if x.position in not_empty_fields:
            return False
    return True
scnnt = False

pygame.init()
window = pygame.display.set_mode((720, 840))
pygame.display.set_caption("BATTLESHIPS")

run = True

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
    window.blit(your_ships_text, (440, 8))

    enemy_ships_font = pygame.font.SysFont('your ships', 30)
    enemy_ships_text = enemy_ships_font.render("ENEMY SHIPS ", True, BRIGHTER_GRAY)
    window.blit(enemy_ships_text, (440, 428))

    for event in ev:
        if event.type == pygame.QUIT:
            run = False

    if len(player_ships) != 8:

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if 330 < mouse_x < 690 and 30 < mouse_y < 390:
            pygame.mouse.set_visible(False)
            pygame.draw.rect(window, EVEN_BRIGHTER_BLUE,
                             (math.floor(mouse_x / 30) * 30, math.floor(mouse_y / 30) * 30, 30, 30))
        else:
            pygame.mouse.set_visible(True)

        select_ships_positions_font = pygame.font.SysFont('select positions for ships', 21)
        select_ships_positions_text = select_ships_positions_font.render("SELECT POSITIONS FOR YOUR SHIPS", True, RED)
        window.blit(select_ships_positions_text, (35, 45))
        if 0 <= len(player_ships) < 3:
            select_patrol_boat_position_font = pygame.font.SysFont('select position for patrol boat', 23)
            select_patrol_boat_position_text = select_patrol_boat_position_font.render("select position for patrol boat...", True, RED)
            window.blit(select_patrol_boat_position_text, (35, 80))
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    if 330 < mouse_x < 690 and 30 < mouse_y < 390:
                        ship_x = math.floor((mouse_x - 330) / 30)
                        ship_y = math.floor((mouse_y - 30) / 30)
                        sf = [Ship_Field(ship_x, ship_y)]
                        if area_empty(sf, 1):
                            player_ships.append(Ship(sf))
                            scnnt = False
                            while True:
                                eship_x = random.randint(0, 11)
                                eship_y = random.randint(0, 11)
                                esf = [Ship_Field(eship_x, eship_y)]
                                if area_empty(esf, 0):
                                    enemy_ships.append(Ship(esf))
                                    break
                        else:
                            scnnt = True

        if 3 <= len(player_ships) < 5:
            select_frigate_position_font = pygame.font.SysFont('select position for frigate', 23)
            select_frigate_position_text = select_frigate_position_font.render("select position for frigate...", True, RED)
            window.blit(select_frigate_position_text, (35, 80))
            if 330 < mouse_x < 690 and 30 < mouse_y < 390:
                pygame.draw.rect(window, EVEN_BRIGHTER_BLUE, ((math.floor(mouse_x / 30) + 1) * 30, (math.floor(mouse_y / 30)) * 30, 30, 30))
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP:
                        ship_x = math.floor((mouse_x - 330) / 30)
                        ship_y = math.floor((mouse_y - 30) / 30)
                        sf = [Ship_Field(ship_x, ship_y), Ship_Field(ship_x + 1, ship_y)]
                        if area_empty(sf, 1):
                            player_ships.append(Ship(sf))
                            scnnt = False
                            while True:
                                eship_x = random.randint(0, 11)
                                eship_y = random.randint(0, 11)
                                esf = [Ship_Field(eship_x, eship_y), Ship_Field(eship_x + 1, eship_y)]
                                if area_empty(esf, 0):
                                    enemy_ships.append(Ship(esf))
                                    break
                        else:
                            scnnt = True
        if 5 <= len(player_ships) < 7:
            select_destroyer_position_font = pygame.font.SysFont('select position for destroyer', 23)
            select_destroyer_position_font = select_destroyer_position_font.render("select position for destroyer...", True, RED)
            window.blit(select_destroyer_position_font, (35, 80))
            if 330 < mouse_x < 690 and 30 < mouse_y < 390:
                pygame.draw.rect(window, EVEN_BRIGHTER_BLUE, ((math.floor(mouse_x / 30) + 1) * 30, (math.floor(mouse_y / 30)) * 30, 30, 30))
                pygame.draw.rect(window, EVEN_BRIGHTER_BLUE, ((math.floor(mouse_x / 30) - 1) * 30, (math.floor(mouse_y / 30)) * 30, 30, 30))
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP:
                        ship_x = math.floor((mouse_x - 330) / 30)
                        ship_y = math.floor((mouse_y - 30) / 30)
                        sf = [Ship_Field(ship_x, ship_y), Ship_Field(ship_x + 1, ship_y), Ship_Field(ship_x - 1, ship_y)]
                        if area_empty(sf, 1):
                            player_ships.append(Ship(sf))
                            scnnt = False
                            while True:
                                eship_x = random.randint(0, 11)
                                eship_y = random.randint(0, 11)
                                esf = [Ship_Field(eship_x, eship_y), Ship_Field(eship_x + 1, eship_y), Ship_Field(eship_x - 1, eship_y)]
                                if area_empty(esf, 0):
                                    enemy_ships.append(Ship(esf))
                                    break
                        else:
                            scnnt = True

        if 7 <= len(player_ships) < 8:
            select_carrier_position_font = pygame.font.SysFont('select position for carrier', 23)
            select_carrier_position_font = select_carrier_position_font.render("select position for carrier...", True, RED)
            window.blit(select_carrier_position_font, (35, 80))
            if 330 < mouse_x < 690 and 30 < mouse_y < 390:
                pygame.draw.rect(window, EVEN_BRIGHTER_BLUE, ((math.floor(mouse_x / 30) + 1) * 30, (math.floor(mouse_y / 30)) * 30, 30, 30))
                pygame.draw.rect(window, EVEN_BRIGHTER_BLUE, ((math.floor(mouse_x / 30) - 1) * 30, (math.floor(mouse_y / 30)) * 30, 30, 30))
                pygame.draw.rect(window, EVEN_BRIGHTER_BLUE, ((math.floor(mouse_x / 30)) * 30, (math.floor(mouse_y / 30) - 1) * 30, 30, 30))
                pygame.draw.rect(window, EVEN_BRIGHTER_BLUE, ((math.floor(mouse_x / 30) + 1) * 30, (math.floor(mouse_y / 30) - 1) * 30, 30, 30))
                pygame.draw.rect(window, EVEN_BRIGHTER_BLUE, ((math.floor(mouse_x / 30) + 2) * 30, (math.floor(mouse_y / 30)) * 30, 30, 30))
                for event in ev:
                    if event.type == pygame.MOUSEBUTTONUP:
                        ship_x = math.floor((mouse_x - 330) / 30)
                        ship_y = math.floor((mouse_y - 30) / 30)
                        sf = [Ship_Field(ship_x, ship_y), Ship_Field(ship_x + 1, ship_y), Ship_Field(ship_x - 1, ship_y), Ship_Field(ship_x, ship_y - 1), Ship_Field(ship_x + 1, ship_y - 1), Ship_Field(ship_x + 2, ship_y)]
                        if area_empty(sf, 1):
                            player_ships.append(Ship(sf))
                            scnnt = False
                            while True:
                                eship_x = random.randint(0, 11)
                                eship_y = random.randint(0, 11)
                                esf = [Ship_Field(eship_x, eship_y), Ship_Field(eship_x + 1, eship_y), Ship_Field(eship_x - 1, eship_y), Ship_Field(eship_x, eship_y - 1), Ship_Field(eship_x + 1, eship_y - 1), Ship_Field(eship_x + 2, eship_y)]
                                if area_empty(esf, 0):
                                    enemy_ships.append(Ship(esf))
                                    break
                        else:
                            scnnt = True

        if scnnt == True:
            ship_cannot_font = pygame.font.SysFont('ship cannot', 21)
            ship_cannot_text = ship_cannot_font.render("ship cannot be placed here...", True, RED)
            window.blit(ship_cannot_text, (35, 100))

    else:

        your_shot_font = pygame.font.SysFont('your shot', 30)
        your_shot_text = your_shot_font.render("YOUR SHOT... ", True, RED)
        window.blit(your_shot_text, (35, 45))

        mouse_x = pygame.mouse.get_pos()[0]
        mouse_y = pygame.mouse.get_pos()[1]
        if 330 < mouse_x < 690 and 450 < mouse_y < 810:
            pygame.mouse.set_visible(False)
            pygame.draw.rect(window, EVEN_BRIGHTER_BLUE,
                             (math.floor(mouse_x / 30) * 30, math.floor(mouse_y / 30) * 30, 30, 30))
        else:
            pygame.mouse.set_visible(True)

        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                if 330 < mouse_x < 690 and 450 < mouse_y < 810:
                    shot_x = math.floor((mouse_x - 330) / 30)
                    shot_y = math.floor((mouse_y - 450) / 30)
                    for i in enemy_ships:
                        for j in i.ship_fields:
                            if j.position == [shot_x, shot_y]:
                                j.was_shot = True
                    e_shot_fields.append([shot_x, shot_y])
                    pygame.display.update()

                    computer_shot()

    for i in player_ships:
        color = EVEN_BRIGHTER_GRAY
        if i.is_sunk():
            color = RED
        if len(i.ship_fields) > 5:
            pygame.draw.rect(window, color, (333 + i.ship_fields[2].position[0] * 30, 33 + i.ship_fields[2].position[1] * 30, 114, 25))
            pygame.draw.rect(window, color, (333 + i.ship_fields[3].position[0] * 30, 33 + i.ship_fields[4].position[1] * 30, 54, 54))
        else:
            sx = min(fx.position[0] for fx in i.ship_fields)
            sy = min(fx.position[1] for fx in i.ship_fields)
            slen = (max(fx.position[0] for fx in i.ship_fields) - sx + 1) * 30 - 6
            swid = (max(fx.position[1] for fx in i.ship_fields) - sy + 1) * 30 - 6
            pygame.draw.rect(window, color, (333 + sx * 30, 33 + sy * 30, slen, swid))


    for i in enemy_ships:
        if i.is_sunk():
            if len(i.ship_fields) > 5:
                pygame.draw.rect(window, EVEN_BRIGHTER_GRAY, (333 + i.ship_fields[2].position[0] * 30, 453 + i.ship_fields[2].position[1] * 30, 114, 25))
                pygame.draw.rect(window, EVEN_BRIGHTER_GRAY, (333 + i.ship_fields[3].position[0] * 30, 453 + i.ship_fields[4].position[1] * 30, 54, 54))
            else:
                sx = min(fx.position[0] for fx in i.ship_fields)
                sy = min(fx.position[1] for fx in i.ship_fields)
                slen = (max(fx.position[0] for fx in i.ship_fields) - sx + 1) * 30 - 6
                swid = (max(fx.position[1] for fx in i.ship_fields) - sy + 1) * 30 - 6
                pygame.draw.rect(window, EVEN_BRIGHTER_GRAY, (333 + sx * 30, 453 + sy * 30, slen, swid))

    for i in e_shot_fields:
        pygame.draw.circle(window, RED, [345 + i[0] * 30, 465 + i[1] * 30], 6)
    for i in p_shot_fields:
        pygame.draw.circle(window, RED, [345 + i[0] * 30, 45 +  i[1] * 30], 6)

    for i in enemy_ships:
        for j in i.ship_fields:
            if j.was_shot == True:
                pygame.draw.rect(window, RED, (335 + j.position[0] * 30, 460 + j.position[1] * 30, 20, 10))
                pygame.draw.rect(window, RED, (340 + j.position[0] * 30, 455 + j.position[1] * 30, 10, 20))

    for i in player_ships:
        for j in i.ship_fields:
            if j.was_shot == True:
                pygame.draw.rect(window, RED, (335 + j.position[0] * 30, 40 + j.position[1] * 30, 20, 10))
                pygame.draw.rect(window, RED, (340 + j.position[0] * 30, 35 + j.position[1] * 30, 10, 20))

    pygame.display.update()

    if [1 for i in range(8)] == [i.is_sunk() for i in player_ships]:
        print('Gameover')
    if [1 for i in range(8)] == [i.is_sunk() for i in enemy_ships]:
        print('Gameover')


