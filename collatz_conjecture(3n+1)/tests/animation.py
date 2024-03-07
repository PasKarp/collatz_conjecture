from manim import *

sequence_dict = {1: 4}
rectangle_list = []


class RectangleObject(VGroup):
    def __init__(self, width, **kwargs):
        super().__init__(**kwargs)
        self.RoundedRectangle = RoundedRectangle(stroke_width=4, stroke_color=GRAY_A, fill_color=BLUE_D,
                                                 fill_opacity=0.5, width=width, height=1)
        self.add(self.RoundedRectangle)


class ArrowObject(VGroup):
    def __init__(self, start_point, end_point, **kwargs):
        super().__init__(**kwargs)
        self.arrow = Arrow(start=start_point, end=end_point, color=GRAY_B)
        self.add(self.arrow)


class Animation(Scene):
    def construct(self):
        self.camera.background_color = DARKER_GREY
        for current_number, next_number in sequence_dict.items():
            self.execute(current_number, next_number)

    def execute(self, c_num, n_num):
        current_width = self.set_width(c_num)
        next_width = self.set_width(n_num)
        current_label = self.txt(c_num)
        current_rectangle = RectangleObject(width=current_width)
        rectangle_list.insert(c_num, current_rectangle)
        current_label.move_to(current_rectangle)
        current_label.add_updater(lambda x: x.move_to(current_rectangle.get_center()))

        next_label = self.txt(n_num)
        next_rectangle = RectangleObject(width=next_width)
        rectangle_list.insert(n_num, next_rectangle)
        next_label.move_to(next_rectangle)
        next_label.add_updater(lambda mob: mob.move_to(next_rectangle.get_center()))

        self.play(DrawBorderThenFill(current_rectangle))
        self.play(GrowFromCenter(current_label))
        self.play(current_rectangle.animate.shift(UP * 3), run_time=1)

        pointer = Arrow(current_rectangle, next_rectangle.get_top(), color=GRAY_B)
        self.play(GrowArrow(pointer))

        self.play(DrawBorderThenFill(next_rectangle))
        self.play(GrowFromCenter(next_label))
        pointer.add_updater(lambda mob: mob.move_to(next_rectangle.get_top()))
        self.play(next_rectangle.animate.shift(LEFT * 2), run_time=1)
        return

    def set_width(self, rec_l):
        if len(str(rec_l)) == 1:
            return len(str(rec_l))
        else:
            return 0.7 * len(str(rec_l))

    def txt(self, txt):
        return Text(str(txt), color=WHITE)
