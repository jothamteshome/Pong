from PongLib.Block import Block
from PongLib.Ball import Ball
from PongLib.Background import Background
from PongLib.Scoreboard import Scoreboard


class Game:
    def __init__(self, context, display_size):
        # Initialize the background and scoreboard
        self.__context = context
        self.__background = Background(context, display_size)
        self.__scoreboard = Scoreboard(context, display_size)
        self.__display_width = display_size[0]
        self.__display_height = display_size[1]

        # Initialize moving items in game
        self.__left_block = Block(25, self.__display_height / 2)
        self.__right_block = Block(self.__display_width - 25 - 10, self.__display_height / 2)
        self.__ball = Ball(self)

    def draw(self):
        # Draw the scoreboard, background, paddles, and ball on screen
        self.__left_block.draw(self.__context)
        self.__right_block.draw(self.__context)
        self.__ball.draw(self.__context)
        self.__background.draw()
        self.__scoreboard.draw()

    def update(self):
        # Update moving game items
        self.__left_block.update()
        self.__right_block.update()
        self.__ball.update(self.__left_block.get_rect(), self.__right_block.get_rect())

    def on_w(self):
        # Move left paddle up on 'W' keypress
        self.__left_block.set_y_speed(-abs(self.__left_block.get_y_speed()))
        if self.__left_block.get_ypos() + self.__left_block.get_y_speed() > 0:
            self.__left_block.move()

    def on_s(self):
        # Move left paddle down on 'S' keypress
        self.__left_block.set_y_speed(abs((self.__left_block.get_y_speed())))
        if self.__left_block.get_ypos() + self.__left_block.get_y_speed() < self.__display_height:
            self.__left_block.move()

    def on_up(self):
        # Move right paddle up on 'Up Arrow' keypress
        self.__right_block.set_y_speed(-abs(self.__right_block.get_y_speed()))
        if self.__right_block.get_ypos() + self.__right_block.get_y_speed() > 0:
            self.__right_block.move()

    def on_down(self):
        # Move right paddle down on 'Down Arrow' keypress
        self.__right_block.set_y_speed(abs((self.__right_block.get_y_speed())))
        if self.__right_block.get_ypos() + self.__right_block.get_y_speed() < self.__display_height:
            self.__right_block.move()

    def get_display_width(self):
        return self.__display_width

    def get_display_height(self):
        return self.__display_height

    def get_scoreboard(self):
        return self.__scoreboard
