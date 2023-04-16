import math
import pygame
from color import Colors
from cube import Cube
import numpy as np
import time


class GameManager:

    def __init__(self) -> None:
        pygame.init()
        self.SCREEN_DIM = (SCREEN_WIDTH, SCREEN_HEIGHT) = (1125, 786)
        self.TARGET_FPS = 60
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.finished = False
        self.delta_time: float = 0

        self.world_center: np.ndarray = np.array([
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            0,
            1,
        ], dtype='float32')

        # define cube
        self.cube_expand: bool = False
        self.cube = Cube(
            position=self.world_center,
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
        # rotate cube
        angle = 0.3 * self.delta_time
        self.cube.rotation[0] += angle  # rotate x
        # self.cube.rotation[1] += angle  # rotate y
        self.cube.rotation[2] += angle  # rotate z

        # scale cube
        # scale_factor = math.sin(time.time()) + 2
        # self.cube.scale[0] = scale_factor
        # self.cube.scale[1] = scale_factor
        # self.cube.scale[2] = scale_factor

        # translate cube
        translation = math.sin(time.time()) * 5
        self.cube.position[0] = self.world_center[0] + translation

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
