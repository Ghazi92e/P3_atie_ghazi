import pygame
from modules.app_game import Appgame



pygame.init()
pygame.display.set_caption("MacGyver")
"""Initialize main function in modules app_game"""
start = Appgame()
start.game()


