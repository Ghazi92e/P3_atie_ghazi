from modules.constantes import NUMBER_SPRITE_SIDE, SIZE_SPRITE, WALL_SPRITE
import random


class MapElement:
    """Set starting position for the elements Macgyver and Objects"""
    def __init__(self, my_map):
        self.x = 0
        self.y = 0
        self.case_x = 0
        self.case_y = 0
        self.my_map = my_map


class Macgyver(MapElement):
    def move(self, direction):
        """Verify available position and change Macgyver position."""
        if direction == "right":
            if self.case_x < 14 and self.my_map[self.case_y][self.case_x + 1] != WALL_SPRITE:
                if self.case_x + 1 <= NUMBER_SPRITE_SIDE - 1:
                    self.case_x += 1
                    self.x = self.case_x * SIZE_SPRITE
        if direction == "left":
            if self.case_x >= 0 and self.my_map[self.case_y][self.case_x - 1] != WALL_SPRITE:
                if self.case_x - 1 >= 0:
                    self.case_x -= 1
                    self.x = self.case_x * SIZE_SPRITE
        if direction == "up":
            if self.case_y >= 0 and self.my_map[self.case_y - 1][self.case_x] != WALL_SPRITE:
                if self.case_y - 1 >= 0:
                    self.case_y -= 1
                    self.y = self.case_y * SIZE_SPRITE
        if direction == "down":
            if self.case_y < 14 and self.my_map[self.case_y + 1][self.case_x] != WALL_SPRITE:
                if self.case_y + 1 <= NUMBER_SPRITE_SIDE - 1:
                    self.case_y += 1
                    self.y = self.case_y * SIZE_SPRITE


class Object(MapElement):
    def randomize_position(self):
        """Generate a random position for objects"""
        while self.my_map[self.case_y][self.case_x] != "X":
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
            self.x = self.case_x * SIZE_SPRITE
            self.y = self.case_y * SIZE_SPRITE
