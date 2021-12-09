from OPU import *
from manim_slide import MyBullets



class Chap4_00(OPU_Slide):
   def construct(self):
        note = "בוא נעשה סקירה קצרה של החומר שלמדנו בקורס עד כה:\
                התחלנו בלדבר על קונפיגורציות ודרגות חופש של גופים קשיחים.\
                        המשכנו לדבר על תנועה של גוף קשיחי והתייחסנו לייצוג של רוטציה באמצעות מטריצות רוטציה ואז באמצעות קואורדינטות אקפוננציאליות.\
                                 ואת המפגש האחרון סיימנו בעצם כשדיברנו על מטריצות טרנפורמציה שמשלבות ייצוג של רוטציה וטרנסלציה ואז הגענו לדבר על ייצוג בורג והשתמשנו בו בייצוג הקואורדינטות האקספוננציאליות של קונפיגורציה. \
                                         היום נלמד נושא חשוב ומעניין שנקרא פורוורד קינמטיקס. קינמטיקס מתייחס לתנועה של גופים ומערכות ואילו המילה פורוורד מתארת את הגישה החישובית.\
                                                 מה שאנחנו בעצם מחשבים הוא את המיקום והאוריאנטציה של האנד אפקטור באמצעות הנתונים מהג'וינטס של הרובוט."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Roadmap : ", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/bluebot.jpg').scale(0.99).shift(DOWN*1.3)
 
        bullets = VGroup()
        bullets+= Text(r"Configuration space, joint, links, DOF, grublers formula, task and workspaces ...")
        bullets+= Text(r"Rigid body motion, rotation matrices, twist, transformation matrices, screw motion, exponential coordinates")
        bullets+= Text(r"Today: Forward kinematics - the calculation of the position and orientation of the EE from its joint coordinates")
        
        blist = MyBullets(latex_grp=bullets, size=3, isNumbered=True).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist, img)
        self.wait()


class Chap4_01(OPU_Slide):
   def construct(self):
        note = "פורוורד קינמטיקס מוגדר להיות הבעיה הבאה:\
                 בהינתן משתני המפרקים - מהו המיקום והאוריאנטציה של האנד אפקטור של הרובוט? \
                         במילים אחרות נרצה למפות את הטטות (משתני המפרקים) לקונפיגורציה של האא."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*2)
        img1 = ImageMobject('../images/fk0.png').scale(1.1).next_to(img, RIGHT)

        self.add(title, secondary_title, prob, img, img1)
        self.wait()


class Chap4_02(OPU_Slide):
   def construct(self):
        note = "קיימים מספר פתרונות לבעיה כאשר הפתרון הראשון שנדון בו הוא הפתרון הטריגונומטרי.\
                אפשר לחשב את איקס כסכומי הקוסנוסים את ט כסכומי הסינוסים ואת הזוית של האא כסכומי הטטות."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*2)
        sol1 = Text("Solution 1: Trigonometrically", color=GREEN).scale(0.3).next_to(img, RIGHT).shift(UP*1.5)
        img1 = ImageMobject('../images/tig.png').scale(1.5).next_to(sol1, DOWN).align_to(sol1, LEFT)

        

        self.add(title, secondary_title, prob, img, sol1, img1)
        self.wait()

class Chap4_03(OPU_Slide):
   def construct(self):
        note = "אבל מה אם המערכת אותה אנחנו מנסים לנתח היא בעלת מספר רב של דרגות חופש?\
                 פה הפתרון הטריגונומטרי הופך להיות מסובך ומסורבל וכפי שכבר ראינו ניתן בעצם לפתור את העיה בעזרת מכפלה של מטריצות טרנספורמציה."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/fk1.png').scale(0.8).shift(DOWN*1+LEFT*2)
        sol1 = Text("Solution 1: Trigonometrically", color=GREEN).scale(0.3).next_to(img, RIGHT).shift(UP*1.5)
        img1 = Text("?", color=RED).scale(3).next_to(sol1, DOWN)

        

        self.add(title, secondary_title, prob, img, sol1, img1)
        self.wait()

class Chap4_04(OPU_Slide):
   def construct(self):
        note = "אז מה אנחנו צריכים בכדי לפתור את הבעיה בעצם? ראינו שניתן לבטא רוטציה ומיקום של כל מסגרת ביחס למסגרת אחרת אז ננסה לבטא את מסגרת האא ביחס למסגרת הבסיס"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*2)

        self.add(title, secondary_title, prob, img)
        self.wait()


class Chap4_05(OPU_Slide):
   def construct(self):
        note = "טי 04 היא הטרנפורמציה הרצויה שמתקבלת ממכפלה של כל הטרנפורמציות בנקודות 0 עד 4. כלומר מ0 ל1 מ1 ל2 וכן הלאה עד 4 . היום אנחנו נכיר את שיטת דנביט הרטנברג שבאמצעותה אנחנו יכולים לייצר טרנפורמציות הומוגניות מרחבית מ4 פרמטרים בלבד. בעוד שאנחנו יודעים שבשביל לייצג קונפיגורציה של גוף קשיח המספר המינימלי של פרמטרים הוא 6.  "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*2)
        sol1 = Text("Solution 2: Transformation matrix multiplication", color=GREEN).scale(0.3).next_to(img, RIGHT).shift(UP*1.5)
        img1 = ImageMobject('../images/t04.png').scale(1.4).next_to(sol1, DOWN)
        img2 = ImageMobject('../images/t04mat.png').scale(1.3).next_to(img1, DOWN).align_to(sol1, LEFT)

        self.add(title, secondary_title, prob, img, sol1, img1, img2)
        self.wait()

class Chap4_06(OPU_Slide):
   def construct(self):
        note = " השיטה השנייה שאותה נלמד היום נקראת שיטת מכפלת האקספוננטים. שמשתמשת בייצוג בורג כדי לפתור את הפורוורד קינמטיקס.\
                 השיטה הזאת מודרנית ויש לה יתרון מהותי על השיטה הקודמת.\
                          הספר מתמקד בפיאואי שכן הספר הוא מודרן-רובוטיקס אבל לא ללמד את שיטת די אייטש זה ממש חטא בקורס רובוטיקה בסיסי. די איטש מופיע בנספח סי בסוף הספר."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem : ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"Given a set of joint variables $\theta$, what is the configuration of the EE?", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*2)
        sol1 = Text("Solution 3: Product of Exponentials", color=GREEN).scale(0.3).next_to(img, RIGHT).shift(UP*1.5)
        img1 = ImageMobject('../images/poe0.png').scale(1.4).next_to(sol1, DOWN)
        img2 = ImageMobject('../images/poe1.png').scale(1.3).next_to(img1, DOWN)
        self.add(title, secondary_title, prob, img, sol1, img1, img2)
        self.wait()

class Chap4_07(OPU_Slide):
   def construct(self):
        note = "אז בוא נתחיל ללמוד את שתי השיטות - חשוב לומר שאנחנו פותרים את בעיית הפ.ק. עבור רובוטים מסוג אופן ציין כאשר אנחנו דנים בשני סוגים של ג'וינטים - רוולוט ופריזמטיק - \
                וזאת מכיון שאנחנו מבינים משילוב של מספר ג'וינטי רוולוט ניתן לייצר מפרקים מורכבים יותר."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("In this chapter ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        prob = Tex(r"We only deal with open chain robots where the joints to consider are:", color=RED).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/joints.png').scale(0.7).shift(DOWN*1.1)
        jnt = Text("Joint Types", color=GREEN).scale(0.3).next_to(img, LEFT).shift(DOWN*0.5)
        

        self.add(title, secondary_title, prob, img, jnt)
        self.wait()




#Denavit Hartenberg Parameters

class DH_00(OPU_Slide):
   def construct(self):
        note = "1שיטת ד.ה. בעצם בנויה מ4 שלבים. נעבור עליהם לפי הסדר. 1 2 3 4. נתחיל ב"
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("F.K. using D.H. method:", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        bullets = VGroup()
        bullets+= Text(r"Assign frames according to the D.H. convention rules")
        bullets+= Text(r"Create the D.H. parameters table.")
        bullets+= Text(r"Plug the table values into the corresponding H.T.M.")
        bullets+= Text(r"Multiply the H.T.M together in order")
        
        blist = MyBullets(latex_grp=bullets, size=4, isNumbered=True).scale(0.3).shift(UP)
        self.add(title, secondary_title, blist)
        self.wait()

class DH_01(OPU_Slide):
   def construct(self):
        note = "אז מה שאנחנו מתבקשים לעשות זה להוסיף מסגרת לכל ג'וינט. ניתן אינקס אי לג'וינט אי מינוס אחד לג'וינט הקודם לו. בין שני הג'וינטים כמובן שיש לינק. כמו שציינתי בשיטה הזאת נצליח לבנות טרנספורמציות באמצעות 4 פרטרים בלבד. \
                מה שיקרה זה בעצם שאנחנו נגביל את הרוטציה והטרנפורמציה לצירי האיקס והזד בלבד. בשביל לעשות זאת אנחנו חייבים למקם את המסגרות על כל ג'וינט לפי סט של חוקים:"
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)

        self.add(title, secondary_title, img, ll, lr)
        self.wait()


class DH_02(OPU_Slide):
   def construct(self):
        note = "החוק הראשון אומר שציר הסיבוב בחיובי הוא ציר הזד."
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.123)

        self.add(title, secondary_title, img, ll, lr, rule1, rule11)
        self.wait()


