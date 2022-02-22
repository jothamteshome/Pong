from Pong_AI_Lib.Item import Item
import pygame


class Block(Item):
    __height = 50
    __width = 10

    def __init__(self, xpos, ypos):
        super().__init__()
        self.set_xpos(xpos)
        self.set_ypos(ypos)

    def draw(self, context):
        pygame.draw.rect(context, self.get_color(), pygame.Rect(self.get_xpos(), self.get_ypos() - self.__height / 2,
                                                                self.__width, self.__height))

    def update(self, elapsed):
        pass
