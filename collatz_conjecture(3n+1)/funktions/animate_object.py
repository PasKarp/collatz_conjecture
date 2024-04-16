"""
Module: animate_object

This module provides a function to animate the appearance of an object in the scene.

Functions:
    - animate_object
"""
from manim import *


def animate_object(scene, index, canvas, speed=1.5):
    """
    Parameters:
        - scene (Scene): The scene object to render the animation.
        - index (int): The index of the object in the Collatz sequence.
        - canvas (Canvas): The Canvas object containing the objects to animate.
        - speed (float, optional): The animation speed factor. Defaults to 1.5.
    """
    current_rectangle = canvas.rectangle_dict.get(index)
    current_rectangle.shift(canvas.coordinates)
    scene.play(DrawBorderThenFill(current_rectangle, run_time=speed))
    scene.play(GrowFromCenter(canvas.label_dict[index], run_time=speed))
