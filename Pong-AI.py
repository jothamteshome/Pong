import Pong_AI_Lib
import pygame
from pygame.locals import *

from Pong_AI_Lib.Game import Game
import random


class App:
    def __init__(self):
        # Initialize display, clock, and fps
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 858, 530
        self.game = None
        self.fps = 60
        self.fps_clock = pygame.time.Clock()

        random.seed()

    def on_init(self):
        # Initialize window and game
        pygame.init()
        pygame.display.set_caption('Pong AI')
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.game = Game(self._display_surf, self.size)
        self._running = True

    def on_event(self, event):
        # Exit game on 'Quit' event
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        # Update the game, and check if any paddle input
        # keys are pressed
        self.game.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.game.on_up()
        if keys[pygame.K_DOWN]:
            self.game.on_down()
        if keys[pygame.K_w]:
            self.game.on_w()
        if keys[pygame.K_s]:
            self.game.on_s()

    def on_render(self):
        # Refresh the background and draw updated screen
        self._display_surf.fill((0, 0, 0))
        self.game.draw()
        pygame.display.flip()
        pygame.display.update()
        self.fps_clock.tick(self.fps)

    def on_cleanup(self):
        # Quit the game
        pygame.quit()

    def on_execute(self):
        # Start up the game
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()