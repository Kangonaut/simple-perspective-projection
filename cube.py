import math

import pygame
from pygame import Color
from transformation import Transformation
import numpy as np
from color import Colors


class Cube:
    def __init__(self, position: np.ndarray, color: Color = Colors.GREEN, point_radius: float = 5.0,
                 line_width: int = 1):
        self.position: np.ndarray = position
        self.rotation: np.ndarray = np.array([0, 0, 0], dtype='float32')  # angle values for x, y and z
        self.scale: np.ndarray = np.array([1, 1, 1], dtype='float32')

        self.points: np.ndarray = np.array([
            [-0.5, 0.5, -0.5, 1],
            [0.5, 0.5, -0.5, 1],
            [0.5, -0.5, -0.5, 1],
            [-0.5, -0.5, -0.5, 1],
            [-0.5, 0.5, 0.5, 1],
            [0.5, 0.5, 0.5, 1],
            [0.5, -0.5, 0.5, 1],
            [-0.5, -0.5, 0.5, 1],
        ], dtype='float32')

        self.color = color
        self.point_radius: float = point_radius
        self.line_width: int = line_width

    def draw(self, surface: pygame.Surface, fov_angle, width, height):
        aspect_ratio: float = width / height

        projected_points = []
        for point in self.points:
            point = Transformation.scale_matrix(self.scale).dot(point)  # scale
            point = Transformation.rotation_matrix(self.rotation).dot(point)  # rotate
            point = Transformation.translation_matrix(self.position).dot(point)  # translate
            point = Transformation.perspective_projection_matrix(point, fov_angle, aspect_ratio).dot(point)  # project (perspective)
            # point = Transformation.orthographic_projection_matrix(point, aspect_ratio).dot(point)  # project (orthigraphic)

            # convert to screen point
            # 1. ignore remove z-axis
            screen_point = point[:2]
            # 2. map range [-1, 1] to the screen width and height
            screen_point[0] = (point[0] + 1) / 2 * width
            screen_point[1] = (point[1] + 1) / 2 * height

            projected_points.append(screen_point)
            pygame.draw.circle(surface, self.color, screen_point, self.point_radius)

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
