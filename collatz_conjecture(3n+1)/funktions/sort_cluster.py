"""
Module: sort_cluster

This module provides a function to calculate the sorting value for clustering objects.

Functions:
    - sort_cluster
"""


def sort_cluster(tracker):
    """
    Parameters:
        - tracker (int): The tracker value indicating the position of the cluster.

    Returns:
        - result (float): The calculated sorting value for clustering objects.
    """
    if tracker == 0:
        return 0
    result = 0
    if tracker == 1:
        return -2
    if tracker % 2 == 0:
        a = 2
    else:
        a = -2
    for c in range(round(tracker / 2)):
        result += a
    return result
