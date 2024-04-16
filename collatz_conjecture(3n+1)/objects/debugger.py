"""
Module: debugger

This module defines the Debugger class for displaying debug information.

Classes:
    - Debugger
"""
from objects.label_object import *


class Debugger:
    """
    Attributes:
        - debugger_label (LabelObject): The label object for displaying debug information.
    """
    def __init__(self, scene):
        """
        Initializes the Debugger.

        Parameters:
            - scene (Scene): The scene object to display the debugger label on.
        """
        self.debugger_label = LabelObject(Text(f"{0} {0}"))
        self.debugger_label.move_to(([3, 0, 0]))
        scene.add(self.debugger_label)

    def update_debugger(self, scene, coordinates, value):
        """
        Updates the debugger label with new information.

        Parameters:
            - scene (Scene): The scene object.
            - coordinates (np.array): The coordinates to display.
            - value: The value to display.
        """
        offset = np.array([3, 0, 0])
        if isinstance(value, list):
            x_value, y_value = value[:2]
            scene.play(Transform(self.debugger_label, Text(f"{x_value} {y_value}")))
        else:
            scene.play(Transform(self.debugger_label, Text(str(value))))
        scene.play(self.debugger_label.animate.move_to(coordinates + offset))
        scene.wait(1)
