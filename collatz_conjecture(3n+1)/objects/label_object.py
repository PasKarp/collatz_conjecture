"""
Module: label_object

This module defines the LabelObject class for creating labels in animations.

Classes:
    - LabelObject
"""
from manim import *


class LabelObject(VGroup):
    """
    A class for creating labels in animations.
    """
    def __init__(self, text, **kwargs):
        """
                Initializes the LabelObject.

                Parameters:
                    - text: The text to display in the label.
                    - **kwargs: Additional arguments for customizing the label.
        """
        super().__init__(text, color=WHITE, **kwargs)
