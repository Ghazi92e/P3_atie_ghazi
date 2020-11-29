import pygame
from modules.constants import SIDE_WINDOW, HEIGHT_WINDOW, WALL_SPRITE, \
    NUMBER_SPRITE_SIDE, SIZE_SPRITE
import random

window = pygame.display.set_mode((SIDE_WINDOW, HEIGHT_WINDOW))


class MapElement:
    """Set starting position for the elements Macgyver and Objects"""

    def __init__(self, my_map, image):
        self.x = 0
        self.y = 0
        self.case_x = 0
        self.case_y = 0
        self.my_map = my_map
        self.image = pygame.image.load(image).convert_alpha()


class Macgyver(MapElement):
    def __init__(self, my_map, image):
        super().__init__(my_map, image)
        self.objects = []

    def move(self, direction):
        """Verify available position and change Macgyver position"""
        if direction == "right":
            if self.case_x < NUMBER_SPRITE_SIDE - 1 \
                    and self.my_map[self.case_y][self.case_x + 1] \
                    != WALL_SPRITE:
                if self.case_x + 1 <= NUMBER_SPRITE_SIDE - 1:
                    self.case_x += 1
                    self.x = self.case_x * SIZE_SPRITE
        if direction == "left":
            if self.case_x >= 0 \
                    and self.my_map[self.case_y][self.case_x - 1] \
                    != WALL_SPRITE:
                if self.case_x - 1 >= 0:
                    self.case_x -= 1
                    self.x = self.case_x * SIZE_SPRITE
        if direction == "up":
            if self.case_y >= 0 \
                    and self.my_map[self.case_y - 1][self.case_x] \
                    != WALL_SPRITE:
                if self.case_y - 1 >= 0:
                    self.case_y -= 1
                    self.y = self.case_y * SIZE_SPRITE
        if direction == "down":
            if self.case_y < 14 \
                    and self.my_map[self.case_y + 1][self.case_x] \
                    != WALL_SPRITE:
                if self.case_y + 1 <= NUMBER_SPRITE_SIDE - 1:
                    self.case_y += 1
                    self.y = self.case_y * SIZE_SPRITE

    def add_mc(self):
        window.blit(self.image, (self.x, self.y))

    @property
    def count_object(self):
        """Return number of objects in the inventory"""
        return len(self.objects)

    def object_counter(self):
        """Count objects in the inventory"""
        font = pygame.font.Font(None, 100)
        text = font.render(str(self.count_object), True, (255, 255, 255))
        rect_text = text.get_rect()
        rect_text.topright = window.get_rect().topright
        window.blit(text, rect_text)
        pygame.display.flip()

    def win(self):
        """Display message win on window"""
        black = (0, 0, 0)
        myfont = pygame.font.SysFont("Times New Roman", 25)
        randfont = myfont.render("Well done you won !! "
                                 "Press space to restart", 1, black)
        window.blit(randfont, (150, 250))
        pygame.display.flip()

    def lose(self):
        """Display message lose on window"""
        black = (0, 0, 0)
        myfont = pygame.font.SysFont("Times New Roman", 25)
        randfont = myfont.render("Game Over ! "
                                 "Press space to restart", 1, black)
        window.blit(randfont, (150, 300))
        pygame.display.flip()

    def pick_objects(self, obj1, obj2, obj3):
        """Verify if Macgyver collect the
        3 objects and add objects in inventory"""
        if self.case_x == obj1.case_x and self.case_y == obj1.case_y:
            obj1.case_x = 0
            obj1.case_y = 15
            self.objects.append(obj1)
        if self.case_x == obj2.case_x and self.case_y == obj2.case_y:
            obj2.case_x = 1
            obj2.case_y = 15
            self.objects.append(obj2)
        if self.case_x == obj3.case_x and self.case_y == obj3.case_y:
            obj3.case_x = 2
            obj3.case_y = 15
            self.objects.append(obj3)


class Object(MapElement):
    @classmethod
    def init_items(cls, my_map, images, obj_count=3):
        """Generate multiple objects at different positions"""
        list_objects = []
        for i in range(obj_count):
            obj = cls(my_map, images[i])
            obj.randomize_position()
            list_objects.append(obj)
        return list_objects

    def randomize_position(self):
        """Generate a random position for objects"""
        while self.my_map[self.case_y][self.case_x] != "X":
            self.case_x = random.randint(0, 14)
            self.x = self.case_x * SIZE_SPRITE
            self.case_y = random.randint(0, 14)
            self.y = self.case_y * SIZE_SPRITE

    """Display the objects"""

    @staticmethod
    def display_objects(objects):
        for obj in objects:
            window.blit(obj.image, (obj.case_x * SIZE_SPRITE, obj.case_y * SIZE_SPRITE))
