"""
Module: shift_cluster

This module provides a function to calculate the shift value for clustering objects.

Functions:
    - shift_cluster
"""


def shift_cluster(tracker):
    """
    Parameters:
        - tracker (int): The tracker value indicating the position of the cluster.

    Returns:
        - result (float): The calculated shift value for clustering objects.
    """
    if tracker == 1:
        result = 2
    else:
        result = 2 + (tracker - 1) / 2
    return result
