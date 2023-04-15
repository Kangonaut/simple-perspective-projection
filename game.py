import pygame
from color import Colors
from cube import Cube
import numpy as np


class GameManager:

    def __init__(self) -> None:
        pygame.init()
        self.SCREEN_DIM = (SCREEN_WIDTH, SCREEN_HEIGHT) = (1125, 786)
        self.TARGET_FPS = 60
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.finished = False
        self.delta_time: float = 0

        # define cube
        self.cube = Cube(
            position=np.array([
                int(SCREEN_WIDTH / 2),
                int(SCREEN_HEIGHT / 2)
            ], dtype='float32')
        )

    def __handle_input(self) -> None:
        pygame.event.pump()

        for event in pygame.event.get():
            # quit on quit UI button
            if event.type == pygame.QUIT:
                self.finished = True
            elif event.type == pygame.KEYDOWN:
                # quit on ESC button
                if event.key == pygame.K_ESCAPE:
                    self.finished = True

    def __update(self):
        self.cube.rotation[0] += 0.01  # rotate x
        # self.cube.rotation[1] += 0.01  # rotate y
        self.cube.rotation[2] += 0.01  # rotate z

    def __draw(self) -> None:
        self.screen.fill(Colors.BLACK)

        # draw cube
        self.cube.draw(self.screen)

        pygame.display.flip()

    def run(self) -> None:
        while not self.finished:
            self.delta_time = self.clock.get_time() / 1000

            self.__handle_input()
            self.__update()
            self.__draw()

            self.clock.tick(self.TARGET_FPS)  # VSYNC

            print()
            print('==== NEW FRAME ====')