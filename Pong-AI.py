import Pong_AI_Lib
import pygame
from pygame.locals import *

from Pong_AI_Lib.Game import Game
import random


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 858, 530
        self.game = None
        self.fps = 144
        self.fps_clock = pygame.time.Clock()

        random.seed()

    def on_init(self):
        pygame.init()
        pygame.display.set_caption('Pong AI')
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.game = Game(self._display_surf, self.size)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
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
        self._display_surf.fill((0, 0, 0))
        self.game.draw()
        pygame.display.flip()
        pygame.display.update()
        self.fps_clock.tick(self.fps)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
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