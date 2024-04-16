"""
Module: start_triangle

This module provides a function to animate the initial triangle formation in the scene.

Functions:
    - start_triangle
"""
from funktions.animate_object import animate_object
from funktions.add_arrow import add_arrow


def start_triangle(scene, canvas):
    """
    Parameters:
        - scene (Scene): The scene object to render the animation.
        - canvas (Canvas): The Canvas object containing the objects to animate.
    """
    temp = list(canvas.sequence_dict.keys())[:3]
    one = ([-1.5, 0, 0])
    four = ([0, 2.1, 0])
    two = ([1.5, 0, 0])
    canvas.coordinates = one
    animate_object(scene, temp[0], canvas)
    add_arrow(scene, one, four)
    canvas.coordinates = four
    animate_object(scene, temp[1], canvas)
    add_arrow(scene, four, two)
    canvas.coordinates = two
    animate_object(scene, temp[2], canvas)
    add_arrow(scene, two, one)
