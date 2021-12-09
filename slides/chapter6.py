from OPU import *
from manim_slide import MyBullets



class Chap6_00(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem", color=BLUE).next_to(title, DOWN).scale(0.4)
        # img = ImageMobject('../images/rob.jpg').scale(0.7).shift(DOWN*1.3)
 
        bullets = VGroup()
        bullets+= Text(r"Inverse kinnematics is the most important problem in the field of robotics.")
        bullets+= Text(r"Recall that in forward kinematics we calculated the configuration of the EE for a given set of joint positions.")
        bullets+= Text(r"In the inverse kinematics problem, we need to find the joint positions, given a desired EE configuration.")
        
        blist = MyBullets(latex_grp=bullets, size=3, isNumbered=False).scale(0.27).shift(UP)
        self.add(title, secondary_title, blist)

        self.wait()

class Chap6_01(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem", color=BLUE).next_to(title, DOWN).scale(0.4)
        # img = ImageMobject('../images/rob.jpg').scale(0.7).shift(DOWN*1.3)
 
        bullets = VGroup()
        bullets+= Text(r"Inverse kinnematics is the most important problem in the field of robotics.")
        bullets+= Text(r"Recall that in forward kinematics we calculated the configuration of the EE for a given set of joint positions.")
        bullets+= Text(r"In the inverse kinematics problem, we need to find the joint positions, given a desired EE configuration.")
        
        blist = MyBullets(latex_grp=bullets, size=3, isNumbered=False).scale(0.27).shift(UP)
        self.add(title, secondary_title, blist)

        mask = Rectangle(color=WHITE, width=2.2, height=1.5, fill_color=WHITE, fill_opacity=1).shift(DOWN*1.5+RIGHT*1.3)
        ball = Circle(radius=0.15, color=ORANGE, fill_color=ORANGE, fill_opacity=1).shift(DOWN*0.6)
        
        cap = cv2.VideoCapture("../media/videos/ik.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        for _ in range(1) :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.4).shift(DOWN*1.4)
                self.add(frame_img,mask)
                self.wait(0.042)
                self.remove(frame_img,mask)
        self.add(frame_img,mask,ball)
        
        cap.release()

        self.wait()

class Chap6_02(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem", color=BLUE).next_to(title, DOWN).scale(0.4)
        # img = ImageMobject('../images/rob.jpg').scale(0.7).shift(DOWN*1.3)
 
        bullets = VGroup()
        bullets+= Text(r"Inverse kinnematics is the most important problem in the field of robotics.")
        bullets+= Text(r"Recall that in forward kinematics we calculated the configuration of the EE for a given set of joint positions.")
        bullets+= Text(r"In the inverse kinematics problem, we need to find the joint positions, given a desired EE configuration.")
        
        blist = MyBullets(latex_grp=bullets, size=3, isNumbered=False).scale(0.27).shift(UP)
        self.add(title, secondary_title, blist)

        mask = Rectangle(color=WHITE, width=2.2, height=1.5, fill_color=WHITE, fill_opacity=1).shift(DOWN*1.5+RIGHT*1.3)
        ball = Circle(radius=0.15, color=ORANGE, fill_color=ORANGE, fill_opacity=1).shift(DOWN*0.6)
        
        cap = cv2.VideoCapture("../media/videos/ik.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
        # for _ in range(10) :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.4).shift(DOWN*1.4)
                self.add(frame_img,mask,ball)
                self.wait(0.042)
                self.remove(frame_img,mask,ball)
        self.add(frame_img,mask,ball)
        
        cap.release()

        self.wait()




class Chap6_03(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("IK problem definition", color=BLUE).next_to(title, DOWN).scale(0.4)


        txt1= Tex(r"A more formal definition of the problem is:").scale(0.5)
        txt2= Tex(r"For a general n degree-of-freedom open chain with forward kinematics $T(\theta)$, where $\theta\in\mathbb{R}^n$,").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"The inverse kinematics problem can be stated as follows:").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        # txt4= Tex(r"Given a homogeneous transform $X \in SE(3)$ ,").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"Given a homogeneous transform $X \in SE(3)$ ,").scale(0.5).next_to(txt3, DOWN)
        # txt5= Tex(r"Find solutions $\theta$ that satisfy $T(\theta)=X$ .").scale(0.5).next_to(txt4, DOWN).align_to(txt1, LEFT)
        txt5= Tex(r"Find solutions $\theta$ that satisfy $T(\theta)=X$ .").scale(0.5).next_to(txt4, DOWN).align_to(txt4, LEFT)
        # txt6= Tex(r"At a singularity, a robotic arm loses one or more degrees of freedom.").scale(0.5).next_to(txt5, DOWN).align_to(txt1, LEFT)
        
        grp = VGroup(txt1, txt2, txt3, txt4, txt5).center()
        self.add(title, secondary_title, grp)
        self.wait()



class Chap6_04(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Motivational example", color=BLUE).next_to(title, DOWN).scale(0.4)


        txt1= Tex(r"A more formal definition of the problem is:").scale(0.5)
        txt2= Tex(r"For a general n degree-of-freedom open chain with forward kinematics $T(\theta)$, where $\theta\in\mathbb{R}^n$,").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"The inverse kinematics problem can be stated as follows:").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        # txt4= Tex(r"Given a homogeneous transform $X \in SE(3)$ ,").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"Given a homogeneous transform $X \in SE(3)$ ,").scale(0.5).next_to(txt3, DOWN)
        # txt5= Tex(r"Find solutions $\theta$ that satisfy $T(\theta)=X$ .").scale(0.5).next_to(txt4, DOWN).align_to(txt1, LEFT)
        txt5= Tex(r"Find solutions $\theta$ that satisfy $T(\theta)=X$ .").scale(0.5).next_to(txt4, DOWN).align_to(txt4, LEFT)
        # txt6= Tex(r"At a singularity, a robotic arm loses one or more degrees of freedom.").scale(0.5).next_to(txt5, DOWN).align_to(txt1, LEFT)
        
        grp = VGroup(txt1, txt2, txt3, txt4, txt5).center()
        self.add(title, secondary_title, grp)
        self.wait()
