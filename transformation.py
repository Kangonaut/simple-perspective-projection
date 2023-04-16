import numpy as np
import math


class Transformation:
    @staticmethod
    def translation_matrix(position: np.ndarray) -> np.ndarray:
        """
        translate according to the given `position` vector

        :param position: position vector
        :return: the translation matrix
        """
        return np.array([
            [1, 0, 0, position[0]],
            [0, 1, 0, position[1]],
            [0, 0, 1, position[2]],
            [0, 0, 0, 1],
        ])

    @staticmethod
    def scale_matrix(scale: np.ndarray) -> np.ndarray:
        """
        scale according to the scale factors in the `scale` vector

        :param scale: vector containing the scale factors
        :return: the rotation matrix
        """
        return np.array([
            [scale[0], 0, 0, 0],
            [0, scale[1], 0, 0],
            [0, 0, scale[2], 0],
            [0, 0, 0, 1],
        ])

    @staticmethod
    def rotation_matrix(rotation: np.ndarray) -> np.ndarray:
        """
        rotate according to the angles (rad) provided in the `rotation` vector

        :param rotation: a vector containing the angles (rad) of rotation
        :return: the rotation matrix
        """
        x_rotation_matrix = Transformation.x_rotation_matrix(rotation[0])
        y_rotation_matrix = Transformation.y_rotation_matrix(rotation[1])
        z_rotation_matrix = Transformation.z_rotation_matrix(rotation[2])
        return x_rotation_matrix.dot(y_rotation_matrix).dot(z_rotation_matrix)

    @staticmethod
    def z_rotation_matrix(angle: float) -> np.ndarray:
        """
        rotate around the z-axis

        :param angle: the angle (rad) of rotation
        :return: the rotation matrix
        """
        return np.array([
            [math.cos(angle), -math.sin(angle), 0, 0],
            [math.sin(angle), math.cos(angle), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ])

    @staticmethod
    def y_rotation_matrix(angle: float) -> np.ndarray:
        """
        rotate around the y-axis

        :param angle: the angle (rad) of rotation
        :return: the rotation matrix
        """
        return np.array([
            [math.cos(angle), 0, -math.sin(angle), 0],
            [0, 1, 0, 0],
            [math.sin(angle), 0, math.cos(angle), 0],
            [0, 0, 0, 1],
        ])

    @staticmethod
    def x_rotation_matrix(angle: float) -> np.ndarray:
        """
        rotate around the x-axis

        :param angle: the angle (rad) of rotation
        :return: the rotation matrix
        """
        return np.array([
            [1, 0, 0, 0],
            [0, math.cos(angle), -math.sin(angle), 0],
            [0, math.sin(angle), math.cos(angle), 0],
            [0, 0, 0, 1],
        ])
