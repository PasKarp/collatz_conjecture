"""
Module: expand_cluster

This module provides a function to expand the cluster of objects in the scene.

Functions:
    - expand_cluster
"""
from funktions.add_arrow import add_arrow


def expand_cluster(scene, coordinates, cluster, speed=1):
    """
    Parameters:
        - scene (Scene): The scene object to render the animation.
        - coordinates (np.array): The coordinates to expand the cluster to.
        - cluster (VGroup): The cluster of objects to expand.
        - speed (float, optional): The animation speed factor. Defaults to 1.

    Returns:
        - coordinates (np.array): The updated coordinates after expansion.
    """
    previous = coordinates.copy()
    coordinates[1] -= 2
    scene.play(scene.camera.frame.animate.move_to(coordinates), run_time=speed)
    cluster.add(add_arrow(scene, previous, coordinates, speed))
    return coordinates
