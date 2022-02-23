import pygame.font


class Scoreboard:
    def __init__(self, context, display_size):
        # Save the graphics context and size of the display
        self.__context = context
        self.__display_size = display_size

        # The score of the two players
        self.__left_score = 0
        self.__right_score = 0

        # Font to write the score in
        self.__font = pygame.font.Font('freesansbold.ttf', 48)

    def draw(self):
        # Write the current score on the board
        text_left = self.__font.render(str(self.__left_score), True, (255, 255, 255))
        text_right = self.__font.render(str(self.__right_score), True, (255, 255, 255))
        text_rect_left = text_left.get_rect()
        text_rect_right = text_right.get_rect()
        text_rect_left.center, text_rect_right.center = \
            (self.__display_size[0] / 4, 50), (3 * self.__display_size[0] / 4, 50)
        self.__context.blit(text_left, text_rect_left)
        self.__context.blit(text_right, text_rect_right)

    def update_score(self, left, right):
        self.__left_score = left
        self.__right_score = right

    def get_score(self):
        return self.__left_score, self.__right_score

