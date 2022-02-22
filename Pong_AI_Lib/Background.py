import pygame


class Background:
    def __init__(self, context, display_size):
        self.__block_num = display_size[1] / 10
        for i in range(0, int(self.__block_num / 2) + 1):
            pygame.draw.rect(context, (255, 255, 255), pygame.Rect((display_size[0] / 2) - 5, i * 20, 10, 10))
