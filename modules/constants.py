import pygame


pygame.display.init()
pygame.display.set_mode()
""" Set the window parameters"""
NUMBER_SPRITE_SIDE = 15
NUMBER_SPRITE_HEIGHT = 15
SIZE_SPRITE = 42
SIDE_WINDOW = NUMBER_SPRITE_SIDE * SIZE_SPRITE
HEIGHT_WINDOW = NUMBER_SPRITE_HEIGHT * SIZE_SPRITE
"""Set the pictures parameters"""
WALL = pygame.image.load("ressources/wall.png").convert()
GUARDIAN = pygame.image.load("ressources/Gardien.png").convert_alpha()
MACGYVER = pygame.image.load("ressources/MacGyver.png").convert_alpha()
OBJECT1 = pygame.image.load("ressources/aiguille.png").convert_alpha()
OBJECT2 = pygame.image.load("ressources/ether.png").convert_alpha()
OBJECT3 = pygame.image.load("ressources/tube_plastique.png").convert_alpha()
FOND = pygame.image.load("ressources/fond.jpg").convert()
HOME = pygame.image.load("ressources/Home.png").convert()
WALL_SPRITE = "M"
GUARDIAN_SPRITE = "G"
MACGYVER_SPRITE = "P"
