"""
Module: arrow_object

This module defines the ArrowObject class for creating arrows in animations.

Classes:
    - ArrowObject
"""
from manim import *


class ArrowObject(VGroup):
    """
    A class for creating arrows between two points in animations.

    Attributes:
        - arrow (Arrow): The arrow object.
    """
    def __init__(self, start_point, end_point, **kwargs):
        """
        Initializes the ArrowObject.

        Parameters:
            - start_point (np.array): The start point of the arrow.
            - end_point (np.array): The end point of the arrow.
            - **kwargs: Additional arguments for customizing the arrow.
        """
        super().__init__(**kwargs)

        self.arrow = Arrow(start=start_point, end=end_point, color=GRAY_B)
        self.add(self.arrow)
