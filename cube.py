import pygame
from pygame import Color
from transformation import Transformation
import numpy as np
from color import Colors


class Cube:
    def __init__(self, position: np.ndarray, size: int = 50, color: Color = Colors.GREEN, point_radius: float = 5.0):
        self.position: np.ndarray = position
        self.points: np.ndarray = np.array([
            [-size, size, -size, 1],
            [size, size, -size, 1],
            [size, -size, -size, 1],
            [-size, -size, -size, 1],
            [-size, size, size, 1],
            [size, size, size, 1],
            [size, -size, size, 1],
            [-size, -size, size, 1],
        ], dtype='float32')
        self.color = color
        self.point_radius: float = point_radius
        self.rotation: np.ndarray = np.array([0, 0, 0], dtype='float32')  # angle values for x, y and z

    def draw(self, surface: pygame.Surface):
        for point in self.points:
            rotated_point = Transformation.rotation_matrix(self.rotation).dot(point)
            point = self.position + rotated_point[:2]
            pygame.draw.circle(surface, self.color, point[:2], self.point_radius)
            # pygame.draw.line(surface, self.color, point[:2], neighbor_point[:2], width=1)
