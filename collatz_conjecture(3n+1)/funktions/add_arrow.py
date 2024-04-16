"""
Module: add_arrow

This module provides a function to add arrows between two points in the scene.

Functions:
    - add_arrow
"""
from manim import GrowArrow
from funktions.calc_arrow import calc_arrow
from objects.arrow_object import ArrowObject


def add_arrow(scene, start, end, speed=1):
    """
    Parameters:
        - scene (Scene): The scene object to render the arrow.
        - start (np.array): The start point of the arrow.
        - end (np.array): The end point of the arrow.
        - speed (float, optional): The animation speed factor. Defaults to 1.

    Returns:
        - arrow (ArrowObject): The arrow object added to the scene.
    """
    temp = calc_arrow(start, end)
    start -= temp
    end += temp
    arrow = ArrowObject(start, end)
    scene.play(GrowArrow(arrow.arrow, run_time=speed))
    return arrow