class DH_03(OPU_Slide):
   def construct(self):
        note = "ואם מדובר בג'וינט פריזמטי אז ציר הזד הוא עם הכיוון החיובי של תנועת הג'וינט."
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.123)
        zl = Arrow(start=[-4,-1,0], end=[-3.55,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)
        self.wait()

class DH_04(OPU_Slide):
   def construct(self):
        note = "החוק השני מדבר על ראשית הצירים של המסגרת האי מינוס 1. שימו לב שמה שמעניין אותנו זוהי הקונפיגורציה של האא והמסגרות הן נקודות בדרך. אז כדי לחסוך בפרמטרים אנחנו נרצה למקם את המסגרות בצורה אופטימלית."
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/prismatic1.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
       
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4.5,-0.5,0], end=[-2.9,0.45,0], color=RED)
        zr = Arrow(start=[-4.5,-0.53,0], end=[-2.9,0.45,0], color=RED).shift(RIGHT*1.13)
        zl_ = Tex(r"$\hat{z}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2)
        zr_ = Tex(r"$\hat{z}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, rule1, rule11, zl, zr, zl_, zr_)
        self.wait()

class DH_05(OPU_Slide):
   def construct(self):
        note = " החוק אומר למצוא ישר אורטוגונלי לשני צירי הג'וינטים ולמקם את ראשית בצירים של הג'וינט האי מינוס אחד בנקודת החיבור - העברנו ישר אורטוגונלי"
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"1. Set the Z axis:", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4,-1,0], end=[-3.55,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)

        rule2 = Tex(r"Rule 2:", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"Set the origin of the link by finding the line that orthogonally intersects both joint axis.").scale(0.4).next_to(rule2, RIGHT).shift(DOWN*0.123)
        self.add(rule2, rule21)

        self.wait()

class DH_06(OPU_Slide):
   def construct(self):
        note = "ראשית הצירים של הג'וינט האי מינוס אחד עכשיו בנקודת החיבור של הישר עם הציר"
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"1. Set the Z axis:", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4,-1,0], end=[-3.55,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)

        rule2 = Tex(r"Rule 2:", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"Set the origin of the link by finding the line that orthogonally intersects both joint axis.").scale(0.4).next_to(rule2, RIGHT).shift(DOWN*0.123)
        self.add(rule2, rule21)

        orthogonal = Line(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE)
        nl = Line(start=[-4.2,-1.4,0], end=[-4.06,-1.38,0], stroke_width=2.1, color=BLUE)
        nl1 = Line(start=[-4.06,-1.38,0], end=[-4.03,-1.48,0], stroke_width=2.1, color=BLUE)
        nr = Line(start=[-2.1,-1.2,0], end=[-1.94,-1.18,0], stroke_width=2.1, color=BLUE)
        nr1 = Line(start=[-2.1,-1.2,0], end=[-2.08,-1.31,0], stroke_width=2.1, color=BLUE)
        self.play(Create(orthogonal),Create(nl), Create(nl1), Create(nr), Create(nr1))
        self.wait()

class DH_07(OPU_Slide):
   def construct(self):
        note = "ראשית הצירים של הג'וינט האי מינוס אחד עכשיו בנקודת החיבור של הישר עם הציר"
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"1. Set the Z axis:", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2+LEFT*0.05)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)

        rule2 = Tex(r"Rule 2:", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"Set the origin of the link by finding the line that orthogonally intersects both joint axis.").scale(0.4).next_to(rule2, RIGHT).shift(DOWN*0.123)
        self.add(rule2, rule21)

        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE)
       
        self.add(orthogonal)
        zim1 = VGroup(zl, zl_)
        self.play(zim1.animate.move_to([-4.14,-1.12,0]))
        self.wait()

class DH_08(OPU_Slide):
   def construct(self):
        note = "שני מצבי קצה יכולים לקרות : הראשון הוא שהישרים מקבילים ואז נבחר את הקומפיגורציה העדיפה שתגרום לאיפוס של כמה שיותר פרמטרים. אנחנו לא יודעים מהם הפרמטרים אז לא לדאוג עוד נראה דוגמה לכך \
                ומקרה קצה שני מדבר על שני צירים שנחתכים ולכן לא קיימים ישר אורתוגונלי - במקרה כזה נקודת החיתוך של הצירים היא ראשית הצירים של המסגרת האי מינוס אחת. "
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"1. Set the Z axis:", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2+LEFT*0.05)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)

        rule2 = Tex(r"Rule 2:", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"Set the origin of the link by finding the line that orthogonally intersects both joint axis.\\\
                 - If the axis are parallel choose the best option (minimal param values).\\\
                        - If the axis cross set the origin at the crossing point.").scale(0.4).next_to(rule2, RIGHT).shift(DOWN*0.37)
        self.add(rule2, rule21)

        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE)
       
        zim1 = VGroup(zl, zl_)
        zim1.move_to([-4.14,-1.12,0])
        self.add(orthogonal, zim1)

        self.wait()

class DH_09(OPU_Slide):
   def construct(self):
        note = "החוק השלישי פשוט ואומר שאת ציר האיקס ממקמים עם כיוון הישר האורטוגונלי בכיוון מאי מינוס אחד לאי"
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"1. Set the Z axis:", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2+LEFT*0.05)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)

        rule2 = Tex(r"Rule 2:", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"Set the origin of the link by finding the line that orthogonally intersects both joint axis.\\\
                 - If the axis are parallel choose the best option (minimal param values).\\\
                        - If the axis cross set the origin at the crossing point.").scale(0.4).next_to(rule2, RIGHT).shift(DOWN*0.37)
        self.add(rule2, rule21)

        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE)
       
        zim1 = VGroup(zl, zl_)
        zim1.move_to([-4.14,-1.12,0])
        self.add(orthogonal, zim1)

        rule3 = Tex(r"Rule 3:", color=RED).scale(0.4).next_to(rule21, DOWN).align_to(rule2, LEFT)
        rule31 = Tex(r"Set the $\hat{x}_{i-1}$ axis in the direction of the mutually perpendicular line from the (i-1) axis to the i axis.").scale(0.4).next_to(rule3, RIGHT).shift(DOWN*0.123)
        self.add(rule3, rule31)

        self.wait()

class DH_10(OPU_Slide):
   def construct(self):
        note = "במידה ולא קיים ישר - זה קורה כי הצירים נחתכים ואז ציר האיקס אורטוגונלי למישור שנפרס על ידי שני הצירים"
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"1. Set the Z axis:", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2+LEFT*0.05)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)

        rule2 = Tex(r"Rule 2:", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"Set the origin of the link by finding the line that orthogonally intersects both joint axis.\\\
                 - If the axis are parallel choose the best option (minimal param values).\\\
                        - If the axis cross set the origin at the crossing point.").scale(0.4).next_to(rule2, RIGHT).shift(DOWN*0.37)
        self.add(rule2, rule21)

        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE)
       
        zim1 = VGroup(zl, zl_)
        zim1.move_to([-4.14,-1.12,0])
        self.add(orthogonal, zim1)

        rule3 = Tex(r"Rule 3:", color=RED).scale(0.4).next_to(rule21, DOWN).align_to(rule2, LEFT)
        rule31 = Tex(r"Set the $\hat{x}_{i-1}$ axis in the direction of the mutually perpendicular line from the (i-1) axis to the i axis.").scale(0.4).next_to(rule3, RIGHT).shift(DOWN*0.123)
        self.add(rule3, rule31)
        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.play(Create(x), Create(x_))


class DH_11(OPU_Slide):
   def construct(self):
        note = "במידה ולא קיים ישר - זה קורה כי הצירים נחתכים ואז ציר האיקס אורטוגונלי למישור שנפרס על ידי שני הצירים"
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"1. Set the Z axis:", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2+LEFT*0.05)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)

        rule2 = Tex(r"Rule 2:", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"Set the origin of the link by finding the line that orthogonally intersects both joint axis.\\\
                 - If the axis are parallel choose the best option (minimal param values).\\\
                        - If the axis cross set the origin at the crossing point.").scale(0.4).next_to(rule2, RIGHT).shift(DOWN*0.37)
        self.add(rule2, rule21)

        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE)
       
        zim1 = VGroup(zl, zl_)
        zim1.move_to([-4.14,-1.12,0])
        self.add(orthogonal, zim1)

        rule3 = Tex(r"Rule 3:", color=RED).scale(0.4).next_to(rule21, DOWN).align_to(rule2, LEFT)
        rule31 = Tex(r"Set the $\hat{x}_{i-1}$ axis in the direction of the mutually perpendicular line from the (i-1) axis to the i axis.\\- If the pependicular line doesn't exist choose $\hat{x}_{i-1}$ to be perpendicular to the plane spanned by $\hat{z}_{i-1}$ and $\hat{z}_{i}$.").scale(0.4).next_to(rule3, RIGHT).shift(DOWN*0.4)
        self.add(rule3, rule31)
        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)
        self.wait()


class DH_12(OPU_Slide):
   def construct(self):
        note = "החוק הרביעי בעצם קובע את ציר הוואי כתוצאת המכפלה הקרטזית או במילים פשוטות לפי חוק יד ימין. "
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"1. Set the Z axis:", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2+LEFT*0.05)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)

        rule2 = Tex(r"Rule 2:", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"Set the origin of the link by finding the line that orthogonally intersects both joint axis.\\\
                 - If the axis are parallel choose the best option (minimal param values).\\\
                        - If the axis cross set the origin at the crossing point.").scale(0.4).next_to(rule2, RIGHT).shift(DOWN*0.37)
        self.add(rule2, rule21)

        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE)
       
        zim1 = VGroup(zl, zl_)
        zim1.move_to([-4.14,-1.12,0])
        self.add(orthogonal, zim1)

        rule3 = Tex(r"Rule 3:", color=RED).scale(0.4).next_to(rule21, DOWN).align_to(rule2, LEFT)
        rule31 = Tex(r"Set the $\hat{x}_{i-1}$ axis in the direction of the mutually perpendicular line from the (i-1) axis to the i axis.\\- If the pependicular line doesn't exist choose $\hat{x}_{i-1}$ to be perpendicular to the plane spanned by $\hat{z}_{i-1}$ and $\hat{z}_{i}$.").scale(0.4).next_to(rule3, RIGHT).shift(DOWN*0.4)
        self.add(rule3, rule31)
        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)

        rule4 = Tex(r"Rule 4:", color=RED).scale(0.4).next_to(rule31, DOWN).align_to(rule2, LEFT)
        rule41 = Tex(r"Determine the $\hat{y}_{i-1}$ axis from the cross product equasion $\hat{y}_{i-1} = \hat{z}_{i-1}\times\hat{x}_{i-1}$.").scale(0.4).next_to(rule4, RIGHT).shift(DOWN*0.026)
        self.add(rule4, rule41)
        self.wait()

