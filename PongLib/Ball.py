from PongLib.Item import Item
import pygame
import random

Min_Ball_Speed = 4.5    # Minimum speed of the ball
Max_Ball_Speed = 5.5    # Maximum speed of the ball
Shift_Y_Range = 150     # Shift from center ball can start at
Ball_Size = 10          # Side length of ball


class Ball(Item):
    def __init__(self, game):
        super().__init__()

        # Game the ball is a part of
        self.__game = game

        # Set the speed of the ball on construction
        self.set_x_speed(Min_Ball_Speed)
        self.set_y_speed(Min_Ball_Speed)

        # Get random shift amount for ball to start at
        self.__starting_y = random.randint(-Shift_Y_Range, Shift_Y_Range)

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

        # Variable to store rectangle
        self.__rectangle = None

        # Set a tag for when the ball should be paused
        self.__paused = False
        self.__pause_start = None

    def draw(self, context):
        # Draw the rectangle on the graphics context
        pygame.draw.rect(context, self.get_color(), self.__rectangle)

    def update(self, left_paddle, right_paddle):
        # Update the rectangle
        self.__rectangle = pygame.Rect(self.get_xpos() - Ball_Size / 2, self.get_ypos() - Ball_Size / 2,
                                       Ball_Size, Ball_Size)

        # If ball is colliding with the left paddle, change the position
        # to one pixel to the right of the left paddle and shoot it to the right
        if self.__rectangle.colliderect(left_paddle):
            self.set_xpos(36)
            self.set_x_speed(abs(self.get_x_speed()))

        # If the ball is colliding with the right paddle, change the position
        # to one pixel to the left of the right paddle and shoot it to the left
        elif self.__rectangle.colliderect(right_paddle):
            self.set_xpos(self.__game.get_display_width() - 36)
            self.set_x_speed(-abs(self.get_x_speed()))

        # Update the position of the ball
        self.set_xpos(self.get_xpos() + self.get_x_speed())
        self.set_ypos(self.get_ypos() + self.get_y_speed())

        # If the entire ball goes off the left end
        if (self.get_xpos() + 2 * Ball_Size) < 0:

            # Update scoreboard to reflect right winning round
            if not self.__paused:
                current_score = self.__game.get_scoreboard().get_score()
                self.__game.get_scoreboard().update_score(current_score[0], current_score[1] + 1)

            # Pause game for a second before resuming
            # This is to allow the game loop to continue while the ball is paused
            # unlike with pygame.time.delay(), which hangs the entire program

            # Hold the ball in place while it should be paused
            self.set_x_speed(0)
            self.set_y_speed(0)

            # Set the start time for the pause then set the paused flag
            if not self.__paused:
                self.__pause_start = pygame.time.get_ticks()
                self.__paused = True

            # Unpause the game when one second has passed
            if pygame.time.get_ticks() - self.__pause_start > 1000:
                self.__paused = False

                # Flip which side the ball will shoot next
                if self.__shoot_left:
                    self.set_x_speed(-abs(random.uniform(Min_Ball_Speed, Max_Ball_Speed)))
                    self.__shoot_left = False
                else:
                    self.set_x_speed(abs(random.uniform(Min_Ball_Speed, Max_Ball_Speed)))
                    self.__shoot_left = True

                # Set the y-speed to a random number to shoot the ball in a
                # different direction every time
                self.set_y_speed(random.choice([random.uniform(-Min_Ball_Speed, -Max_Ball_Speed),
                                                random.uniform(Min_Ball_Speed, Max_Ball_Speed)]))

                # Reset the ball to the middle of the screen
                self.set_xpos(self.__game.get_display_width() / 2)
                self.set_ypos(self.__game.get_display_height() / 2 + random.randint(-Shift_Y_Range, Shift_Y_Range))

        # If the entire ball goes off the right end
        elif (self.get_xpos() - 2 * Ball_Size) > self.__game.get_display_width():

            # Update scoreboard to reflect left winning round
            if not self.__paused:
                current_score = self.__game.get_scoreboard().get_score()
                self.__game.get_scoreboard().update_score(current_score[0] + 1, current_score[1])

            # Pause game for a second before resuming
            # This is to allow the game loop to continue while the ball is paused
            # unlike with pygame.time.delay(), which hangs the entire program

            # Hold the ball in place while it should be paused
            self.set_x_speed(0)
            self.set_y_speed(0)

            # Set the start time for the pause then set the paused flag
            if not self.__paused:
                self.__pause_start = pygame.time.get_ticks()
                self.__paused = True

            # Unpause the game when one second has passed
            if pygame.time.get_ticks() - self.__pause_start > 1000:
                self.__paused = False

                # Flip which side the ball will shoot next
                if self.__shoot_left:
                    self.set_x_speed(-abs(random.uniform(Min_Ball_Speed, Max_Ball_Speed)))
                    self.__shoot_left = False
                else:
                    self.set_x_speed(abs(random.uniform(Min_Ball_Speed, Max_Ball_Speed)))
                    self.__shoot_left = True

                # Set the y-speed to a random number to shoot the ball in a
                # different direction every time
                self.set_y_speed(random.choice([random.uniform(-Min_Ball_Speed, -Max_Ball_Speed),
                                                random.uniform(Min_Ball_Speed, Max_Ball_Speed)]))

                # Reset the ball to the middle of the screen
                self.set_xpos(self.__game.get_display_width() / 2)
                self.set_ypos(self.__game.get_display_height() / 2 + random.randint(-Shift_Y_Range, Shift_Y_Range))

        # If the ball hits the top
        if self.get_ypos() < 0:
            # Bounce it down
            self.set_y_speed(abs(self.get_y_speed()))

        # If the ball hits the bottom
        elif self.get_ypos() > self.__game.get_display_height():
            # Bounce it up
            self.set_y_speed(-abs(self.get_y_speed()))
