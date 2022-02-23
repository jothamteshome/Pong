from Pong_AI_Lib.Item import Item
import pygame


class Block(Item):
    __height = 50
    __width = 10

    def __init__(self, xpos, ypos):
        super().__init__()
        self.set_xpos(xpos)
        self.set_ypos(ypos)
        self.__rectangle = None

    def draw(self, context):
        pygame.draw.rect(context, self.get_color(), self.__rectangle)

    def move(self):
        self.set_ypos(self.get_ypos() + self.get_y_speed())

    def update(self):
        self.__rectangle = pygame.Rect(self.get_xpos(), self.get_ypos() - self.__height / 2,
                                       self.__width, self.__height)

    def get_rect(self):
        return self.__rectangle