class DH_13(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Frame assignment:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"1. Set the Z axis:", color=RED).scale(0.4).shift(UP+LEFT*0.5)
        rule1 = Tex(r"Rule 1: ", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"The $\hat{z}_i$ axis coincides with joint axis i and the $\hat{z}_{i-1}$ axis coincides with joint axis $i-1$.\\\
                For prismatic joints, the $\hat{z}$-direction of the link reference frame is along the positive direction of translation.").scale(0.4).next_to(rule1, RIGHT).shift(DOWN*0.36)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.2+LEFT*0.05)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)

        rule2 = Tex(r"Rule 2:", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"Set the origin of the link by finding the line that orthogonally intersects both joint axis.\\\
                 - If the axis are parallel choose the best option (minimal param values).\\\
                        - If the axis cross set the origin at the crossing point.").scale(0.4).next_to(rule2, RIGHT).shift(DOWN*0.37)
        self.add(rule2, rule21)

        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE)
       
        zim1 = VGroup(zl, zl_)
        zim1.move_to([-4.14,-1.12,0])
        self.add(orthogonal, zim1)

        rule3 = Tex(r"Rule 3:", color=RED).scale(0.4).next_to(rule21, DOWN).align_to(rule2, LEFT)
        rule31 = Tex(r"Set the $\hat{x}_{i-1}$ axis in the direction of the mutually perpendicular line from the (i-1) axis to the i axis.\\- If the pependicular line doesn't exist choose $\hat{x}_{i-1}$ to be perpendicular to the plane spanned by $\hat{z}_{i-1}$ and $\hat{z}_{i}$.").scale(0.4).next_to(rule3, RIGHT).shift(DOWN*0.4)
        self.add(rule3, rule31)
        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)

        rule4 = Tex(r"Rule 4:", color=RED).scale(0.4).next_to(rule31, DOWN).align_to(rule2, LEFT)
        rule41 = Tex(r"Determine the $\hat{y}_{i-1}$ axis from the cross product equasion $\hat{y}_{i-1} = \hat{z}_{i-1}\times\hat{x}_{i-1}$.").scale(0.4).next_to(rule4, RIGHT).shift(DOWN*0.026)
        self.add(rule4, rule41)

        y = Arrow(start=[-4.13,-1.73,0], end=[-4.53,-0.83,0], stroke_width=2.1, color=GREEN)
        y_ = Tex(r"$\hat{y}_{i-1}$", color=GREEN).scale(0.35).next_to(y, LEFT).shift(RIGHT*0.2+UP*0.3)

        self.add(y,y_)
        self.wait()


class DH_14(OPU_Slide):
   def construct(self):
        note = "אז אחרי שמיקמנו את המסגרות ואת מערכות הצירים שלהם לכל ג'וינט . השיטה מגדירה 4 פרמטרים אותם נצטרך לחישוב הפ.ק. לכל ג'וינט. הפרמטר הראשון .:\
                איי מינוס אחד הוא הלינק לנגט' - האורך של הישר האורטוגונלי. "
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("The 4 parameters:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"$a_{i-1}$", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"is the link length, which is the length of the mutually perpendicular line $\hat{a}_{i-1}$.").scale(0.4).next_to(rule1, RIGHT)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.4+RIGHT*0.33)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)


        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE).add_tip(tip_length=0.1)
        nl = Line(start=[-4.2,-1.4,0], end=[-4.06,-1.38,0], stroke_width=2.1, color=BLUE)
        nl1 = Line(start=[-4.06,-1.38,0], end=[-4.03,-1.48,0], stroke_width=2.1, color=BLUE)
        nr = Line(start=[-2.1,-1.2,0], end=[-1.94,-1.18,0], stroke_width=2.1, color=BLUE)
        nr1 = Line(start=[-2.1,-1.2,0], end=[-2.08,-1.31,0], stroke_width=2.1, color=BLUE)
        self.add(nl, nl1, nr, nr1)
        zim1 = VGroup(zl, zl_)
        zim1.move_to([-3.94,-1.22,0])
        self.add(orthogonal, zim1)

        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)
        y = Arrow(start=[-4.13,-1.73,0], end=[-4.53,-0.83,0], stroke_width=2.1, color=GREEN)
        y_ = Tex(r"$\hat{y}_{i-1}$", color=GREEN).scale(0.35).next_to(y, LEFT).shift(RIGHT*0.2+UP*0.3)

        self.add(y,y_)

        xr = Arrow(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=2.1, color=DARK_BLUE)
        xr_ = Tex(r"$\hat{x}_{i}$", color=DARK_BLUE).scale(0.35).next_to(xr, RIGHT).shift(DOWN*0.2+LEFT*0.5)
        yr = Arrow(start=[-1.92,-0.9,0], end=[-2.9,-0.35,0], stroke_width=2.1, color=GREEN)
        yr_ = Tex(r"$\hat{y}_{i}$", color=GREEN).scale(0.35).next_to(yr, LEFT).shift(RIGHT*0.2+UP*0.3)
        a = Tex(r"$a_{i-1}$", color=BLUE).scale(0.35).next_to(x, RIGHT).shift(RIGHT*0.4+UP*0.2)

        self.add(xr, xr_, yr, yr_, a)
        self.wait()


class DH_15(OPU_Slide):
   def construct(self):
        note = "הפרמטר השני - אלפא מינוס אחת נקרא הטוויסט - מוגדר להיות הזוית שבה צריך לסובב את מערכת הצירים של אי מינוס אחת סביב ציר האיקס שלו כדי להשוות בין צירי הזד של שתי המסגרות."
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("The 4 parameters:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"$a_{i-1}$", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"is the link length, which is the length of the mutually perpendicular line $\hat{a}_{i-1}$.").scale(0.4).next_to(rule1, RIGHT)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.4+RIGHT*0.33)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)


        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE).add_tip(tip_length=0.1)
        nl = Line(start=[-4.2,-1.4,0], end=[-4.06,-1.38,0], stroke_width=2.1, color=BLUE)
        nl1 = Line(start=[-4.06,-1.38,0], end=[-4.03,-1.48,0], stroke_width=2.1, color=BLUE)
        nr = Line(start=[-2.1,-1.2,0], end=[-1.94,-1.18,0], stroke_width=2.1, color=BLUE)
        nr1 = Line(start=[-2.1,-1.2,0], end=[-2.08,-1.31,0], stroke_width=2.1, color=BLUE)
        self.add(nl, nl1, nr, nr1)

        zim1 = VGroup(zl, zl_)
        zim1.move_to([-3.94,-1.22,0])
        self.add(orthogonal, zim1)

        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)
        y = Arrow(start=[-4.13,-1.73,0], end=[-4.53,-0.83,0], stroke_width=2.1, color=GREEN)
        y_ = Tex(r"$\hat{y}_{i-1}$", color=GREEN).scale(0.35).next_to(y, LEFT).shift(RIGHT*0.2+UP*0.3)

        self.add(y,y_)

        xr = Arrow(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=2.1, color=DARK_BLUE)
        xr_ = Tex(r"$\hat{x}_{i}$", color=DARK_BLUE).scale(0.35).next_to(xr, RIGHT).shift(DOWN*0.2+LEFT*0.5)
        yr = Arrow(start=[-1.92,-0.9,0], end=[-2.9,-0.35,0], stroke_width=2.1, color=GREEN)
        yr_ = Tex(r"$\hat{y}_{i}$", color=GREEN).scale(0.35).next_to(yr, LEFT).shift(RIGHT*0.2+UP*0.3)
        a = Tex(r"$a_{i-1}$", color=BLUE).scale(0.35).next_to(x, RIGHT).shift(RIGHT*0.4+UP*0.2)

        self.add(xr, xr_, yr, yr_, a)

        rule2 = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"is called the link twist, which is the angle from $\hat{z}_{i-1}$ to $\hat{z}_{i}$  measured about $\hat{x}_{i-1}$ .").scale(0.4).next_to(rule2, RIGHT)
        self.add(rule2, rule21)


        self.wait()


class DH_16(OPU_Slide):
   def construct(self):
        note = "נסתכל שוב על האנימציה "
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("The 4 parameters:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"$a_{i-1}$", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"is the link length, which is the length of the mutually perpendicular line $\hat{a}_{i-1}$.").scale(0.4).next_to(rule1, RIGHT)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.4+RIGHT*0.33)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)


        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE).add_tip(tip_length=0.1)
        nl = Line(start=[-4.2,-1.4,0], end=[-4.06,-1.38,0], stroke_width=2.1, color=BLUE)
        nl1 = Line(start=[-4.06,-1.38,0], end=[-4.03,-1.48,0], stroke_width=2.1, color=BLUE)
        nr = Line(start=[-2.1,-1.2,0], end=[-1.94,-1.18,0], stroke_width=2.1, color=BLUE)
        nr1 = Line(start=[-2.1,-1.2,0], end=[-2.08,-1.31,0], stroke_width=2.1, color=BLUE)
        self.add(nl, nl1, nr, nr1)

        zim1 = VGroup(zl, zl_)
        zim1.move_to([-3.94,-1.22,0])
        self.add(orthogonal, zim1)

        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)
        y = Arrow(start=[-4.13,-1.73,0], end=[-4.53,-0.83,0], stroke_width=2.1, color=GREEN)
        y_ = Tex(r"$\hat{y}_{i-1}$", color=GREEN).scale(0.35).next_to(y, LEFT).shift(RIGHT*0.2+UP*0.3)

        self.add(y,y_)

        xr = Arrow(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=2.1, color=DARK_BLUE)
        xr_ = Tex(r"$\hat{x}_{i}$", color=DARK_BLUE).scale(0.35).next_to(xr, RIGHT).shift(DOWN*0.2+LEFT*0.5)
        yr = Arrow(start=[-1.92,-0.9,0], end=[-2.9,-0.35,0], stroke_width=2.1, color=GREEN)
        yr_ = Tex(r"$\hat{y}_{i}$", color=GREEN).scale(0.35).next_to(yr, LEFT).shift(RIGHT*0.2+UP*0.3)
        a = Tex(r"$a_{i-1}$", color=BLUE).scale(0.35).next_to(x, RIGHT).shift(RIGHT*0.4+UP*0.2)

        self.add(xr, xr_, yr, yr_, a)

        rule2 = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"is called the link twist, which is the angle from $\hat{z}_{i-1}$ to $\hat{z}_{i}$  measured about $\hat{x}_{i-1}$ .").scale(0.4).next_to(rule2, RIGHT)
        self.add(rule2, rule21)

        alpha = DashedLine(start=[-3.75,-0.5,0], end=[-4.25,-1.5,0], stroke_width=2.1, color=RED).add_tip(at_start=True,  tip_length=0.1)
        alpha_ = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.3).next_to(zl, UP).shift(DOWN*0.25+LEFT*0.1)
        alpha__ = CurvedArrow(start_point=[-4.1,-1.2,0], end_point=[-4.35,-1.1,0],  color=RED, stroke_width=2, tip_length=0.06)
        # self.add(alpha, alpha_, alpha__)

        # self.wait()

        self.play(alpha.animate().rotate(angle=40*DEGREES, about_point=[-4.25,-1.5,0]), run_time = 2)
        self.play(Create(alpha_), Write(alpha__))


