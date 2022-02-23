from PongLib.Item import Item
import pygame

Block_Height = 50
Block_Width = 10


class Block(Item):

    def __init__(self, xpos, ypos):
        super().__init__()
        self.set_xpos(xpos)
        self.set_ypos(ypos)
        self.__rectangle = None

    def draw(self, context):
        # Draw paddle on context
        pygame.draw.rect(context, self.get_color(), self.__rectangle)

    def move(self):
        # Move paddle
        self.set_ypos(self.get_ypos() + self.get_y_speed())

    def update(self):
        # Update paddle position
        self.__rectangle = pygame.Rect(self.get_xpos(), self.get_ypos() - Block_Height / 2,
                                       Block_Width, Block_Height)

    def get_rect(self):
        return self.__rectangle
