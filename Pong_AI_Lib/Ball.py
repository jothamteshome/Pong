from Pong_AI_Lib.Item import Item
import pygame
import random


class Ball(Item):
    def __init__(self, xpos, ypos):
        super().__init__()

        # Side length of ball
        self.__side = 10

        # Get random shift amount for ball to start at
        self.__starting_y = random.randint(-150, 150)

        # Decide which side to shoot the ball towards
        self.__shoot_towards = random.randint(0, 1)

        # Shoot to the left if 0, otherwise shoot to the right
        if self.__shoot_towards == 0:
            self.set_speed(-self.get_speed())

        # Set the position of the ball
        self.set_xpos(xpos)
        self.set_ypos(ypos + self.__starting_y)

    def draw(self, context):
        pygame.draw.rect(context, self.get_color(), pygame.Rect(self.get_xpos() - self.__side / 2,
                                                                self.get_ypos() - self.__side / 2, self.__side,
                                                                self.__side))

    def update(self, elapsed):
        pass