class DH_17(OPU_Slide):
   def construct(self):
        note = " הפרמטר השלישי - נקרא האופסט - הוא בעצם המרחק מנקודת המפגש של הישר עם ציר הסיבוב האיי עד ראשית הצירים של המסגרת האיית."
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("The 4 parameters:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"$a_{i-1}$", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"is the link length, which is the length of the mutually perpendicular line $\hat{a}_{i-1}$.").scale(0.4).next_to(rule1, RIGHT)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.4+RIGHT*0.33)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)


        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE).add_tip(tip_length=0.1)
        nl = Line(start=[-4.2,-1.4,0], end=[-4.06,-1.38,0], stroke_width=2.1, color=BLUE)
        nl1 = Line(start=[-4.06,-1.38,0], end=[-4.03,-1.48,0], stroke_width=2.1, color=BLUE)
        nr = Line(start=[-2.1,-1.2,0], end=[-1.94,-1.18,0], stroke_width=2.1, color=BLUE)
        nr1 = Line(start=[-2.1,-1.2,0], end=[-2.08,-1.31,0], stroke_width=2.1, color=BLUE)
        self.add(nl, nl1, nr, nr1)

        zim1 = VGroup(zl, zl_)
        zim1.move_to([-3.94,-1.22,0])
        self.add(orthogonal, zim1)

        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)
        y = Arrow(start=[-4.13,-1.73,0], end=[-4.53,-0.83,0], stroke_width=2.1, color=GREEN)
        y_ = Tex(r"$\hat{y}_{i-1}$", color=GREEN).scale(0.35).next_to(y, LEFT).shift(RIGHT*0.2+UP*0.3)

        self.add(y,y_)

        xr = Arrow(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=2.1, color=DARK_BLUE)
        xr_ = Tex(r"$\hat{x}_{i}$", color=DARK_BLUE).scale(0.35).next_to(xr, RIGHT).shift(DOWN*0.2+LEFT*0.5)
        yr = Arrow(start=[-1.92,-0.9,0], end=[-2.9,-0.35,0], stroke_width=2.1, color=GREEN)
        yr_ = Tex(r"$\hat{y}_{i}$", color=GREEN).scale(0.35).next_to(yr, LEFT).shift(RIGHT*0.2+UP*0.3)
        a = Tex(r"$a_{i-1}$", color=BLUE).scale(0.35).next_to(x, RIGHT).shift(RIGHT*0.4+UP*0.2)

        self.add(xr, xr_, yr, yr_, a)

        rule2 = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"is called the link twist, which is the angle from $\hat{z}_{i-1}$ to $\hat{z}_{i}$  measured about $\hat{x}_{i-1}$ .").scale(0.4).next_to(rule2, RIGHT)
        self.add(rule2, rule21)

        alpha = DashedLine(start=[-3.75,-0.5,0], end=[-4.25,-1.5,0], stroke_width=2.1, color=RED).add_tip(at_start=True,  tip_length=0.1).rotate(angle=40*DEGREES, about_point=[-4.25,-1.5,0])
        alpha_ = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.3).next_to(zl, UP).shift(DOWN*0.25+LEFT*0.1)
        alpha__ = CurvedArrow(start_point=[-4.1,-1.2,0], end_point=[-4.35,-1.1,0],  color=RED, stroke_width=2, tip_length=0.06)
        self.add(alpha, alpha_, alpha__)

        rule3 = Tex(r"$d_i$:", color=RED).scale(0.4).next_to(rule21, DOWN).align_to(rule2, LEFT)
        rule31 = Tex(r"is the link offset, which is the distance from the intersection of $\hat{x}_{i-1}$ and $\hat{z}_{i}$ to the origin of the link-i frame.").scale(0.4).next_to(rule3, RIGHT).shift(DOWN*0.123)
        self.add(rule3, rule31)

        self.wait()


class DH_18(OPU_Slide):
   def construct(self):
        note = " הפרמטר השלישי - נקרא האופסט - הוא בעצם המרחק מנקודת המפגש של הישר עם ציר הסיבוב האיי עד ראשית הצירים של המסגרת האיית."
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("The 4 parameters:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"$a_{i-1}$", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"is the link length, which is the length of the mutually perpendicular line $\hat{a}_{i-1}$.").scale(0.4).next_to(rule1, RIGHT)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.4+RIGHT*0.33)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)


        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE).add_tip(tip_length=0.1)
        nl = Line(start=[-4.2,-1.4,0], end=[-4.06,-1.38,0], stroke_width=2.1, color=BLUE)
        nl1 = Line(start=[-4.06,-1.38,0], end=[-4.03,-1.48,0], stroke_width=2.1, color=BLUE)
        nr = Line(start=[-2.1,-1.2,0], end=[-1.94,-1.18,0], stroke_width=2.1, color=BLUE)
        nr1 = Line(start=[-2.1,-1.2,0], end=[-2.08,-1.31,0], stroke_width=2.1, color=BLUE)
        self.add(nl, nl1, nr, nr1)

        zim1 = VGroup(zl, zl_)
        zim1.move_to([-3.94,-1.22,0])
        self.add(orthogonal, zim1)

        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)
        y = Arrow(start=[-4.13,-1.73,0], end=[-4.53,-0.83,0], stroke_width=2.1, color=GREEN)
        y_ = Tex(r"$\hat{y}_{i-1}$", color=GREEN).scale(0.35).next_to(y, LEFT).shift(RIGHT*0.2+UP*0.3)

        self.add(y,y_)

        xr = Arrow(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=2.1, color=DARK_BLUE)
        xr_ = Tex(r"$\hat{x}_{i}$", color=DARK_BLUE).scale(0.35).next_to(xr, RIGHT).shift(DOWN*0.2+LEFT*0.5)
        yr = Arrow(start=[-1.92,-0.9,0], end=[-2.9,-0.35,0], stroke_width=2.1, color=GREEN)
        yr_ = Tex(r"$\hat{y}_{i}$", color=GREEN).scale(0.35).next_to(yr, LEFT).shift(RIGHT*0.2+UP*0.3)
        a = Tex(r"$a_{i-1}$", color=BLUE).scale(0.35).next_to(x, RIGHT).shift(RIGHT*0.4+UP*0.2)

        self.add(xr, xr_, yr, yr_, a)

        rule2 = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"is called the link twist, which is the angle from $\hat{z}_{i-1}$ to $\hat{z}_{i}$  measured about $\hat{x}_{i-1}$ .").scale(0.4).next_to(rule2, RIGHT)
        self.add(rule2, rule21)

        alpha = DashedLine(start=[-3.75,-0.5,0], end=[-4.25,-1.5,0], stroke_width=2.1, color=RED).add_tip(at_start=True,  tip_length=0.1).rotate(angle=40*DEGREES, about_point=[-4.25,-1.5,0])
        alpha_ = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.3).next_to(zl, UP).shift(DOWN*0.25+LEFT*0.1)
        alpha__ = CurvedArrow(start_point=[-4.1,-1.2,0], end_point=[-4.35,-1.1,0],  color=RED, stroke_width=2, tip_length=0.06)
        self.add(alpha, alpha_, alpha__)

        rule3 = Tex(r"$d_i$:", color=RED).scale(0.4).next_to(rule21, DOWN).align_to(rule2, LEFT)
        rule31 = Tex(r"is the link offset, which is the distance from the intersection of $\hat{x}_{i-1}$ and $\hat{z}_{i}$ to the origin of the link-i frame.").scale(0.4).next_to(rule3, RIGHT).shift(DOWN*0.123)
        self.add(rule3, rule31)

        di = DashedLine(start=[-1.88,-1.3,0], end=[-2.15,-0.75,0], stroke_width=3.5, color=ORANGE).add_tip(tip_length=0.1)
        di_ = Tex(r"$d_{i}$", color=ORANGE).scale(0.35).next_to(di, LEFT).shift(RIGHT*0.25)

        self.play(Create(di), Write(di_))
        self.wait()


