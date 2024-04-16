"""
Module: canvas

This module contains the Canvas class for rendering Collatz sequence visualizations.

Classes:
    - Canvas
"""
import objects.rectangle_object
from objects.rectangle_object import *
from objects.debugger import *
from funktions import *


class Canvas:
    """
    A class for managing and rendering Collatz sequence visualization elements.

    Attributes:
        - speed (float): Animation speed factor.
        - coordinates (np.array): Current coordinates for rendering objects.
        - sequence_dict (dict): Dictionary containing Collatz sequence information.
        - rectangle_dict (dict): Dictionary containing rectangle objects for each number in the sequence.
        - label_dict (dict): Dictionary containing label objects for each number in the sequence.
        - memory_list (list): List storing visited numbers in the sequence.
        - cluster (VGroup): Group containing clustered objects.
        - knots_list (list): List storing numbers where the cluster transitions.
    """

    def __init__(self, scene, input_dict, debugger_instance):
        """
               Initializes the Canvas object.

               Parameters:
                   - scene (Scene): The scene object to render the canvas.
                   - input_dict (dict): Dictionary containing Collatz sequence information.
                   - debugger_instance (str): Instance of the debugger (currently not used).
        """
        self.speed = 1.2
        self.coordinates = np.array([0, 0, 0])
        self.sequence_dict = input_dict
        self.rectangle_dict = {}
        self.label_dict = {}
        self.memory_list = [4]
        self.cluster = VGroup()
        self.knots_list = []

        # self.debugger = debugger_instance

        for i in self.sequence_dict:
            self.create_objects(i)

        start_triangle(scene, self)
        self.manage_canvas_elements(scene)
        scene.play(scene.camera.frame.animate.move_to(([0, len(self.sequence_dict) * 0.5, 0])))
        scene.play(scene.camera.frame.animate.set(width=len(self.sequence_dict) * 2.5), )
        scene.wait(2)

    def add_sequence(self, key, obj):
        self.sequence_dict[key] = obj

    def add_rectangle(self, key, obj):
        self.rectangle_dict[key] = obj

    def add_label(self, key, obj):
        self.label_dict[key] = obj

    def create_objects(self, index):
        """
                Creates rectangle and label objects for the given index if they don't exist.

                Parameters:
                    - index (int): The index in the Collatz sequence.
        """
        if index not in self.rectangle_dict:
            self.add_rectangle(index, RectangleObject(set_width(index)))
            self.add_label(index, LabelObject(Text(str(index))))
            self.set_label(index)

    def set_label(self, index):
        """
                Sets label position relative to rectangle position.

                Parameters:
                    - index (int): The index in the Collatz sequence.
        """
        current_label = self.label_dict.get(index)
        current_label.move_to(self.rectangle_dict.get(index))
        current_label.add_updater(lambda x: x.move_to(self.rectangle_dict.get(index).get_center()))

    def time_check(self):
        """
                Checks if animation speed needs adjustment based on memory list size.
        """
        if len(self.memory_list) == 8:
            self.speed = 0.5
        elif len(self.memory_list) == 20:
            self.speed = 0.3

    def manage_canvas_elements(self, scene):
        """
                Manages rendering of canvas elements.

                Parameters:
                    - scene (Scene): The scene object for rendering.
        """
        first = True
        for key, value in self.sequence_dict.items():
            if key in [1, 4, 2]:
                continue
            if key not in self.memory_list:
                self.memory_list.append(key)
            self.time_check()
            if len(self.cluster) == 0:
                self.coordinates = ([7, 3, 0])
                scene.play(scene.camera.frame.animate.move_to(self.coordinates), run_time=self.speed)
            else:
                expand_cluster(scene, self.coordinates, self.cluster, self.speed)
            animate_object(scene, key, self, self.speed)
            self.cluster.add(self.rectangle_dict.get(key))
            if value in self.memory_list:
                close_cluster(scene, self, value, self.speed)
                first = True
                continue
            if not first:
                self.knots_list.append(key)
            else:
                first = False
        scene.wait(self.speed / 2)
