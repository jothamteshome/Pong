import pygame


class Background:
    def __init__(self, context, display_size):
        self.__block_num = display_size[1] / 10
        self.__context = context
        self.__display_size = display_size

    def draw(self):
        for i in range(0, int(self.__block_num / 2) + 1):
            pygame.draw.rect(self.__context, (255, 255, 255),
                             pygame.Rect((self.__display_size[0] / 2) - 5, i * 20, 10, 10))
