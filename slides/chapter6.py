from manim.mobject.mobject import T
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
        img = ImageMobject('../images/ik_wolf.png').scale(1).shift(DOWN*1)


        txt1= Tex(r"Let use Wolfram player to look at a 2 link planar arm:").scale(0.5).next_to(img, UP)
       
        
        self.add(title, secondary_title, img, txt1)
        self.wait()



class Chap6_05(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("IK problem definition", color=BLUE).next_to(title, DOWN).scale(0.4)


        txt1= Tex(r"before moving in make sure you are familiar with ...").scale(0.5).shift(UP*1.5)
        txt2= Tex(r"The law of cosines:").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"The inverse kinematics problem can be stated as follows:").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"Given a homogeneous transform $X \in SE(3)$ ,").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        txt5= Tex(r"Find solutions $\theta$ that satisfy $T(\theta)=X$ .").scale(0.5).next_to(txt4, DOWN).align_to(txt1, LEFT)
        txt6= Tex(r"The atan2\(y,x\) function:").scale(0.5).next_to(txt5, DOWN).align_to(txt1, LEFT)
        

        img1 = ImageMobject('../images/cosines.png').scale(0.5).next_to(txt1, DOWN)
        img2 = ImageMobject('../images/atan21.png').scale(0.9).next_to(img1, RIGHT)
        img3 = ImageMobject('../images/atan2.png').scale(0.2).next_to(img2, RIGHT)
        grp = Group(img1, img3, img2).center()
        self.add(title, secondary_title, txt1, grp)
        self.wait()




class Chap6_06(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("IK problem definition", color=BLUE).next_to(title, DOWN).scale(0.4)


        txt1= Tex(r"Find the possible configuration for a given EE location.").scale(0.5).shift(UP*1.5)
        txt2= Tex(r"The law of cosines:").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"The inverse kinematics problem can be stated as follows:").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"Given a homogeneous transform $X \in SE(3)$ ,").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        txt5= Tex(r"Find solutions $\theta$ that satisfy $T(\theta)=X$ .").scale(0.5).next_to(txt4, DOWN).align_to(txt1, LEFT)
        txt6= Tex(r"The atan2\(y,x\) function:").scale(0.5).next_to(txt5, DOWN).align_to(txt1, LEFT)
        

        img1 = ImageMobject('../images/workspace.png').scale(1).next_to(txt1, DOWN)
        img2 = ImageMobject('../images/alpha.png').scale(1).next_to(img1, RIGHT).shift(UP*1.5)
        img3 = ImageMobject('../images/beta.png').scale(1).next_to(img2, DOWN).align_to(img2, LEFT)
        txt= Tex(r"$\gamma = atan2(y,x)$").scale(0.4).next_to(img3, DOWN).align_to(img2, LEFT)
        img4 = ImageMobject('../images/opt1.png').scale(1).next_to(txt, DOWN).align_to(img2, LEFT)
        img5 = ImageMobject('../images/opt2.png').scale(1).next_to(img4, DOWN).align_to(img2, LEFT)

        grp = Group(img1.shift(LEFT*0.5), img3, img2,txt).center().shift(DOWN)
        self.add(title, secondary_title, txt1, grp)
        self.wait()


class Chap6_07(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("IK problem definition", color=BLUE).next_to(title, DOWN).scale(0.4)


        txt1= Tex(r"Find the possible configuration for a given EE location.").scale(0.5).shift(UP*1.5)
        txt2= Tex(r"The law of cosines:").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"The inverse kinematics problem can be stated as follows:").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"Given a homogeneous transform $X \in SE(3)$ ,").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        txt5= Tex(r"Find solutions $\theta$ that satisfy $T(\theta)=X$ .").scale(0.5).next_to(txt4, DOWN).align_to(txt1, LEFT)
        txt6= Tex(r"The atan2\(y,x\) function:").scale(0.5).next_to(txt5, DOWN).align_to(txt1, LEFT)
        

        img1 = ImageMobject('../images/workspace.png').scale(1).next_to(txt1, DOWN)
        
        img4 = ImageMobject('../images/opt1.png').scale(1.2).next_to(img1, RIGHT).shift(UP)
        txt= Tex(r"elbow-down configuration", color=GREEN).scale(0.4).next_to(img4, UP)
        txti= Tex(r"elbow-up configuration", color=GREEN).scale(0.4).next_to(img4, DOWN)
        img5 = ImageMobject('../images/opt2.png').scale(1.2).next_to(txti, DOWN)

        grp = Group(img4, img5, img1, txt, txti).center().shift(DOWN)
        self.add(title, secondary_title, grp, txt1)
        self.wait()



