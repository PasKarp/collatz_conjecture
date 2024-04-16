"""
Module: set_width

This module provides a function to set the width of a rectangle based on the index in the Collatz sequence.

Functions:
    - set_width
"""


def set_width(index):
    """
    Parameters:
        - index (int): The index of the number in the Collatz sequence.

    Returns:
        - width (float): The width of the rectangle corresponding to the index.
    """
    if len(str(index)) == 1:
        return len(str(index))
    else:
        return 0.7 * len(str(index))
