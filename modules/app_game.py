import pygame

from modules.constants import SIDE_WINDOW, HEIGHT_WINDOW, \
    GUARDIAN_SPRITE, OBJECT1, MACGYVER, OBJECT2, OBJECT3, GUARDIAN, WALL
from modules.map import Map
from modules.map_element import Object, Macgyver

window = pygame.display.set_mode((SIDE_WINDOW, HEIGHT_WINDOW))

FOND = pygame.image.load("ressources/fond.jpg")
HOME = pygame.image.load("ressources/Home.png")
window.blit(HOME, (0, 0))


class Appgame:
    def __init__(self, continue_game):
        pygame.init()
        pygame.display.set_caption("MacGyver")
        self.continue_game = continue_game

    def main_menu(self):
        """Menu game"""
        self.continue_game = False
        play = True
        pygame.display.flip()
        while play:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        play = False
                        self.continue_game = True

    def main_game(self):
        """Main game"""
        m = Map()
        m.creation()
        macgyver = MACGYVER
        mc = Macgyver(m.my_map, macgyver)
        images = [OBJECT1, OBJECT2, OBJECT3]
        obj1, obj2, obj3 = Object.init_items(m.my_map, images)
        while self.continue_game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
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
                m.display(window, WALL, GUARDIAN)
                mc.add_mc()
                Object.display_objects([obj1, obj2, obj3])
                mc.object_counter()

                if m.my_map[mc.case_x][mc.case_y] == GUARDIAN_SPRITE \
                        and mc.count_object == 3:
                    self.continue_game = False
                    mc.win()
                if m.my_map[mc.case_x][mc.case_y] == GUARDIAN_SPRITE \
                        and mc.count_object != 3:
                    self.continue_game = False
                    mc.lose()
