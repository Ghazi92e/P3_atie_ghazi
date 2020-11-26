import pygame

from modules.app_game import Appgame

"""Initialize Appgame in modules app_game"""
continue_game = True
while continue_game:
    start = Appgame(continue_game)
    start.main_menu()
    start.main_game()