class DH_19(OPU_Slide):
   def construct(self):
        note = "הפרמטר הרביעי והאחרון הוא הזוית פי, שמוגדר להיות הזוית אותה צריך לסובב את איקס של אי מינוס אחת סביב ציר זד של איי כדי שיתלכד עם איקס של איי "
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("The 4 parameters:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"$a_{i-1}$", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"is the link length, which is the length of the mutually perpendicular line $\hat{a}_{i-1}$.").scale(0.4).next_to(rule1, RIGHT)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.4+RIGHT*0.33)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)


        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE).add_tip(tip_length=0.1)
        nl = Line(start=[-4.2,-1.4,0], end=[-4.06,-1.38,0], stroke_width=2.1, color=BLUE)
        nl1 = Line(start=[-4.06,-1.38,0], end=[-4.03,-1.48,0], stroke_width=2.1, color=BLUE)
        nr = Line(start=[-2.1,-1.2,0], end=[-1.94,-1.18,0], stroke_width=2.1, color=BLUE)
        nr1 = Line(start=[-2.1,-1.2,0], end=[-2.08,-1.31,0], stroke_width=2.1, color=BLUE)
        self.add(nl, nl1, nr, nr1)

        zim1 = VGroup(zl, zl_)
        zim1.move_to([-3.94,-1.22,0])
        self.add(orthogonal, zim1)

        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)
        y = Arrow(start=[-4.13,-1.73,0], end=[-4.53,-0.83,0], stroke_width=2.1, color=GREEN)
        y_ = Tex(r"$\hat{y}_{i-1}$", color=GREEN).scale(0.35).next_to(y, LEFT).shift(RIGHT*0.2+UP*0.3)

        self.add(y,y_)

        xr = Arrow(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=2.1, color=DARK_BLUE)
        xr_ = Tex(r"$\hat{x}_{i}$", color=DARK_BLUE).scale(0.35).next_to(xr, RIGHT).shift(DOWN*0.2+LEFT*0.5)
        yr = Arrow(start=[-1.92,-0.9,0], end=[-2.9,-0.35,0], stroke_width=2.1, color=GREEN)
        yr_ = Tex(r"$\hat{y}_{i}$", color=GREEN).scale(0.35).next_to(yr, LEFT).shift(RIGHT*0.2+UP*0.3)
        a = Tex(r"$a_{i-1}$", color=BLUE).scale(0.35).next_to(x, RIGHT).shift(RIGHT*0.4+UP*0.2)

        self.add(xr, xr_, yr, yr_, a)

        rule2 = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"is called the link twist, which is the angle from $\hat{z}_{i-1}$ to $\hat{z}_{i}$  measured about $\hat{x}_{i-1}$ .").scale(0.4).next_to(rule2, RIGHT)
        self.add(rule2, rule21)

        alpha = DashedLine(start=[-3.75,-0.5,0], end=[-4.25,-1.5,0], stroke_width=2.1, color=RED).add_tip(at_start=True,  tip_length=0.1).rotate(angle=40*DEGREES, about_point=[-4.25,-1.5,0])
        alpha_ = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.3).next_to(zl, UP).shift(DOWN*0.25+LEFT*0.1)
        alpha__ = CurvedArrow(start_point=[-4.1,-1.2,0], end_point=[-4.35,-1.1,0],  color=RED, stroke_width=2, tip_length=0.06)
        self.add(alpha, alpha_, alpha__)

        rule3 = Tex(r"$d_i$:", color=RED).scale(0.4).next_to(rule21, DOWN).align_to(rule2, LEFT)
        rule31 = Tex(r"is the link offset, which is the distance from the intersection of $\hat{x}_{i-1}$ and $\hat{z}_{i}$ to the origin of the link-i frame.").scale(0.4).next_to(rule3, RIGHT).shift(DOWN*0.123)
        self.add(rule3, rule31)

        di = DashedLine(start=[-1.88,-1.3,0], end=[-2.15,-0.75,0], stroke_width=3.5, color=ORANGE).add_tip(tip_length=0.1)
        di_ = Tex(r"$d_{i}$", color=ORANGE).scale(0.35).next_to(di, LEFT).shift(RIGHT*0.25)

        self.add(di,di_)
        
        rule4 = Tex(r"$\phi_i$:", color=RED).scale(0.4).next_to(rule31, DOWN).align_to(rule2, LEFT)
        rule41 = Tex(r"is called the joint angle, which is the angle from $\hat{x}_{i-1}$ to $\hat{x}_{i}$ measured about the $\hat{z}_{i}$-axis.").scale(0.4).next_to(rule4, RIGHT).shift(DOWN*0.123)
        self.add(rule4, rule41)


        self.wait()


class DH_20(OPU_Slide):
   def construct(self):
        note = "הפרמטר הרביעי והאחרון הוא הזוית פי, שמוגדר להיות הזוית אותה צריך לסובב את איקס של אי מינוס אחת סביב ציר זד של איי כדי שיתלכד עם איקס של איי "
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("The 4 parameters:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"$a_{i-1}$", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"is the link length, which is the length of the mutually perpendicular line $\hat{a}_{i-1}$.").scale(0.4).next_to(rule1, RIGHT)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.4+RIGHT*0.33)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)


        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE).add_tip(tip_length=0.1)
        nl = Line(start=[-4.2,-1.4,0], end=[-4.06,-1.38,0], stroke_width=2.1, color=BLUE)
        nl1 = Line(start=[-4.06,-1.38,0], end=[-4.03,-1.48,0], stroke_width=2.1, color=BLUE)
        nr = Line(start=[-2.1,-1.2,0], end=[-1.94,-1.18,0], stroke_width=2.1, color=BLUE)
        nr1 = Line(start=[-2.1,-1.2,0], end=[-2.08,-1.31,0], stroke_width=2.1, color=BLUE)
        self.add(nl, nl1, nr, nr1)

        zim1 = VGroup(zl, zl_)
        zim1.move_to([-3.94,-1.22,0])
        self.add(orthogonal, zim1)

        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)
        y = Arrow(start=[-4.13,-1.73,0], end=[-4.53,-0.83,0], stroke_width=2.1, color=GREEN)
        y_ = Tex(r"$\hat{y}_{i-1}$", color=GREEN).scale(0.35).next_to(y, LEFT).shift(RIGHT*0.2+UP*0.3)

        self.add(y,y_)

        xr = Arrow(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=2.1, color=DARK_BLUE)
        xr_ = Tex(r"$\hat{x}_{i}$", color=DARK_BLUE).scale(0.35).next_to(xr, RIGHT).shift(DOWN*0.2+LEFT*0.5)
        yr = Arrow(start=[-1.92,-0.9,0], end=[-2.9,-0.35,0], stroke_width=2.1, color=GREEN)
        yr_ = Tex(r"$\hat{y}_{i}$", color=GREEN).scale(0.35).next_to(yr, LEFT).shift(RIGHT*0.2+UP*0.3)
        a = Tex(r"$a_{i-1}$", color=BLUE).scale(0.35).next_to(x, RIGHT).shift(RIGHT*0.4+UP*0.2)

        self.add(xr, xr_, yr, yr_, a)

        rule2 = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"is called the link twist, which is the angle from $\hat{z}_{i-1}$ to $\hat{z}_{i}$  measured about $\hat{x}_{i-1}$ .").scale(0.4).next_to(rule2, RIGHT)
        self.add(rule2, rule21)

        alpha = DashedLine(start=[-3.75,-0.5,0], end=[-4.25,-1.5,0], stroke_width=2.1, color=RED).add_tip(at_start=True,  tip_length=0.1).rotate(angle=40*DEGREES, about_point=[-4.25,-1.5,0])
        alpha_ = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.3).next_to(zl, UP).shift(DOWN*0.25+LEFT*0.1)
        alpha__ = CurvedArrow(start_point=[-4.1,-1.2,0], end_point=[-4.35,-1.1,0],  color=RED, stroke_width=2, tip_length=0.06)
        self.add(alpha, alpha_, alpha__)

        rule3 = Tex(r"$d_i$:", color=RED).scale(0.4).next_to(rule21, DOWN).align_to(rule2, LEFT)
        rule31 = Tex(r"is the link offset, which is the distance from the intersection of $\hat{x}_{i-1}$ and $\hat{z}_{i}$ to the origin of the link-i frame.").scale(0.4).next_to(rule3, RIGHT).shift(DOWN*0.123)
        self.add(rule3, rule31)

        di = DashedLine(start=[-1.88,-1.3,0], end=[-2.15,-0.75,0], stroke_width=3.5, color=ORANGE).add_tip(tip_length=0.1)
        di_ = Tex(r"$d_{i}$", color=ORANGE).scale(0.35).next_to(di, LEFT).shift(RIGHT*0.25)

        self.add(di,di_)
        
        rule4 = Tex(r"$\phi_i$:", color=RED).scale(0.4).next_to(rule31, DOWN).align_to(rule2, LEFT)
        rule41 = Tex(r"is called the joint angle, which is the angle from $\hat{x}_{i-1}$ to $\hat{x}_{i}$ measured about the $\hat{z}_{i}$-axis.").scale(0.4).next_to(rule4, RIGHT).shift(DOWN*0.123)
        self.add(rule4, rule41)

        xc = DashedLine(start=[-4.25,-1.5,0], end=[-3.3,-1.425,0], stroke_width=3).add_tip(tip_length=0.1)
        self.play(xc.animate().move_to([-1.425,-1.235,0]), run_time=2)
        # self.wait()


