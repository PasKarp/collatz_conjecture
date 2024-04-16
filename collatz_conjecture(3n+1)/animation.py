"""
Module: collatz_sequence

This module provides functions related to generating and updating Collatz sequences.

Dependencies:
    - Manim: The library used for rendering animations.
    - objects.canvas: Module containing the Canvas class for drawing.
    - funktions: Module containing various utility functions for managing Collatz sequences.
"""

from manim import *
from objects.canvas import Canvas
from funktions import *

# from objects.debugger import Debugger

input_dict = {1: 4, 4: 2, 2: 1, 3: 10, 10: 5, 5: 16, 16: 8, 8: 4, 6: 3, 7: 22, 22: 11, 11: 34, 34: 17, 17: 52, 52: 26,
              26: 13, 13: 40, 40: 20, 20: 10, 9: 28, 28: 14, 14: 7, 12: 6, 15: 46, 46: 23, 23: 70, 70: 35, 35: 106,
              106: 53, 53: 160, 160: 80, 80: 40, 18: 9}


class DynamicCameraScene(MovingCameraScene):
    """
    A scene class for rendering a dynamic canvas.

    Attributes:
        - camera (Camera): The camera used for rendering.
        - input_dict (dict): Dictionary containing Collatz sequence information.
    """
    def construct(self):
        """
                Method to construct the scene.
                """
        # Set background color
        self.camera.background_color = DARKER_GREY

        # debugger_instance = Debugger(self)

        # Create canvas object with input dictionary
        Canvas(self, input_dict, debugger_instance='None')
