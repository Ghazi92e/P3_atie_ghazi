import pygame

pygame.init()

from constantes import *


class Map:
    def __init__(self):
        self.my_map = []

    def creation(self):
        with open("map.txt") as generating_file:
            content = []
            for ligne in generating_file:
                ligne_map = []
                for element in ligne:
                    if element != '\n':
                        ligne_map.append(element)
                content.append(ligne_map)
            self.my_map = content

    def display(self, window):
        number_ligne = 0
        for ligne in self.my_map:
            number_case = 0
            for element in ligne:
                x = number_case * SIZE_SPRITE
                y = number_ligne * SIZE_SPRITE
                if element == "M":
                    window.blit(WALL, (x, y))
                elif element == "G":
                    window.blit(GUARDIAN, (x, y))
                number_case += 1
            number_ligne += 1


class Macgyver():
    def __init__(self, my_map):
        self.x = 0
        self.y = 0
        self.my_map = my_map


running = True
while running:
    pygame.display.set_caption("MacGyver")
    window = pygame.display.set_mode((SIDE_WINDOW, HEIGHT_WINDOW))
    m = Map()
    m.creation()
    m.display(window)
    p = Macgyver(m.my_map)
    window.blit(MACGYVER, (p.x, p.y))
    pygame.display.flip()
    for event in pygame.event.get():
        # que l'evenement est fermetture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