class DH_21(OPU_Slide):
   def construct(self):
        note = "הפרמטר הרביעי והאחרון הוא הזוית פי, שמוגדר להיות הזוית אותה צריך לסובב את איקס של אי מינוס אחת סביב ציר זד של איי כדי שיתלכד עם איקס של איי "
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("The 4 parameters:", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        rule1 = Tex(r"$a_{i-1}$", color=RED).scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule11 = Tex(r"is the link length, which is the length of the mutually perpendicular line $\hat{a}_{i-1}$.").scale(0.4).next_to(rule1, RIGHT)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.4+RIGHT*0.33)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, rule1, rule11, zl, zr, zl_, zr_)


        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE).add_tip(tip_length=0.1)
        nl = Line(start=[-4.2,-1.4,0], end=[-4.06,-1.38,0], stroke_width=2.1, color=BLUE)
        nl1 = Line(start=[-4.06,-1.38,0], end=[-4.03,-1.48,0], stroke_width=2.1, color=BLUE)
        nr = Line(start=[-2.1,-1.2,0], end=[-1.94,-1.18,0], stroke_width=2.1, color=BLUE)
        nr1 = Line(start=[-2.1,-1.2,0], end=[-2.08,-1.31,0], stroke_width=2.1, color=BLUE)
        self.add(nl, nl1, nr, nr1)

        zim1 = VGroup(zl, zl_)
        zim1.move_to([-3.94,-1.22,0])
        self.add(orthogonal, zim1)

        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)
        y = Arrow(start=[-4.13,-1.73,0], end=[-4.53,-0.83,0], stroke_width=2.1, color=GREEN)
        y_ = Tex(r"$\hat{y}_{i-1}$", color=GREEN).scale(0.35).next_to(y, LEFT).shift(RIGHT*0.2+UP*0.3)

        self.add(y,y_)

        xr = Arrow(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=2.1, color=DARK_BLUE)
        xr_ = Tex(r"$\hat{x}_{i}$", color=DARK_BLUE).scale(0.35).next_to(xr, RIGHT).shift(DOWN*0.2+LEFT*0.5)
        yr = Arrow(start=[-1.92,-0.9,0], end=[-2.9,-0.35,0], stroke_width=2.1, color=GREEN)
        yr_ = Tex(r"$\hat{y}_{i}$", color=GREEN).scale(0.35).next_to(yr, LEFT).shift(RIGHT*0.2+UP*0.3)
        a = Tex(r"$a_{i-1}$", color=BLUE).scale(0.35).next_to(x, RIGHT).shift(RIGHT*0.4+UP*0.2)

        self.add(xr, xr_, yr, yr_, a)

        rule2 = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.4).next_to(rule11, DOWN).align_to(rule1, LEFT)
        rule21 = Tex(r"is called the link twist, which is the angle from $\hat{z}_{i-1}$ to $\hat{z}_{i}$  measured about $\hat{x}_{i-1}$ .").scale(0.4).next_to(rule2, RIGHT)
        self.add(rule2, rule21)

        alpha = DashedLine(start=[-3.75,-0.5,0], end=[-4.25,-1.5,0], stroke_width=2.1, color=RED).add_tip(at_start=True,  tip_length=0.1).rotate(angle=40*DEGREES, about_point=[-4.25,-1.5,0])
        alpha_ = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.3).next_to(zl, UP).shift(DOWN*0.25+LEFT*0.1)
        alpha__ = CurvedArrow(start_point=[-4.1,-1.2,0], end_point=[-4.35,-1.1,0],  color=RED, stroke_width=2, tip_length=0.06)
        self.add(alpha, alpha_, alpha__)

        rule3 = Tex(r"$d_i$:", color=RED).scale(0.4).next_to(rule21, DOWN).align_to(rule2, LEFT)
        rule31 = Tex(r"is the link offset, which is the distance from the intersection of $\hat{x}_{i-1}$ and $\hat{z}_{i}$ to the origin of the link-i frame.").scale(0.4).next_to(rule3, RIGHT).shift(DOWN*0.123)
        self.add(rule3, rule31)

        di = DashedLine(start=[-1.88,-1.3,0], end=[-2.15,-0.75,0], stroke_width=3.5, color=ORANGE).add_tip(tip_length=0.1)
        di_ = Tex(r"$d_{i}$", color=ORANGE).scale(0.35).next_to(di, LEFT).shift(RIGHT*0.25)

        self.add(di,di_)
        
        rule4 = Tex(r"$\phi_i$:", color=RED).scale(0.4).next_to(rule31, DOWN).align_to(rule2, LEFT)
        rule41 = Tex(r"is called the joint angle, which is the angle from $\hat{x}_{i-1}$ to $\hat{x}_{i}$ measured about the $\hat{z}_{i}$-axis.").scale(0.4).next_to(rule4, RIGHT).shift(DOWN*0.123)
        self.add(rule4, rule41)

        xc = DashedLine(start=[-4.25,-1.5,0], end=[-3.3,-1.425,0], stroke_width=3).add_tip(tip_length=0.1).move_to([-1.425,-1.235,0])
        self.add(xc)

        xic = DashedLine(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=3).add_tip(tip_length=0.1).shift(RIGHT*0.22+UP*0.175)
        # xic = DashedLine(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=3).add_tip(tip_length=0.1).shift(RIGHT*0.22+UP*0.175).move_to([-1.425,-0.93,0])
        self.add(xic)
        phi = CurvedArrow(start_point=[-1.425,-1.235,0], end_point=[-1.425,-0.93,0], stroke_width=2, tip_length=0.06)
        phii = Tex(r"$\phi_i$").scale(0.3).next_to(phi, RIGHT).shift(LEFT*0.23)
        self.play(xic.animate().move_to([-1.425,-0.93,0]), run_time=2)
        self.play(Create(phi), Write(phii))

        # self.wait()



class DH_22(OPU_Slide):
   def construct(self):
        note = "אז בעצם אחרי שמיקמנו מסגרת לכל ג'וינט צריל מסגרת נוספת לבסיס ומסגרת נוספת לא.א. השיטה אומרת שאת מסגרת הבסיס בדרך כלל נקבע עם המסגרת הראשונה ואת מסגרת הא.א. נקבע כך שנפשט ככל שניתן את הפרמטרים - במילים אחרות כל שכמה שיותר פרמטרים יהיו מאופסים"
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Assigning the Ground and End-Effector Frames:", color=BLUE).next_to(title, DOWN).scale(0.4)
        self.add(title, secondary_title)

        rule1 = Tex(r"We would like to simplify as many of the D.H. parametes as possible.").scale(0.4).shift(UP*1.5+LEFT*0.5)
        rule2 = Tex(r"The ground frame is usually chosen to coincide with the link-1 frame in its zero (rest) position.").scale(0.4).next_to(rule1, DOWN).align_to(rule1, LEFT)
        rule3 = Tex(r"If the joint is revolute this choice forces $a_0 = \alpha_0 = d_1 = 0$.").scale(0.4).next_to(rule2, DOWN).align_to(rule1, LEFT)
        rule4 = Tex(r"If the joint is prismatic joint we have $a_0 = \alpha_0 = \phi_1 = 0$.").scale(0.4).next_to(rule3, DOWN).align_to(rule1, LEFT)
        rule5 = Tex(r"The end-effector frame is attached to some reference point on the end-effector, usually at a location that makes the description of the task intuitive and natural and also simplifies as many of the D–H parameters as possible").scale(0.4).next_to(rule4, DOWN).align_to(rule1, LEFT)
        self.play(Write(rule1),Write(rule2),Write(rule3),Write(rule4),Write(rule5))
        self.wait()


class DH_23(OPU_Slide):
   def construct(self):
        note = "אז אחרי שיש לנו את 4 הפרמטרים לכל אחד מהג'וינטים בעצם נציב אותם במטריצת הטרנספורמציה המתאימה מאיי מינוס אחת לאיי. "
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Manipulator Forward Kinematics:", color=BLUE).next_to(title, DOWN).scale(0.4)
        self.add(title, secondary_title)

        ti = ImageMobject("../images/ti.png").next_to(secondary_title, DOWN).shift(LEFT*2.5+DOWN*0.3)
        ti1 = ImageMobject("../images/ti1.png").next_to(ti, RIGHT)
        ti2 = ImageMobject("../images/ti2.png").shift(DOWN*1.3)
        
        self.add(ti, ti1, ti2)
        self.wait()


class DH_24(OPU_Slide):
   def construct(self):
        note = "אפשר לראות שהטרנספורמציה הזאת היא מכפלה של 4 אופרטורים :\
                רוטציה...."
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Manipulator Forward Kinematics:", color=BLUE).next_to(title, DOWN).scale(0.4)

        img = ImageMobject('../images/dh0.png').scale(1.5).shift(LEFT*3+DOWN*0.05)
        ll = Line(start=[-4,-1,0], end=[-5,-3,0], stroke_width=2.1)
        lr = Line(start=[-2.035,-1,0], end=[-1.035,-3,0], stroke_width=2.1)
        zl = Arrow(start=[-4,-1,0], end=[-3.52,0,0], color=RED)
        zr = Arrow(start=[-2.035,-1,0], end=[-2.51,0,0], color=RED)
        zl_ = Tex(r"$\hat{z}_{i-1}$", color=RED).scale(0.35).next_to(zl, UP).shift(DOWN*0.4+RIGHT*0.33)
        zr_ = Tex(r"$\hat{z}_{i}$", color=RED).scale(0.35).next_to(zr, UP).shift(DOWN*0.2)
        self.add(title, secondary_title, img, ll, lr, zl, zr, zl_, zr_)


        orthogonal = DashedLine(start=[-4.25,-1.5,0], end=[-1.9,-1.3,0], stroke_width=2.1, color=BLUE).add_tip(tip_length=0.1)
        nl = Line(start=[-4.2,-1.4,0], end=[-4.06,-1.38,0], stroke_width=2.1, color=BLUE)
        nl1 = Line(start=[-4.06,-1.38,0], end=[-4.03,-1.48,0], stroke_width=2.1, color=BLUE)
        nr = Line(start=[-2.1,-1.2,0], end=[-1.94,-1.18,0], stroke_width=2.1, color=BLUE)
        nr1 = Line(start=[-2.1,-1.2,0], end=[-2.08,-1.31,0], stroke_width=2.1, color=BLUE)
        self.add(nl, nl1, nr, nr1)

        zim1 = VGroup(zl, zl_)
        zim1.move_to([-3.94,-1.22,0])
        self.add(orthogonal, zim1)

        x = Arrow(start=[-4.5,-1.53,0], end=[-3.5,-1.43,0], stroke_width=2.1, color=DARK_BLUE)
        x_ = Tex(r"$\hat{x}_{i-1}$", color=DARK_BLUE).scale(0.35).next_to(x, RIGHT).shift(DOWN*0.2+LEFT*0.5)

        self.add(x,x_)
        y = Arrow(start=[-4.13,-1.73,0], end=[-4.53,-0.83,0], stroke_width=2.1, color=GREEN)
        y_ = Tex(r"$\hat{y}_{i-1}$", color=GREEN).scale(0.35).next_to(y, LEFT).shift(RIGHT*0.2+UP*0.3)

        self.add(y,y_)

        xr = Arrow(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=2.1, color=DARK_BLUE)
        xr_ = Tex(r"$\hat{x}_{i}$", color=DARK_BLUE).scale(0.35).next_to(xr, RIGHT).shift(DOWN*0.2+LEFT*0.5)
        yr = Arrow(start=[-1.92,-0.9,0], end=[-2.9,-0.35,0], stroke_width=2.1, color=GREEN)
        yr_ = Tex(r"$\hat{y}_{i}$", color=GREEN).scale(0.35).next_to(yr, LEFT).shift(RIGHT*0.2+UP*0.3)
        a = Tex(r"$a_{i-1}$", color=BLUE).scale(0.35).next_to(x, RIGHT).shift(RIGHT*0.4+UP*0.2)

        self.add(xr, xr_, yr, yr_, a)

        alpha = DashedLine(start=[-3.75,-0.5,0], end=[-4.25,-1.5,0], stroke_width=2.1, color=RED).add_tip(at_start=True,  tip_length=0.1).rotate(angle=40*DEGREES, about_point=[-4.25,-1.5,0])
        alpha_ = Tex(r"$\alpha_{i-1}$", color=RED).scale(0.3).next_to(zl, UP).shift(DOWN*0.25+LEFT*0.1)
        alpha__ = CurvedArrow(start_point=[-4.1,-1.2,0], end_point=[-4.35,-1.1,0],  color=RED, stroke_width=2, tip_length=0.06)
        self.add(alpha, alpha_, alpha__)


        di = DashedLine(start=[-1.88,-1.3,0], end=[-2.15,-0.75,0], stroke_width=3.5, color=ORANGE).add_tip(tip_length=0.1)
        di_ = Tex(r"$d_{i}$", color=ORANGE).scale(0.35).next_to(di, LEFT).shift(RIGHT*0.25)

        self.add(di,di_)

        xc = DashedLine(start=[-4.25,-1.5,0], end=[-3.3,-1.425,0], stroke_width=3).add_tip(tip_length=0.1).move_to([-1.425,-1.235,0])
        self.add(xc)

        xic = DashedLine(start=[-2.35,-0.92,0], end=[-1.45,-0.25,0], stroke_width=3).add_tip(tip_length=0.1).shift(RIGHT*0.22+UP*0.175).move_to([-1.425,-0.93,0])
        phi = CurvedArrow(start_point=[-1.425,-1.235,0], end_point=[-1.425,-0.93,0], stroke_width=2, tip_length=0.06)
        phii = Tex(r"$\phi_i$").scale(0.3).next_to(phi, RIGHT).shift(LEFT*0.23)
        self.add(xic, phi, phii)

        ti = ImageMobject("../images/ti.png").next_to(secondary_title, DOWN).shift(RIGHT)
        ti4 = ImageMobject("../images/ti3.png").shift(RIGHT*2.7+DOWN*0.4)
       
        
        self.add(ti, ti4)
        self.wait()


