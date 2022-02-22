from Pong_AI_Lib.Block import Block
import pygame


class Game:
    def __init__(self, display_size):
        self.__display_width = display_size[0]
        self.__display_height = display_size[1]
        self.__left_block = Block(25, self.__display_height / 2)
        self.__right_block = Block(self.__display_width - 35, self.__display_height / 2)

    def draw(self, context):
        self.__left_block.draw(context)
        self.__right_block.draw(context)
