import pygame

from modules.constants import SIDE_WINDOW, HEIGHT_WINDOW, \
    HOME, FOND, GUARDIAN_SPRITE
from modules.map import Map
from modules.map_element import Object, Macgyver

window = pygame.display.set_mode((SIDE_WINDOW, HEIGHT_WINDOW))
window.blit(HOME, (0, 0))


def init_items(my_map):
    """Generate multiple objects at different positions"""
    obj1 = Object(my_map)
    obj1.randomize_position()
    obj2 = Object(my_map)
    obj2.randomize_position()
    obj3 = Object(my_map)
    obj3.randomize_position()

    return obj1, obj2, obj3


class Appgame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("MacGyver")

    def game(self):
        """Main function"""
        play_game = 1
        while play_game:
            pygame.display.flip()
            continue_game = 1
            continue_home = 1
            while continue_home:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT \
                            or event.type == pygame.KEYDOWN \
                            and event.key == pygame.K_ESCAPE:
                        continue_home = 0
                        continue_game = 0
                        play_game = 0
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            continue_home = 0
                            continue_game = 1
                            pygame.display.flip()
            m = Map()
            m.creation()
            obj1, obj2, obj3 = init_items(m.my_map)
            objects = Object(m.my_map)
            mc = Macgyver(m.my_map)

            while continue_game:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        continue_game = 0
                        play_game = 0
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            continue_game = 0
                            play_game = 0
                        elif event.key == pygame.K_RIGHT:
                            mc.move('right')
                        elif event.key == pygame.K_LEFT:
                            mc.move('left')
                        elif event.key == pygame.K_UP:
                            mc.move('up')
                        elif event.key == pygame.K_DOWN:
                            mc.move('down')

                    mc.pick_objects(obj1, obj2, obj3)
                    window.blit(FOND, (0, 0))
                    m.display(window)
                    mc.add_mc()
                    objects.display_objects(obj1, obj2, obj3)
                    mc.object_counter()

                    if m.my_map[mc.case_x][mc.case_y] == GUARDIAN_SPRITE \
                            and mc.count_object == 3:
                        continue_game = 0
                        mc.win()
                    if m.my_map[mc.case_x][mc.case_y] == GUARDIAN_SPRITE \
                            and mc.count_object != 3:
                        continue_game = 0
                        mc.lose()