class DH_25(OPU_Slide):
   def construct(self):
        note = "תרגילים"
        self.create_note(note)
        self.add_info()

        title = Text("Appendix C: Denavit–Hartenberg Parameters").shift(UP*3).scale(0.65)
        secondary_title = Text("Exercises ...", color=BLUE).scale(2)
        self.add(title, secondary_title)

        self.wait()



class Chap4_08(OPU_Slide):
   def construct(self):
        note = "השיטה הנוספת והעיקרית שנלמדת בספר היא מכפלת האקספוננטים - לפני שנתחיל לעבור עליה חושב להכיר את המונח הום או זירו פוזישן שמוגדר להיות מנח הרובוט כאשר כל המשתנים של הג'וינטים מאופסים - \
                כלומר כל הזויות מאופסות ברוולוט ג'וינט ובפריזמטיק ג'וינט השינוי באורך גם הוא מאופס. "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("4.1 Product of Exponentials:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Home or Zero position of a robot is when all the joints are set to zero", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*3)
        self.add(title, secondary_title, prob, img)

        circ1, rect1, in_circ1, circ2, rect2, in_circ2, circ3, rect3, in_circ3, rect0 = get_robot_1dof()
        moving_arm = VGroup(circ1, rect1, in_circ1, circ2, rect2, in_circ2 , circ3, rect3, in_circ3).scale(0.4).shift(DOWN*2.3)
        rect0.scale(0.4).next_to(circ1, DOWN).shift(UP*0.5)
        moving_arm.rotate(30*DEGREES, about_point=circ1.get_center())
        rect2.rotate(30*DEGREES, about_point=circ2.get_center())
       
        circ3.rotate(30*DEGREES, about_point=circ2.get_center())
        rect3.rotate(30*DEGREES, about_point=circ2.get_center())
        in_circ3.rotate(30*DEGREES, about_point=circ2.get_center())
       
        circ3.rotate(-60*DEGREES, about_point=circ3.get_center())
        rect3.rotate(-60*DEGREES, about_point=circ3.get_center())
        in_circ3.rotate(-60*DEGREES, about_point=circ3.get_center())
        self.play(FadeIn(moving_arm,rect0))
        self.play(Rotate(in_circ3,60*DEGREES,about_point=circ3.get_center()),
                        Rotate(rect3,60*DEGREES,about_point=circ3.get_center()),
                                Rotate(circ3,60*DEGREES,about_point=circ3.get_center()), rate_func=linear)

        self.play(Rotate(in_circ3,-30*DEGREES,about_point=circ2.get_center()),
                                Rotate(rect3,-30*DEGREES,about_point=circ2.get_center()),
                                        Rotate(circ3,-30*DEGREES,about_point=circ2.get_center()),
                                                 Rotate(rect2,-30*DEGREES,about_point=circ2.get_center()), rate_func=linear)
        
        self.play(Rotate(moving_arm,-30*DEGREES,about_point=circ1.get_center()), rate_func=linear)

        self.wait()

def get_robot_1dof(dof=1):
    rect1 = Rectangle(BLUE, 0.75,3)
    circ1 = Circle(0.5).next_to(rect1, LEFT).shift(RIGHT*0.5)
    in_circ1= Circle(0.05, color=BLUE).move_to(circ1.get_center())
    rect2 = Rectangle(BLUE, 0.75,3).move_to(rect1.get_right()+RIGHT*2)
    circ2 = Circle(0.5).next_to(rect2, LEFT).shift(RIGHT*0.5)
    in_circ2= Circle(0.05, color=BLUE).move_to(circ2.get_center())
    rect3 = Rectangle(BLUE, 0.75,3).move_to(rect2.get_right()+RIGHT*2)
    circ3 = Circle(0.5).next_to(rect3, LEFT).shift(RIGHT*0.5)
    in_circ3= Circle(0.05, color=BLUE).move_to(circ3.get_center())
    rect0 = Rectangle(BLUE, 0.75,0.75).next_to(circ1, DOWN).shift(UP*0.5)
    return circ1, rect1, in_circ1, circ2, rect2, in_circ2, circ3, rect3, in_circ3, rect0



