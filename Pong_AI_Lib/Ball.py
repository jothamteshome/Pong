from Pong_AI_Lib.Item import Item
import pygame
import random


class Ball(Item):
    def __init__(self, game):
        super().__init__()

        self.__game = game

        self.set_x_speed(1.5)
        self.set_y_speed(1.5)

        # Side length of ball
        self.__side = 10

        # Get random shift amount for ball to start at
        self.__starting_y = random.randint(-150, 150)

        # Decide which side to shoot the ball towards
        self.__shoot_towards = random.randint(0, 1)

        # Shoot to the left if 0, otherwise shoot to the right
        if self.__shoot_towards == 0:
            self.set_x_speed(-abs(self.get_x_speed()))
            self.__shoot_left = False
        else:
            self.set_x_speed(abs(self.get_x_speed()))
            self.__shoot_left = True

        # Set the position of the ball
        self.set_xpos(game.get_display_width() / 2)
        self.set_ypos(game.get_display_height() / 2 + self.__starting_y)
        self.__rectangle = None

    def draw(self, context):
        pygame.draw.rect(context, self.get_color(), self.__rectangle)

    def update(self, left_paddle, right_paddle):
        self.__rectangle = pygame.Rect(self.get_xpos() - self.__side / 2,
                                       self.get_ypos() - self.__side / 2, self.__side,
                                       self.__side)
        if self.__rectangle.colliderect(left_paddle) or self.__rectangle.colliderect(right_paddle):
            self.set_x_speed(-self.get_x_speed())
        self.set_xpos(self.get_xpos() + self.get_x_speed())
        self.set_ypos(self.get_ypos() + self.get_y_speed())
        if self.get_xpos() < 0:
            # Update scoreboard to reflect right winning round
            current_score = self.__game.get_scoreboard().get_score()
            self.__game.get_scoreboard().update_score(current_score[0], current_score[1] + 1)
            if self.__shoot_left:
                self.set_x_speed(-abs(self.get_x_speed()))
                self.__shoot_left = False
            else:
                self.set_x_speed(abs(self.get_x_speed()))
                self.__shoot_left = True
            self.set_xpos(self.__game.get_display_width() / 2)
            self.set_ypos(self.__game.get_display_height() / 2 + random.randint(-150, 150))
        elif self.get_xpos() > self.__game.get_display_width():
            # Update scoreboard to reflect left winning round
            current_score = self.__game.get_scoreboard().get_score()
            self.__game.get_scoreboard().update_score(current_score[0] + 1, current_score[1])
            if self.__shoot_left:
                self.set_x_speed(-abs(self.get_x_speed()))
                self.__shoot_left = False
            else:
                self.set_x_speed(abs(self.get_x_speed()))
                self.__shoot_left = True
            self.set_xpos(self.__game.get_display_width() / 2)
            self.set_ypos(self.__game.get_display_height() / 2 + random.randint(-150, 150))

        if self.get_ypos() < 0:
            self.set_y_speed(abs(self.get_y_speed()))
        elif self.get_ypos() > self.__game.get_display_height():
            self.set_y_speed(-abs(self.get_y_speed()))
