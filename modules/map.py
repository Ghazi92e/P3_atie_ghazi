from modules.constants import SIZE_SPRITE, WALL, GUARDIAN, WALL_SPRITE, GUARDIAN_SPRITE


class Map:
    def __init__(self):
        self.my_map = []

    def creation(self):
        """Create a double entry table based on the .txt file"""
        with open("map.txt") as generating_file:
            content = []
            for line in generating_file:
                line_map = []
                for element in line:
                    if element != '\n':
                        line_map.append(element)
                content.append(line_map)
            self.my_map = content

    def display(self, window):
        """Use the double entry table to display wall sprite and guardian sprite"""
        number_line = 0
        for line in self.my_map:
            number_case = 0
            for element in line:
                x = number_case * SIZE_SPRITE
                y = number_line * SIZE_SPRITE
                if element == WALL_SPRITE:
                    window.blit(WALL, (x, y))
                elif element == GUARDIAN_SPRITE:
                    window.blit(GUARDIAN, (x, y))
                number_case += 1
            number_line += 1