class Chap6_08(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("6.1 Analytic Inverse Kinematics", color=BLUE).next_to(title, DOWN).scale(0.4)


        img1 = ImageMobject('../images/pumabegin.png').scale(1).next_to(secondary_title, DOWN)
    
        self.add(title, secondary_title, img1)
        cap = cv2.VideoCapture("../media/videos/puma.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag:
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.4).shift(DOWN*1.4)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
        self.add(frame_img)
        
        cap.release()

        self.wait()




class Chap6_09(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("6.1.1 Analytic Inverse Kinematics of a 6R PUMA-type arm", color=BLUE).next_to(title, DOWN).scale(0.4)

        txt = Tex(r"The inverse kinematics problem for PUMA-type arms can be decoupled into inverse-position and inverse-orientation subproblems. Starting with the solution of the inverse position subproblem.").scale(0.5).shift(UP*1.5)

        img1 = ImageMobject('../images/pumaxyz.png').scale(1).next_to(txt, DOWN).shift(LEFT*3+DOWN*0.7)
        
        self.add(title, secondary_title, img1, txt)


        self.wait()



class Chap6_10(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("6.1.1 Analytic Inverse Kinematics of a 6R PUMA-type arm", color=BLUE).next_to(title, DOWN).scale(0.4)

        txt = Tex(r"Solving the inverse position subproblem.").scale(0.5).shift(UP*1.5)

        img1 = ImageMobject('../images/pumaxyz.png').scale(1).next_to(txt, DOWN).shift(LEFT*3+DOWN*0.7)
        
        self.add(title, secondary_title, img1, txt)

        txt1= Tex(r"The EE is at $p\in\mathbb{R}^3 , p = (p_x,p_y,p_z)$.").scale(0.45).shift(UP*0.45+RIGHT*2)
        txt2= Tex(r"Then $\theta_1 = atan2(p_y, p_x)$").scale(0.45).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"Note that a second valid solution for $\theta_1$ is given by:").scale(0.45).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"$\theta_1 = atan2(p_y, p_x)+\pi$").scale(0.45).next_to(txt3, DOWN).align_to(txt1, LEFT)
        self.add(txt1, txt2, txt3, txt4)
        self.wait()



class Chap6_11(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("6.1.1 Analytic Inverse Kinematics of a 6R PUMA-type arm", color=BLUE).next_to(title, DOWN).scale(0.4)

        txt = Tex(r"Solving the inverse position subproblem.").scale(0.5).shift(UP*1.5)

        img1 = ImageMobject('../images/pumaxyz.png').scale(1).next_to(txt, DOWN).shift(LEFT*3+DOWN*0.7)
        
        self.add(title, secondary_title, img1, txt)

        txt1= Tex(r"If there is an offset $d \ne 0$ , then in general there will be two solutions for $\theta_1$, the righty and lefty solutions.").scale(0.45).shift(UP*0.45+RIGHT*3)
        txt2= Tex(r"Then $\theta_1 = \phi-\alpha$ where $\alpha = atan2(d, \sqrt{r^2-d^2})$").scale(0.45).next_to(txt1, DOWN).align_to(txt1, LEFT+[0.2, 0, 0])
        txt3= Tex(r"The second solution for $\theta_1$ is given by:").scale(0.45).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"$\theta_1 = \pi + atan2(p_y, p_x)+atan2(-\sqrt{p_x^2+p_y^2-d^2}, d)$").scale(0.45).next_to(txt3, DOWN).align_to(txt1, LEFT)
        self.add(txt1, txt2, txt3, txt4)
        self.wait()



class Chap6_11(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("6.1.1 Analytic Inverse Kinematics of a 6R PUMA-type arm", color=BLUE).next_to(title, DOWN).scale(0.4)

        txt = Tex(r"Solving the inverse position subproblem.").scale(0.5).shift(UP*1.5)

        img1 = ImageMobject('../images/offset.png').scale(0.9).next_to(txt, DOWN).shift(LEFT*3.2+DOWN*0.7)
        
        self.add(title, secondary_title, img1, txt)

        txt1= Tex(r"If there is an offset $d_1 \ne 0$ , then in general there will be two solutions for $\theta_1$, the righty and lefty solutions.").scale(0.45).shift(UP*0.45+RIGHT*3)
        txt2= Tex(r"Then $\theta_1 = \phi-\alpha$ where $\alpha = atan2(d_1, \sqrt{r^2-d_1^2}), \phi=atan2(p_y, p_x)$").scale(0.45).next_to(txt1, DOWN).align_to(txt1, LEFT+[1, 0, 0])
        txt3= Tex(r"The second solution for $\theta_1$ is given by:").scale(0.45).next_to(txt2, DOWN).align_to(txt2, LEFT)
        txt4= Tex(r"$\theta_1 = \pi + atan2(p_y, p_x)+atan2(-\sqrt{p_x^2+p_y^2-d_1^2}, d_1)$").scale(0.45).next_to(txt3, DOWN).align_to(txt2, LEFT)
        self.add(txt1, txt2, txt3, txt4)
        self.wait()


class Chap6_12(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("6.1.1 Analytic Inverse Kinematics of a 6R PUMA-type arm", color=BLUE).next_to(title, DOWN).scale(0.4)

        txt = Tex(r"Solving the inverse position subproblem.").scale(0.5).shift(UP*1.5)

        img1 = ImageMobject('../images/options.png').scale(0.8).next_to(txt, DOWN).shift(LEFT*3+DOWN*0.7)
        img2 = ImageMobject('../images/theta34.png').scale(1).next_to(img1, RIGHT).shift(UP*0.7)
        img3 = ImageMobject('../images/theta4.png').scale(1).next_to(img2, DOWN).align_to(img2, LEFT)
        
        self.add(title, secondary_title, img1.shift(LEFT*0.3), img2, img3, txt)

        self.wait()


class Chap6_13(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("6.1.1 Analytic Inverse Kinematics of a 6R PUMA-type arm", color=BLUE).next_to(title, DOWN).scale(0.4)

        txt = Tex(r"Solving the inverse orientation subproblem.").scale(0.5).shift(UP*1.5)

        img1 = ImageMobject('../images/or1.png').scale(1).next_to(txt, DOWN)
        img2 = ImageMobject('../images/or2.png').scale(1).next_to(img1, DOWN)
        img3 = ImageMobject('../images/or3.png').scale(1).next_to(img2, DOWN)
        
        self.add(title, secondary_title, img1, img2, txt)

        self.wait()



class Chap6_14(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("6.1.1 Analytic Inverse Kinematics of a 6R PUMA-type arm", color=BLUE).next_to(title, DOWN).scale(0.4)

        txt = Tex(r"Solving the inverse orientation subproblem.").scale(0.5).shift(UP*1.5)

        img1 = ImageMobject('../images/or1.png').scale(1).next_to(txt, DOWN)
        img2 = ImageMobject('../images/or2.png').scale(1).next_to(img1, DOWN)
        img3 = ImageMobject('../images/or3.png').scale(0.8).shift(DOWN)
        
        self.add(title, secondary_title, img3, txt)

        self.wait()


class Chap6_15(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 6: Inverse Kinematics").shift(UP*3).scale(0.65)
        secondary_title = Text("6.2 Numerical Inverse Kinematics", color=BLUE).next_to(title, DOWN).scale(0.4)
        self.add(title, secondary_title)


        txt1= Tex(r"Iterative numerical methods can be applied if the inverse kinematics equations do not admit analytic solutions.").scale(0.45).shift(UP*1.4)
        txt2= Tex(r"Even in cases where an analytic solution does exist, numerical methods are often used to improve the accuracy of these solutions.").scale(0.45).next_to(txt1, DOWN).align_to(txt1, LEFT+[0.2, 0, 0])
        txt3= Tex(r"We will make use of an approach fundamental to nonlinear root-finding, the Newton–Raphson method.").scale(0.45).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"We will deal with corner cases where an exact solution may not exist and we seek the closest approximate solution; or, conversely, an infinity of inverse kinematics solutions exists (i.e., if the robot is kinematically redundant)\
                and we seek a solution that is optimal with respect to some criterion.").scale(0.45).next_to(txt3, DOWN).align_to(txt1, LEFT)

        self.add(txt1, txt2, txt3, txt4)

        self.wait()

