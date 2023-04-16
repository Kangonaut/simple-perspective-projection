import numpy as np
import math


class Transformation:
    @staticmethod
    def orthographic_projection_matrix(position: np.ndarray, aspect_ratio: float) -> np.ndarray:
        """
        perform orthographic projection

        algorithm:
         1. map values inside the projection window to range [-1; +1]
         2. just ignore the z-axis

        :param position: position vector
        :param aspect_ratio: screen aspect ratio
        :return: the projection matrix
        """
        return np.array([
            [1 / aspect_ratio, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ])

    @staticmethod
    def perspective_projection_matrix(position: np.ndarray, fov_angle: float, aspect_ratio: float) -> np.ndarray:
        """
        perform perspective projection

        algorithm:
         1. map values inside the projection window to range [-1; +1]
         2. project point onto the projection window (distant points will appear further away)

        :param position: position vector
        :param fov_angle: field-of-view angle
        :param aspect_ratio: screen aspect ratio
        :return: the projection matrix
        """
        z_near = 1 / math.tan(fov_angle / 2)
        z_pos = position[2]

        return np.array([
            [z_near / (aspect_ratio * z_pos), 0, 0, 0],
            [0, z_near / z_pos, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ])

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
