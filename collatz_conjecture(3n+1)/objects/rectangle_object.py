"""
Module: rectangle_object

This module defines the RectangleObject class for creating rectangles in animations.

Classes:
    - RectangleObject
"""
from manim import *


class RectangleObject(VGroup):
    """
    A class for creating rectangles in animations.
    """
    def __init__(self, width, **kwargs):
        """
        Initializes the RectangleObject.

        Parameters:
            - width (float): The width of the rectangle.
            - **kwargs: Additional arguments for customizing the rectangle.
        """
        super().__init__(**kwargs)
        self.RoundedRectangle = RoundedRectangle(z_index=-1, stroke_width=4, stroke_color=GRAY_A, fill_color=BLUE_D,
                                                 fill_opacity=0.5, width=width, height=1)
        self.add(self.RoundedRectangle)
