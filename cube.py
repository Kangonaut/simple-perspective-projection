import pygame
from pygame import Color
from transformation import Transformation
import numpy as np
from color import Colors


class Cube:
    def __init__(self, position: np.ndarray, size: int = 50, color: Color = Colors.GREEN, point_radius: float = 5.0,
                 line_width: int = 1):
        self.position: np.ndarray = position
        self.rotation: np.ndarray = np.array([0, 0, 0], dtype='float32')  # angle values for x, y and z
        self.scale: np.ndarray = np.array([1, 1, 1], dtype='float32')

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
        self.line_width: int = line_width

    def draw(self, surface: pygame.Surface):
        projected_points = []
        for point in self.points:
            point = Transformation.scale_matrix(self.scale).dot(point)  # scale
            point = Transformation.rotation_matrix(self.rotation).dot(point)  # rotate
            point = Transformation.translation_matrix(self.position).dot(point)  # translate
            final_point = point[:2]

            projected_point = final_point[:2]

            projected_points.append(final_point)
            pygame.draw.circle(surface, self.color, projected_point, self.point_radius)

        # draw lines
        for idx in range(0, 4):
            # front square
            start = projected_points[idx]
            end = projected_points[(idx + 1) % 4]
            pygame.draw.line(surface, self.color, start, end, width=self.line_width)

            # back square
            start = projected_points[idx + 4]
            end = projected_points[((idx + 1) % 4) + 4]
            pygame.draw.line(surface, self.color, start, end, width=self.line_width)

            # connection between the squares
            start = projected_points[idx]
            end = projected_points[idx + 4]
            pygame.draw.line(surface, self.color, start, end, width=self.line_width)
