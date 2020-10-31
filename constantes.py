import pygame


pygame.display.init()
pygame.display.set_mode()
NUMBER_SPRITE_SIDE = 15
NUMBER_SPRITE_HEIGHT = 15
SIZE_SPRITE = 50
SIDE_WINDOW = NUMBER_SPRITE_SIDE * SIZE_SPRITE
HEIGHT_WINDOW = NUMBER_SPRITE_HEIGHT * SIZE_SPRITE
WALL = pygame.image.load("wall.png").convert()
GUARDIAN = pygame.image.load("Gardien.png").convert()
MACGYVER = pygame.image.load("MacGyver.png").convert()
