import pygame

from modules import constantes
from pygame.locals import *
from modules.constantes import FOND, MACGYVER, OBJECT1, SIZE_SPRITE, OBJECT2, OBJECT3, GUARDIAN_SPRITE, SIDE_WINDOW, \
    HEIGHT_WINDOW, HOME
from modules.map import Map
from modules.map_element import Object, Macgyver

window = pygame.display.set_mode((SIDE_WINDOW, HEIGHT_WINDOW))
window.blit(HOME, (0, 0))


def init_items(my_map):
    obj1 = Object(my_map)
    obj1.randomize_position()
    obj2 = Object(my_map)
    obj2.randomize_position()
    obj3 = Object(my_map)
    obj3.randomize_position()

    return obj1, obj2, obj3


class Appgame:
    def game(self):
        play_game = 1
        while play_game:
            pygame.display.flip()
            continue_game = 1
            continue_home = 1
            while continue_home:
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        continue_home = 0
                        continue_game = 0
                        play_game = 0
                    elif event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            continue_home = 0
                            continue_game = 1
                            pygame.display.flip()
            m = Map()
            m.creation()
            obj1, obj2, obj3 = init_items(m.my_map)
            p = Macgyver(m.my_map)
            object_count = 0

            font = pygame.font.Font(None, 100)
            text = font.render(str(object_count), True, (255, 255, 255))
            rect_text = text.get_rect()
            rect_text.center = text.get_rect().center
            pygame.display.flip()

            while continue_game:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        continue_game = 0
                        play_game = 0
                    elif event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            continue_game = 0
                            play_game = 0
                        elif event.key == K_RIGHT:
                            p.move('right')
                        elif event.key == K_LEFT:
                            p.move('left')
                        elif event.key == K_UP:
                            p.move('up')
                        elif event.key == K_DOWN:
                            p.move('down')

                    if p.case_x == obj1.case_x and p.case_y == obj1.case_y:
                        obj1.case_x = 0
                        obj1.case_y = 15
                        object_count += 1

                    if p.case_x == obj2.case_x and p.case_y == obj2.case_y:
                        obj2.case_x = 1
                        obj2.case_y = 15
                        object_count += 1

                    if p.case_x == obj3.case_x and p.case_y == obj3.case_y:
                        obj3.case_x = 2
                        obj3.case_y = 15
                        object_count += 1

                    window.blit(FOND, (0, 0))
                    m.display(window)
                    window.blit(MACGYVER, (p.x, p.y))
                    window.blit(OBJECT1, (obj1.case_x * SIZE_SPRITE, obj1.case_y * SIZE_SPRITE))
                    window.blit(OBJECT2, (obj2.case_x * SIZE_SPRITE, obj2.case_y * SIZE_SPRITE))
                    window.blit(OBJECT3, (obj3.case_x * SIZE_SPRITE, obj3.case_y * SIZE_SPRITE))

                    text = font.render(str(object_count), True, (255, 255, 255))
                    rect_text.center = window.get_rect().center
                    window.blit(text, rect_text)
                    pygame.display.flip()

                    if m.my_map[p.case_x][p.case_y] == GUARDIAN_SPRITE and object_count == 3:
                        black = (0, 0, 0)
                        myfont = pygame.font.SysFont("Times New Roman", 25)
                        randfont = myfont.render("Well done you won !! Press space to restart", 1, black)
                        window.blit(randfont, (150, 250))
                        continue_game = 0
                        pygame.display.flip()

                    if m.my_map[p.case_x][p.case_y] == GUARDIAN_SPRITE and object_count != 3:
                        black = (0, 0, 0)
                        myfont = pygame.font.SysFont("Times New Roman", 25)
                        randfont = myfont.render("Game Over ! Press space to restart", 1, black)
                        window.blit(randfont, (150, 300))
                        continue_game = 0
                        pygame.display.flip()
