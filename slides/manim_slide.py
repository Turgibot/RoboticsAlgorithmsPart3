from manim import *

import os
import shutil
import numpy as np
import cv2

config.video_dir= "../video_slides"
config.notes_dir= "../notes"
config.flush_cache = True
config.disable_caching = True

class SlideScene(Scene):
    breaks=[0]
    video_slides_dir=config.video_dir
    notes_dir=config.notes_dir
    def setup(self):
        super(SlideScene, self).setup()
        self.breaks=[0]

    def slide_break(self,t=0.5):
        self.breaks+=[self.renderer.time+t/2]
        self.wait(t)

    def save_times(self):
        self.breaks+=[self.renderer.time]
        out=""
        dirname=os.path.dirname(self.renderer.file_writer.movie_file_path)
        for i in range(len(self.breaks)-1):
            out+=f"<p class=\"fragment\" type='video' time_start={self.breaks[i]} time_end={self.breaks[i+1]}></p>\n"
        with open("%s/%s.txt"%(dirname,type(self).__name__),'w') as f:
            f.write(out)

    def copy_files(self):
        if self.video_slides_dir !=None:
            dirname=os.path.dirname(self.renderer.file_writer.movie_file_path)
            slide_name = type(self).__name__
            if not os.path.exists(self.video_slides_dir):
                os.makedirs(self.video_slides_dir)
            shutil.copy2(os.path.join(dirname,"%s.mp4"%slide_name), self.video_slides_dir)
            shutil.copy2(os.path.join(dirname,"%s.txt"%slide_name), self.video_slides_dir)

    def tear_down(self):
        super(SlideScene, self).tear_down()
        self.save_times()

    def print_end_message(self):
        super(SlideScene, self).print_end_message()
        self.copy_files()
    
    def create_note(self, note="Nothing to say"):
        out=""
        dirname=self.notes_dir
        if not os.path.exists(dirname):
                os.makedirs(dirname)
        out=f'<aside class="notes">%s</aside>\n'%(note)
        with open("%s/%s.txt"%(dirname,type(self).__name__),'w') as f:
            f.write(out)


class MyBullets:
     def __new__(self, isNumbered=False, latex_grp=None, size=0):
        bullets = VGroup(latex_grp[0])
        if isNumbered:
            bul = Text("1. ")
            bullets[0].add_to_back(bul.next_to(bullets[0], LEFT, SMALL_BUFF).align_to(bullets[0], bullets[0].get_center()).shift(UP*0.05+LEFT*0.7))

        else:
            bul = MathTex("\\cdot ").scale(2)
            bullets[0].add_to_back(bul.next_to(bullets[0], LEFT, SMALL_BUFF).align_to(bullets[0], bullets[0].get_center()).shift(LEFT*0.12))

        for i in range(1, size):
            bullets+=latex_grp[i].set_buffer(0)
            if isNumbered:
                bul = Text(str(i+1)+". ")
                bul.next_to(bullets[i], LEFT).shift(UP*0.05+LEFT*0.5)
            else:
                bul = MathTex("\\cdot").scale(2)
                bul.next_to(bullets[i], LEFT, MED_SMALL_BUFF).align_to(bullets[i], bullets[i].get_center())
            bullets[i].add_to_back(bul)

        return bullets.arrange(DOWN, aligned_edge=LEFT, buff=0.7)