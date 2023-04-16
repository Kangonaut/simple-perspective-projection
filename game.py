import math
import pygame
from color import Colors
from cube import Cube
import numpy as np
import time


class GameManager:

    def __init__(self) -> None:
        pygame.init()
        self.SCREEN_DIM = (self.SCREEN_WIDTH, self.SCREEN_HEIGHT) = (1125, 786)
        self.TARGET_FPS = 60
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.finished = False
        self.delta_time: float = 0

        self.world_center: np.ndarray = np.array([
            0,  # self.SCREEN_WIDTH / 2,
            0,  # self.SCREEN_HEIGHT / 2,
            0,
            1,
        ], dtype='float32')

        # define cube
        self.cube_expand: bool = False
        self.cube = Cube(
            position=np.array([
                0,
                0,
                5,  # z-axis displacement
                1,
            ], dtype='float32'),
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
        self.cube.rotation[1] += angle  # rotate y
        # self.cube.rotation[2] += angle  # rotate z

        # scale cube
        scale_factor = (math.sin(time.time()) + 2)
        self.cube.scale[0] = scale_factor
        self.cube.scale[1] = scale_factor
        self.cube.scale[2] = scale_factor

        # translate cube
        translation = math.sin(time.time())
        # self.cube.position[0] = self.world_center[0] + translation
        # self.cube.position[1] = self.world_center[1] + translation

    def __draw(self) -> None:
        self.screen.fill(Colors.BLACK)

        # draw cube
        fov_angle = math.pi / 2
        aspect_ratio = self.SCREEN_WIDTH / self.SCREEN_HEIGHT
        self.cube.draw(self.screen, fov_angle, self.SCREEN_WIDTH, self.SCREEN_HEIGHT)

        pygame.display.flip()

    def run(self) -> None:
        while not self.finished:
            self.delta_time = self.clock.get_time() / 1000

            self.__handle_input()
            self.__update()
            self.__draw()

            self.clock.tick(self.TARGET_FPS)  # VSYNC
