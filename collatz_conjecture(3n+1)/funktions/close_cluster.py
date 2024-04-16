"""
Module: close_cluster

This module provides a function to close the current cluster and transition to the next in the scene.

Functions:
    - close_cluster
"""
from manim import *
from funktions.sort_cluster import sort_cluster
from funktions.shift_cluster import shift_cluster
from funktions.add_arrow import add_arrow


def close_cluster(scene, canvas, value, speed):
    """
    Parameters:
        - scene (Scene): The scene object to render the animation.
        - canvas (Canvas): The Canvas object containing the cluster to close.
        - value: The value used to close the cluster.
        - speed (float): The animation speed factor.
    """
    coordinates = canvas.rectangle_dict.get(value).get_center()
    scene.play(scene.camera.frame.animate.move_to(coordinates), run_time=speed)
    count = canvas.knots_list.count(value)
    canvas.knots_list.append(value)
    coordinates[0] += sort_cluster(count)
    coordinates[1] += shift_cluster(len(canvas.cluster))

    # canvas.debugger.update_debugger(scene, canvas.rectangle_dict.get(value).get_center(), len(canvas.cluster))

    scene.play(canvas.cluster.animate.move_to(coordinates), run_time=speed)
    add_arrow(scene, coordinates - ([0, (len(canvas.cluster) - 1) / 2, 0]),
              canvas.rectangle_dict.get(value).get_center(), speed)
    canvas.cluster = VGroup()
    scene.wait(speed/2)
    return canvas.cluster
