from Pong_AI_Lib.Block import Block
from Pong_AI_Lib.Ball import Ball
from Pong_AI_Lib.Background import Background
import pygame


class Game:
    def __init__(self, context, display_size):
        self.__context = context
        self.__background = Background(context, display_size)
        self.__display_width = display_size[0]
        self.__display_height = display_size[1]
        self.__game_items = []

        self.__left_block = Block(25, self.__display_height / 2)
        self.__right_block = Block(self.__display_width - 25 - 10, self.__display_height / 2)
        self.__ball = Ball(self.__display_width / 2, self.__display_height / 2)
        self.__game_items.append(self.__left_block)
        self.__game_items.append(self.__right_block)
        self.__game_items.append(self.__ball)

    def draw(self):
        for item in self.__game_items:
            item.draw(self.__context)

    def update(self, elapsed):
        for item in self.__game_items:
            item.update(elapsed)
