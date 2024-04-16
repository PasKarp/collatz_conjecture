"""
Module: calc_arrow

This module provides a function to calculate the position for an arrow given start and end points.

Functions:
    - calc_arrow
"""
import numpy as np


def calc_arrow(start, end):
    """
    Parameters:
        - start (np.array): The start point of the arrow.
        - end (np.array): The end point of the arrow.

    Returns:
        - result (np.array): The calculated position for the arrow.
    """
    s0 = start[0]
    s1 = start[1]
    e0 = end[0]
    e1 = end[1]
    x = (s0 - e0) * 0.15
    y = (s1 - e1) * 0.15
    result = np.array([x, y, 0])
    return result
