from manim_slide import *
from datetime import date

class OPU_Slide(SlideScene):
    def add_info(self):
        today = date.today()
        ou_img = ImageMobject('../images/ou_logo_full_inverted.jpeg').scale(0.4).shift(3*UP+6.3*LEFT)
        name = Text("Guy Tordjman").scale(0.25).shift(3.3*DOWN+6.1*LEFT)
        lecture = Text("Algorithmic Robotics "+str(today.year), color=BLUE).scale(0.25).shift(3.3*DOWN+5.3*RIGHT)
        self.add(ou_img, name, lecture)

    def add_frame(self, name='s', position=[0,0,0], rotation=0):
        fx = Vector(color=GREEN, stroke_width=2, max_tip_length_to_length_ratio=0.2)
        fy = Vector(direction=UP, color=RED, stroke_width=2, max_tip_length_to_length_ratio=0.2)
        
        frame_ = VGroup(fx, fy)
        center = frame_.get_center()
        frame_orig = frame_.get_left()
        frame_.move_to(position+(center))
        frame_.rotate(rotation*DEGREES, about_point=position)
        x = Tex(r"$\hat{x}_"+name+"$", color=GREEN).scale(0.5).next_to(fx, RIGHT).shift(LEFT*0.2+DOWN*0.2)
        y = Tex(r"$\hat{y}_"+name+"$", color=RED).scale(0.5).next_to(fy, LEFT).shift(UP*0.4+RIGHT*0.2)
        frame_+=x
        frame_+=y
        self.add(frame_)
        return frame_

    def add_vector_to_frame(self, start, end, color):
        v = Arrow(start=start+0.1*DOWN, end=end, stroke_width=2, max_tip_length_to_length_ratio=0.2, color=color)
        self.add(v)
        return v
