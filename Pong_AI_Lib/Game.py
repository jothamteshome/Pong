from Pong_AI_Lib.Block import Block
from Pong_AI_Lib.Ball import Ball
from Pong_AI_Lib.Background import Background
from Pong_AI_Lib.Scoreboard import Scoreboard
import pygame


class Game:
    def __init__(self, context, display_size):
        self.__context = context
        self.__background = Background(context, display_size)
        self.__scoreboard = Scoreboard(context, display_size)
        self.__display_width = display_size[0]
        self.__display_height = display_size[1]
        self.__game_items = []

        self.__left_block = Block(25, self.__display_height / 2)
        self.__right_block = Block(self.__display_width - 25 - 10, self.__display_height / 2)
        self.__ball = Ball(self)
        self.__game_items.append(self.__left_block)
        self.__game_items.append(self.__right_block)
        self.__game_items.append(self.__ball)

    def draw(self):
        for item in self.__game_items:
            item.draw(self.__context)
        self.__background.draw()
        self.__scoreboard.draw()

    def update(self):
        self.__left_block.update()
        self.__right_block.update()
        self.__ball.update(self.__left_block.get_rect(), self.__right_block.get_rect())

    def on_w(self):
        self.__left_block.set_y_speed(-abs(self.__left_block.get_y_speed()))
        if self.__left_block.get_ypos() + self.__left_block.get_y_speed() > 0:
            self.__left_block.move()

    def on_s(self):
        self.__left_block.set_y_speed(abs((self.__left_block.get_y_speed())))
        if self.__left_block.get_ypos() + self.__left_block.get_y_speed() < self.__display_height:
            self.__left_block.move()

    def on_up(self):
        self.__right_block.set_y_speed(-abs(self.__right_block.get_y_speed()))
        if self.__right_block.get_ypos() + self.__right_block.get_y_speed() > 0:
            self.__right_block.move()

    def on_down(self):
        self.__right_block.set_y_speed(abs((self.__right_block.get_y_speed())))
        if self.__right_block.get_ypos() + self.__right_block.get_y_speed() < self.__display_height:
            self.__right_block.move()

    def get_display_width(self):
        return self.__display_width

    def get_display_height(self):
        return self.__display_height

    def get_scoreboard(self):
        return self.__scoreboard