class Chap4_09(OPU_Slide):
   def construct(self):
        note = "אז כשהרובוט בהום פוזישן - נגדיר את המטריצה אם להיות הקונפיגורציה של הא.א ביחס למסגרת הבסיס המסומנת כאפס"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("4.1 Product of Exponentials:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Define M to be the position and orientation of frame \{4\} when the robot is at its home position.", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/fkm.png').scale(1.3).next_to(img, RIGHT)
        self.add(title, secondary_title, prob, img, img1)

        self.wait()



class Chap4_10(OPU_Slide):
   def construct(self):
        note = "בשלב הבא צריך לקבוע לכל אחד מהצירים ציר בורג אס. אני מזכיר שציר בורג שקול לטרנפורמציה הומוגונית ובנוי משני וקטורים באר שלוש, \
                הראשון אומגה שהוא המהירות הזויתית ווי - המהירות הלינארית. המהירות הזויות היא ציר הסיבוב במקרה שלפנינו ניתן לראות כי זהו ציר הזד.\
                        המהירות הלינארית נמדדת בנקודת הייחוס (במקרה שלנו בראשית הצירים של מסגרת הבסיס) ומוגדרת כמינוס המכפלה הוקטורית בין המהירות הזויתית לבין נקודה על ציר הסיבוב המסמנת באות קיו. "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("4.1 Product of Exponentials:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"If $\theta_1$ and $\theta_2$ are held at their zero position then the screw axis corresponding to rotating about joint 3 can be expressed in the \{0\} frame as:", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/fks3.png').scale(1.3).next_to(img, RIGHT).shift(UP*0.5)
        img2 = ImageMobject('../images/fkv3.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1, img2)

        self.wait()




class Chap4_11(OPU_Slide):
   def construct(self):
        note = "וכפי שראיתו לאחר שיש לנו את וקטור ציר הבורג אפשר להציב את הערכים שבו בצורה מטריציונית ולקבל את הייצוג של הטרנספורמציה בקואורדינטות אקספוננציאליות.\
                בהנחה שהזיות של הג'וינט הראשון והשני נשארו מאופסות. אם נכפיל משמאל את אם באי בחזקת ציר הבורג טטא של הג'וינט השלישי נקבל את הטרנספורמציה מהבסיס לא.א."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("4.1 Product of Exponentials:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/fks3sqew.png').scale(1.3).next_to(img, RIGHT).shift(UP*0.5+LEFT*0.5)
        # img2 = ImageMobject('../images/fkv3.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1,)

        self.wait()


class Chap4_12(OPU_Slide):
   def construct(self):
        note = "אז עכשיו נניח שמשנים גם את הזוית של טטא שתיים . וטטא שלוש מקובע כרגע על זוית כלשהי אבל טטא אחת מאופסת.\
                אז אם נכפיל את מה שקיבלנו בשקף הקודם תתקבל הטרנספורמציה מהבסיס לא.א. כאשר היא תלויה בזויות משני הג'וינטים האחרונים."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("4.1 Product of Exponentials:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/fks2sqew.png').scale(1.3).next_to(img, RIGHT).shift(UP*0.5+LEFT*0.5)
        # img2 = ImageMobject('../images/fkv3.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1,)

        self.wait()


class Chap4_13(OPU_Slide):
   def construct(self):
        note = "טוב אז אתם רואים לאן זה הולך אני מקווה...\
                אם נייצג טרנספורמצית ציר בורג עבור כל ג'וינט ונכפיל בסדר מהראשון לאחרון משמאל למטריצה אם (למה משמאל - כי הטרנספורמציה ביחס לבסיס) נקבל את הטרנספורמציה מהבסיס לא.א. כפי שרצינו "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("4.1 Product of Exponentials:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.1.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/fks1sqew.png').scale(1.3).next_to(img, RIGHT).shift(UP*0.5+LEFT*0.5)
        # img2 = ImageMobject('../images/fkv3.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1,)

        self.wait()


class Chap4_14(OPU_Slide):
   def construct(self):
        note = "בעצם מה שעשינו זה לפתח את ה פ.א.א בספייס פורם - כלומר ביחס למסדרת הבסיס. בשרטוט אפשר לראות איך ההכפלה באקספוננט משנה את הקונפיגורציה של הא.א ביחס לציר הבורג של אותו ג'וינט. \
                לסיכום  - כדי להגיע לביטוי מכפלת האקספוננטים - צריך שלושה דברים:\
                        1. להגדיר את הקונפיגורציה של הא.א ביחס לבסיס בשהרובוט בהום פוזישן באמצעות המטריצה אם\
                                2. להגדיר ציר בורג לכל אחד מהג'ינטס ביחס לבסיס\
                                        3. וכמובן שאנחנו צריכים את ערכי הטטות של כל הג'וינטס\
                                                וכפי שכתוב בשורה האחרונה בשקף - יתרון של השיטה הזאת הוא שאין צורך להגדיר מסגרות ייחוס"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("4.1 Product of Exponentials:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/fkilus.png').scale(1).shift(DOWN*1+LEFT*3.8)
        img1 = ImageMobject('../images/fks4.png').scale(1.3).next_to(img, RIGHT).shift(UP*0.5)
        # img2 = ImageMobject('../images/fkv3.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1,)

        self.wait()


class Chap4_15(OPU_Slide):
   def construct(self):
        note = "דוגמה 4.1 בספר - שימו לב שבדוגמה נתונים לנו מערכות הצירים אבל הן פה רק כדי להטעות - למה? כין שכל מה שמעניין אותנו זה ציר הבורג ביחס למערכת הצירים של הבסיס וזהו "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Example 4.1:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Derive the forward kinematics for the spatial open chain robot using the PoE formula", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.3.png').scale(1.3).shift(DOWN*1+LEFT*3)
        # img1 = ImageMobject('../images/fks4.png').scale(1.3).next_to(img, RIGHT).shift(UP*0.5+LEFT*0.5)
        # img2 = ImageMobject('../images/fkv3.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img,)

        self.wait()


class Chap4_16(OPU_Slide):
   def construct(self):
        note = "אז מהו הביטוי של הפ.ק. בספיישיאל פורם? ומהי המטריצה אם? "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Example 4.1:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Derive the forward kinematics for the spatial open chain robot using the PoE formula", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.3.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/fks5.png').scale(1.3).next_to(img, RIGHT).shift(UP*0.5+LEFT*0.5)
        # img2 = ImageMobject('../images/fkv3.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1)

        squ1 = Rectangle(color=BLACK, width=2.2, height=0.4, fill_color=BLACK, fill_opacity=1).shift(UP*0.4+RIGHT*3.65)
        squ2 = Rectangle(color=BLACK, width=1.6, height=1.4, fill_color=BLACK, fill_opacity=1).shift(DOWN*1.3+RIGHT*3.47)
        self.add(squ1, squ2)
        self.wait()


class Chap4_17(OPU_Slide):
   def construct(self):
        note = "Example 4.1"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Example 4.1:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Derive the forward kinematics for the spatial open chain robot using the PoE formula", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.3.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/fks5.png').scale(1.3).next_to(img, RIGHT).shift(UP*0.5+LEFT*0.5)
        # img2 = ImageMobject('../images/fkv3.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1)

        self.wait()


class Chap4_18(OPU_Slide):
   def construct(self):
        note = "נמלא טבלה של וקטורי המהירות עבוד כל ג'וינט "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Example 4.1:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Derive the forward kinematics for the spatial open chain robot using the PoE formula", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.3.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/fkstab.png').scale(1.3).next_to(img, RIGHT).shift(UP*0.5+LEFT*0.5)
        # img2 = ImageMobject('../images/fkv3.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1)
        # squ1 = Rectangle(color=BLACK, width=2.2, height=0.4, fill_color=BLACK, fill_opacity=1).shift(UP*0.4+RIGHT*3.65)
        squ2 = Rectangle(color=BLACK, width=0.95, height=0.195, fill_color=BLACK, fill_opacity=1).shift(DOWN*0.59+RIGHT*2.85)
        squ3 = squ2.copy().shift(RIGHT*1.2)
        squ4 = squ2.copy().shift(DOWN*0.26 + RIGHT*1.15)
        squ5 = squ2.copy().shift(DOWN*0.26)
        squ6 = squ2.copy().shift(DOWN*0.52)
        squ7 = squ2.copy().shift(DOWN*0.52 + RIGHT*1.2)
        self.add(squ2, squ3, squ4, squ5, squ6, squ7)
        self.wait()


class Chap4_19(OPU_Slide):
   def construct(self):
        note = "Example 4.1"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Example 4.1:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Derive the forward kinematics for the spatial open chain robot using the PoE formula", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.3.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/fkstab.png').scale(1.3).next_to(img, RIGHT).shift(UP*0.5+LEFT*0.5)
        # img2 = ImageMobject('../images/fkv3.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1)
      
        self.wait()

class Chap4_20(OPU_Slide):
   def construct(self):
        note = "ואז כמובן שנציב את הערכים בייצוג המטריציוני כדי להשלים את מה שחסר כדי לחשב את המכפלה "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Example 4.1:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Derive the forward kinematics for the spatial open chain robot using the PoE formula", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.3.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/fkssum.png').scale(1.3).next_to(img, RIGHT).shift(LEFT*0.5)
        # img2 = ImageMobject('../images/fkv3.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1)
      
        self.wait()


class Chap4_21(OPU_Slide):
   def construct(self):
        note = "תרגיל נוסף - שמו לב שהפעם אין לנו מסגרות על כל ג'וינט אלא רק את מסגרת הבסיס והא.א."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Example 4.4:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Derive the forward kinematics for the spatial open chain robot using the PoE formula", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.5.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/4.51.png').scale(1.3).next_to(img, RIGHT).shift(UP)
        img2 = ImageMobject('../images/4.52.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1, img2)
        squ1 = Rectangle(color=BLACK, width=4.4, height=0.4, fill_color=BLACK, fill_opacity=1).shift(RIGHT*3.38)
        squ2 = Rectangle(color=BLACK, width=2.1, height=1.4, fill_color=BLACK, fill_opacity=1).shift(DOWN*1.3+RIGHT*3.7)
        self.add(squ1, squ2)
        self.wait()


class Chap4_22(OPU_Slide):
   def construct(self):
        note = "Example 4.1"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Example 4.4:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Derive the forward kinematics for the spatial open chain robot using the PoE formula", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.5.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/4.51.png').scale(1.3).next_to(img, RIGHT).shift(UP)
        img2 = ImageMobject('../images/4.52.png').scale(1.3).next_to(img1, DOWN).shift(RIGHT*0.5)
        self.add(title, secondary_title, prob, img, img1, img2)
       
        self.wait()




class Chap4_23(OPU_Slide):
   def construct(self):
        note = "Example 4.1"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Example 4.4:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Derive the forward kinematics for the spatial open chain robot using the PoE formula", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.5.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/4.53.png').scale(1.3).next_to(img, RIGHT).shift(LEFT*0.2)
        self.add(title, secondary_title, prob, img, img1)

        squ2 = Rectangle(color=BLACK, width=0.95, height=0.23, fill_color=BLACK, fill_opacity=1).shift(DOWN*0.64+RIGHT*4.05)
        squ3 = squ2.copy().shift(RIGHT*1.2)
        squ4 = squ2.copy().shift(DOWN*0.3 + RIGHT*1.2)
        squ5 = squ2.copy().shift(DOWN*0.3)
        squ6 = squ2.copy().shift(DOWN*0.62)
        squ7 = squ2.copy().shift(DOWN*0.62 + RIGHT*1.2)
        squ8 = squ2.copy().shift(DOWN*0.93 + RIGHT*1.2)
        squ9 = squ2.copy().shift(DOWN*0.93)
        squ10 = squ2.copy().stretch_to_fit_width(1.1).shift(DOWN*1.24 + RIGHT*1.3)
        squ11 = squ2.copy().shift(DOWN*1.24)
        squ12= squ2.copy().shift(DOWN*1.55)
        squ13 = squ2.copy().shift(DOWN*1.55 + RIGHT*1.2)
        self.add(squ2, squ3, squ4, squ5, squ6, squ7, squ8, squ9, squ10, squ11, squ12, squ13)
        self.wait()



class Chap4_24(OPU_Slide):
   def construct(self):
        note = "Example 4.1"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Example 4.4:", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"Derive the forward kinematics for the spatial open chain robot using the PoE formula", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/4.5.png').scale(1.3).shift(DOWN*1+LEFT*3)
        img1 = ImageMobject('../images/4.53.png').scale(1.3).next_to(img, RIGHT).shift(LEFT*0.2)
        self.add(title, secondary_title, prob, img, img1)

        self.wait()



class Chap4_25(OPU_Slide):
   def construct(self):
        note = "אוקיי אז השקף האחרון מגלה לנו שכמו שהכפלנו משמאל את אם בצירי בורג ביחס לבסיס אפשר להכפיל מימין בצירי בורג ביחס לא.א. הפעולות דומות ונבצע אותם בתרגילים "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("4.1.3 Second Formulation: Screw Axes in the End-Effector Frame", color=BLUE).next_to(title, DOWN).scale(0.4)
        
        prob = Tex(r"The PoE formula can also be represented in the body form:", color=GREEN).next_to(secondary_title, DOWN).scale(0.5)
        img = ImageMobject('../images/poeb.png').scale(1.5)
        self.add(title, secondary_title, prob, img)

        self.wait()

class Chap4_26(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 4: Forward Kintematics").shift(UP*3).scale(0.65)
        secondary_title = Text("Exercises ...", color=BLUE).scale(2)
        self.add(title, secondary_title)

        self.wait()
