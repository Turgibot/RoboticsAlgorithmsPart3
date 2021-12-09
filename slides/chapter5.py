from OPU import *
from manim_slide import MyBullets



class Chap5_00(OPU_Slide):
   def construct(self):
        note = "ביחידה הקודמת פתרנו את בעיית הפורוורד קינמטיקס - והיא : בהינתן ערכי משתני הג'וינטס טטא מהי הקונפיגורציה של הא.א. ? כפי ששמתם לב \
                וזה חוזר על עצמו בספר - היום אנחנו נדבר על הנגזרת של הקונפיגורציה של הא.א כלומר על המהירות או יותר נכון הטוויסט של הא.א."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("The Problem", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/rob.jpg').scale(0.7).shift(DOWN*1.3)
 
        bullets = VGroup()
        bullets+= Text(r"In the last unit we learn about forward kinematics.")
        bullets+= Text(r"We calculated the configuration of the EE for a given set of joint positions.")
        bullets+= Text(r"Today: We would learn how to calculate the twist of an EE from a given set of joint positions and velocities.")
        
        blist = MyBullets(latex_grp=bullets, size=3, isNumbered=False).scale(0.27).shift(UP)

        self.add(title, secondary_title, blist, img)
        self.wait()




class Chap5_01(OPU_Slide):
   def construct(self):
        note = "נתחיל בקצת מוטיבציה - אז למה מהירות חשובה ברובוטיקה - ובכן, אפליקציות רבות במיוחד ברובוטים תעשיים דורשים יכולות של תנועה מהירה מצד אחד - \
                ותנועה איטית ויש יגידו עדינה ומדוייקת מאידך. למשל כמו ברובוט המבצע עבודת ריתוך - שדורשת מהירות ספציפית לחומר המרותך ולזוית הריתוך מה עוד שברור שהרובוט נע מהר יותר כשהוא לא מרתך.\
                         דוגמה נוספת היא הרובוט המצייר הזה - הדוגמה הזאת באה להמחיש כמה היכולת לשלוט במהירות של האא חשובה. תארו לעצמכם שמברשת ספוגה בצבע נעה לכיוון הקנבס במהירות גבוהה מידי שמתיזה את הצבע החוצה מהמברשת. בקיצור מהירות היא מפתח בכל אפליקציה רובוטית קיימת ובכדי לדבר על מהירות חייבים לדבר על היעקוביאן.  "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("Jacobian Motivation", color=BLUE).next_to(title, DOWN).scale(0.4)
        self.add(title, secondary_title)

          #include video
        cap = cv2.VideoCapture("../media/videos/kukaweld.mp4")

        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.6).shift(DOWN*0.6)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

       
        self.wait()


class Chap5_02(OPU_Slide):
   def construct(self):
        note = "נתחיל בקצת מוטיבציה - אז למה מהירות חשובה ברובוטיקה - ובכן, אפליקציות רבות במיוחד ברובוטים תעשיים דורשים יכולות של תנועה מהירה מצד אחד - \
                ותנועה איטית ויש יגידו עדינה ומדוייקת מאידך. למשל כמו ברובוט המבצע עבודת ריתוך - שדורשת מהירות ספציפית לחומר המרותך ולזוית הריתוך מה עוד שברור שהרובוט נע מהר יותר כשהוא לא מרתך.\
                         דוגמה נוספת היא הרובוט המצייר הזה - הדוגמה הזאת באה להמחיש כמה היכולת לשלוט במהירות של האא חשובה. תארו לעצמכם שמברשת ספוגה בצבע נעה לכיוון הקנבס במהירות גבוהה מידי שמתיזה את הצבע החוצה מהמברשת. בקיצור מהירות היא מפתח בכל אפליקציה רובוטית קיימת ובכדי לדבר על מהירות חייבים לדבר על היעקוביאן.  "

        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("Jacobian Motivation", color=BLUE).next_to(title, DOWN).scale(0.4)
        self.add(title, secondary_title)

          #include video
        cap = cv2.VideoCapture("../media/videos/kukapaint.mp4")
        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.6).shift(DOWN*0.6)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()

       
        self.wait()


class Chap5_03(OPU_Slide):
   def construct(self):
        note = "אז מהו היעקוביאן - זוהי מטריצה המתארת את נגזרות הג'וינטים לפי הטטא. כלומר בהינתן איקס שהוא הקואורדינטות של האא אז הנגזרת שלו בזמן \
                זוהי מהירות האא. ואם נגיד שהפ.ק. של איקס הוא הפונקציה אף של טטא כאשר טטא הם משתני הג'וינטס.\
                         אז לפי כלל השרשרת נקבל שהמהירות של האא הוא הנגזרת החלקית של הפ.ק לפי טטא מוכפל בטטא דוט. הנגזרת החלקית היא היעקוביאן. \
                                 כלומר היעקוביאן מקשר בין המהירות של האא לבין מהירות הגוינטים."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("Jacobian Introduction", color=BLUE).next_to(title, DOWN).scale(0.4)
        img = ImageMobject('../images/rob.jpg').scale(0.7).shift(DOWN*1.3)
 
        txt1= Tex(r"Before we talk about twist, let $x \in \mathbb{R}^m$ be the EE minimal set of coordinates.").scale(0.5).shift(UP*1.2)
        txt2= Tex(r"Then, its velocity is $\dot{x} = \frac{dx}{dt}\in \mathbb{R}^m$.").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"So the FK can be written as $x(t) = f(\theta(t))$.").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"Where $\theta \in \mathbb{R}^n$ is a set of n joint variables.").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        txt5= Tex(r"By the chain rule the time derivative at time t is $\dot{x} = \frac{\partial{f(\theta)}}{\partial{\theta}}\frac{d\theta}{dt} = \frac{\partial{f(\theta)}}{\partial{\theta}}\dot{\theta}=J(\theta)\dot{\theta} $").scale(0.5).next_to(txt4, DOWN).align_to(txt1, LEFT)
        txt6= Tex(r"Where $J(\theta)\in\mathbb{R}^{m\times n}$ is called the Jacobian.").scale(0.5).next_to(txt5, DOWN).align_to(txt1, LEFT)
        txt7= Tex(r"The Jacobian matrix represents the linear sensitivity of the EE velocity $\dot{x}$ to the joint velocity $\dot{\theta}$, and it is a function of the joint variables $\theta$.").scale(0.5).next_to(txt6, DOWN).align_to(txt1, LEFT)
        

        self.add(title, secondary_title, txt1, txt2, txt3, txt4, txt5, txt6, txt7)
        self.wait()




class Chap5_04(OPU_Slide):
   def construct(self):
        note = "הספר מראה את הפיתוח של היעקוביאן - כשעברתי עליו שמתי לב לטעות קטנה אבל לא רציתי שתתעכבו בגללה אז אני מראה אותה אותה פה.\
                אם נגדיל קצת את האזור עם הטעות אנחנו רואים שהטוויסא של האא ביחד לוורלד פריים אס, מוגדר כמכפלה של היעקוביאן במהירות הגו'ינטים. כאשר כל עמודה \
                        בעצם מתייחסת לג'וינט נפרד. "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4).shift(LEFT*4.5)
        img = ImageMobject('../images/derive.png').scale(0.8).shift(DOWN*0.4)
 
        txt1= Tex(r"In this section we derive the relationship between an open chain’s joint velocity vector $\theta$ and the EE’s spatial twist $V_s$.").scale(0.5).shift(UP*1.2)
       

        self.add(title, secondary_title, img)
        self.wait()




class Chap5_05(OPU_Slide):
   def construct(self):
        note = "הספר מראה את הפיתוח של היעקוביאן - כשעברתי עליו שמתי לב לטעות קטנה אבל לא רציתי שתתעכבו בגללה אז אני מראה אותה אותה פה.\
                אם נגדיל קצת את האזור עם הטעות אנחנו רואים שהטוויסא של האא ביחד לוורלד פריים אס, מוגדר כמכפלה של היעקוביאן במהירות הגו'ינטים. כאשר כל עמודה \
                        בעצם מתייחסת לג'וינט נפרד. "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4).shift(LEFT*4.5)
        img = ImageMobject('../images/derive.png').scale(0.8).shift(DOWN*0.4)
 
        txt1= Tex(r"Errata**", color=RED).scale(0.5).shift(LEFT*4)
        arrow = Arrow(start=[-4, 0, 0], end=[-1, -1.9, 0], color=RED)

        self.add(title, secondary_title, img, txt1, arrow)
        self.wait()




class Chap5_06(OPU_Slide):
   def construct(self):
        note = "הספר מראה את הפיתוח של היעקוביאן - כשעברתי עליו שמתי לב לטעות קטנה אבל לא רציתי שתתעכבו בגללה אז אני מראה אותה אותה פה.\
                אם נגדיל קצת את האזור עם הטעות אנחנו רואים שהטוויסא של האא ביחד לוורלד פריים אס, מוגדר כמכפלה של היעקוביאן במהירות הגו'ינטים. כאשר כל עמודה \
                        בעצם מתייחסת לג'וינט נפרד. "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4).shift(LEFT*4.5)
        img = ImageMobject('../images/derive.png').scale(0.8).shift(DOWN*0.4)
        img1 = ImageMobject('../images/derive_err.png').scale(0.8).shift(DOWN*4.4)
 
        txt1= Tex(r"Errata**", color=RED).scale(0.5).shift(LEFT*4)
        arrow = Arrow(start=[-4, 0, 0], end=[-1, -1.9, 0], color=RED)

        self.add(title, secondary_title, img1, img,txt1, arrow)
        self.play(FadeOut(txt1, arrow, img), img1.animate().move_to([0,-0.2,0]).scale(1.4), secondary_title.animate().shift(RIGHT*4.5), run_time=1)
        self.wait()




class Chap5_07(OPU_Slide):
   def construct(self):
        note = "הספר מראה את הפיתוח של היעקוביאן - כשעברתי עליו שמתי לב לטעות קטנה אבל לא רציתי שתתעכבו בגללה אז אני מראה אותה אותה פה.\
                אם נגדיל קצת את האזור עם הטעות אנחנו רואים שהטוויסא של האא ביחד לוורלד פריים אס, מוגדר כמכפלה של היעקוביאן במהירות הגו'ינטים. כאשר כל עמודה \
                        בעצם מתייחסת לג'וינט נפרד. "    
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/derive_err.png').scale(0.8).shift(DOWN*4.4).move_to([0,-0.2,0]).scale(1.4)
        v = Tex(r"$V_s = J_{s1}\dot{\theta_1}+J_{s2}(\theta)\dot{\theta_2}+...+J_{sn}(\theta)\dot{\theta_n}$", color=GREEN).scale(0.5).shift(UP*1.07).add_background_linkangle(opacity=1)
        self.add(title, secondary_title, img1)
        self.play(FadeIn(v))
        self.wait()


class Chap5_08(OPU_Slide):
   def construct(self):
        note = "ההגדרה הרשמתי של היעקוביאן מסבירה שכל אחת מהעמודות של היעקוביאן היא מכפלה של מטריצת האדגוינט שאותה כבר פגשנו בעבר , ביצוג הבורג של אותו הג'וינט. שימו לב שעבור העמודה האי ביעקוביאן ביפיקסד פריים  - האדגוינט מחושבת עבור \
                הקואורדינטות האקספוננציליות של הגונטים אחד עד אי פחות אחד. טוב אז נשמע קשה לחישוב ולא משהו שהיינו שמחים להסתבכ איתו. למזלנו הספר רומז במספר שורות \
                        שלא כדאי לפספס שהחישוב של העמודה האיי ביעקוביאן נעשית באותו האופן שבו מצאנו את הפרודקט אוף אקספוננשיאלז רק שהפעם אנחנו לא פותרים עבור האא אלא עבור כל \
                                ג'וינט בנפרד ובנוסף אנחנו לא מניחים שהרובוט בהום פוזישן ושהטטות מאופסות אלא מנתחים עבור ערכי טטא כלשהם. "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/jacob1.png').scale(1.2).shift(UP)
        img2 = ImageMobject('../images/jacob2.png').scale(1.2).next_to(img1, DOWN)
        self.add(title, secondary_title, img1, img2)
        self.wait()


class Chap5_09(OPU_Slide):
   def construct(self):
        note = "ההגדרה הרשמתי של היעקוביאן מסבירה שכל אחת מהעמודות של היעקוביאן היא מכפלה של מטריצת האדגוינט שאותה כבר פגשנו בעבר , ביצוג הבורג של אותו הג'וינט. שימו לב שעבור העמודה האי ביעקוביאן ביפיקסד פריים  - האדגוינט מחושבת עבור \
                הקואורדינטות האקספוננציליות של הגונטים אחד עד אי פחות אחד. טוב אז נשמע קשה לחישוב ולא משהו שהיינו שמחים להסתבכ איתו. למזלנו הספר רומז במספר שורות \
                        שלא כדאי לפספס שהחישוב של העמודה האיי ביעקוביאן נעשית באותו האופן שבו מצאנו את הפרודקט אוף אקספוננשיאלז רק שהפעם אנחנו לא פותרים עבור האא אלא עבור כל \
                                ג'וינט בנפרד ובנוסף אנחנו לא מניחים שהרובוט בהום פוזישן ושהטטות מאופסות אלא מנתחים עבור ערכי טטא כלשהם.\
                                        ----- לציין שמות ומספרים על הג'וינטים ולצייר את הפיקסד פריים ---- "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/summ.png').scale(1.2).shift(UP)
        self.add(title, secondary_title, img1)
        joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base = get_robot()
        moving_arm = VGroup(joint1, link1, in_joint1, joint2, link2, in_joint2 , joint3, link3, in_joint3, joint4, link4, in_joint4).scale(0.4).shift(DOWN*2.3+LEFT*2)
        base.scale(0.4).next_to(joint1, DOWN).shift(UP*0.5)
        self.add(moving_arm,base)
        
        self.wait()

class Chap5_10(OPU_Slide):
   def construct(self):
        note = "אם נתבונן בגוינט השני - ניתן לראות שסיבוב של הגוינטים שלאחריו לא משפיע על הקונפיגורציה שלו ביחס לפיקסד פריים. \
                אבל לאחר שהגוינטים הקודמים לו סובב הקונפיגורציה שלו ביחס לפיקס פריים השתנתה. כלומר כל עמודה ביעקוביאן מחושבת כטוויסט של ג'וינט שמושפע משינוי בקונפיגורציה של ג'וינטים קודמים לו."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/summ.png').scale(1.2).shift(UP)
        self.add(title, secondary_title, img1)
        joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base = get_robot()
        moving_arm = VGroup(joint1, link1, in_joint1, joint2, link2, in_joint2 , joint3, link3, in_joint3, joint4, link4, in_joint4).scale(0.4).shift(DOWN*2.3+LEFT*2)
        base.scale(0.4).next_to(joint1, DOWN).shift(UP*0.5)
        self.add(moving_arm,base)
        l4 = VGroup(joint4, in_joint4, link4)
        l3 = VGroup(joint3, in_joint3, link3)
        l2 = VGroup(joint2, in_joint2, link2)
        l1 = VGroup(joint1, in_joint1, link1)
        self.play(Rotate(l4,30*DEGREES,about_point=joint4.get_center()),rate_func=linear)
        self.wait()


class Chap5_11(OPU_Slide):
   def construct(self):
        note = "אם נתבונן בגוינט השני - ניתן לראות שסיבוב של הגוינטים שלאחריו לא משפיע על הקונפיגורציה שלו ביחס לפיקסד פריים. \
                אבל לאחר שהגוינטים הקודמים לו סובב הקונפיגורציה שלו ביחס לפיקס פריים השתנתה. כלומר כל עמודה ביעקוביאן מחושבת כטוויסט של ג'וינט שמושפע משינוי בקונפיגורציה של ג'וינטים קודמים לו."

        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/summ.png').scale(1.2).shift(UP)
        self.add(title, secondary_title, img1)
        joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base = get_robot()
        moving_arm = VGroup(joint1, link1, in_joint1, joint2, link2, in_joint2 , joint3, link3, in_joint3, joint4, link4, in_joint4).scale(0.4).shift(DOWN*2.3+LEFT*2)
        base.scale(0.4).next_to(joint1, DOWN).shift(UP*0.5)
        l4 = VGroup(joint4, in_joint4, link4)
        l3 = VGroup(joint3, in_joint3, link3)
        l2 = VGroup(joint2, in_joint2, link2)
        l1 = VGroup(joint1, in_joint1, link1)
        l4.rotate(30*DEGREES,about_point=joint4.get_center())
        self.add(moving_arm,base)
        
        self.play(Rotate(l4,30*DEGREES,about_point=joint3.get_center()),
                        Rotate(l3,30*DEGREES,about_point=joint3.get_center()),
                                rate_func=linear)

        self.wait()



class Chap5_12(OPU_Slide):
   def construct(self):
        note = "אם נתבונן בגוינט השני - ניתן לראות שסיבוב של הגוינטים שלאחריו לא משפיע על הקונפיגורציה שלו ביחס לפיקסד פריים. \
                אבל לאחר שהגוינטים הקודמים לו סובב הקונפיגורציה שלו ביחס לפיקס פריים השתנתה. כלומר כל עמודה ביעקוביאן מחושבת כטוויסט של ג'וינט שמושפע משינוי בקונפיגורציה של ג'וינטים קודמים לו."

        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/summ.png').scale(1.2).shift(UP)
        self.add(title, secondary_title, img1)
        joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base = get_robot()
        moving_arm = VGroup(joint1, link1, in_joint1, joint2, link2, in_joint2 , joint3, link3, in_joint3, joint4, link4, in_joint4).scale(0.4).shift(DOWN*2.3+LEFT*2)
        base.scale(0.4).next_to(joint1, DOWN).shift(UP*0.5)
        l4 = VGroup(joint4, in_joint4, link4)
        l3 = VGroup(joint3, in_joint3, link3)
        l2 = VGroup(joint2, in_joint2, link2)
        l1 = VGroup(joint1, in_joint1, link1)
        l4.rotate(30*DEGREES,about_point=joint4.get_center())
        l4.rotate(30*DEGREES,about_point=joint3.get_center())
        l3.rotate(30*DEGREES,about_point=joint3.get_center())
        self.add(moving_arm,base)
        
        self.play(Rotate(l4,30*DEGREES,about_point=joint2.get_center()),
                        Rotate(l3,30*DEGREES,about_point=joint2.get_center()),
                                Rotate(l2,30*DEGREES,about_point=joint2.get_center()),
                                        rate_func=linear)       

        self.wait()



class Chap5_13(OPU_Slide):
   def construct(self):
        note = "אם נתבונן בגוינט השני - ניתן לראות שסיבוב של הגוינטים שלאחריו לא משפיע על הקונפיגורציה שלו ביחס לפיקסד פריים. \
                אבל לאחר שהגוינטים הקודמים לו סובב הקונפיגורציה שלו ביחס לפיקס פריים השתנתה. כלומר כל עמודה ביעקוביאן מחושבת כטוויסט של ג'וינט שמושפע משינוי בקונפיגורציה של ג'וינטים קודמים לו."

        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian", color=BLUE).next_to(title, DOWN).scale(0.4)
        img1 = ImageMobject('../images/summ.png').scale(1.2).shift(UP)
        self.add(title, secondary_title, img1)
        joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base = get_robot()
        moving_arm = VGroup(joint1, link1, in_joint1, joint2, link2, in_joint2 , joint3, link3, in_joint3, joint4, link4, in_joint4).scale(0.4).shift(DOWN*2.3+LEFT*2)
        base.scale(0.4).next_to(joint1, DOWN).shift(UP*0.5)
        l4 = VGroup(joint4, in_joint4, link4)
        l3 = VGroup(joint3, in_joint3, link3)
        l2 = VGroup(joint2, in_joint2, link2)
        l1 = VGroup(joint1, in_joint1, link1)
        l4.rotate(30*DEGREES,about_point=joint4.get_center())
        l4.rotate(30*DEGREES,about_point=joint3.get_center())
        l4.rotate(30*DEGREES,about_point=joint2.get_center())
        l3.rotate(30*DEGREES,about_point=joint3.get_center())
        l3.rotate(30*DEGREES,about_point=joint2.get_center())
        l2.rotate(30*DEGREES,about_point=joint2.get_center())
        self.add(moving_arm,base)
        
        self.play(Rotate(l4,30*DEGREES,about_point=joint1.get_center()),
                        Rotate(l3,30*DEGREES,about_point=joint1.get_center()),
                                Rotate(l2,30*DEGREES,about_point=joint1.get_center()),
                                        Rotate(l1,30*DEGREES,about_point=joint1.get_center()),
                                                rate_func=linear)       

        self.wait()

def get_robot():
    link1 = Rectangle(BLUE, 0.75,3)
    joint1 = Circle(0.5).next_to(link1, LEFT).shift(RIGHT*0.5)
    in_joint1= Circle(0.05, color=BLUE).move_to(joint1.get_center())
    link2 = Rectangle(BLUE, 0.75,3).move_to(link1.get_right()+RIGHT*2)
    joint2 = Circle(0.5).next_to(link2, LEFT).shift(RIGHT*0.5)
    in_joint2= Circle(0.05, color=BLUE).move_to(joint2.get_center())
    link3 = Rectangle(BLUE, 0.75,3).move_to(link2.get_right()+RIGHT*2)
    joint3 = Circle(0.5).next_to(link3, LEFT).shift(RIGHT*0.5)
    in_joint3= Circle(0.05, color=BLUE).move_to(joint3.get_center())
    link4 = Rectangle(BLUE, 0.75,3).move_to(link3.get_right()+RIGHT*2)
    joint4 = Circle(0.5).next_to(link4, LEFT).shift(RIGHT*0.5)
    in_joint4= Circle(0.05, color=BLUE).move_to(joint4.get_center())
    base = Rectangle(BLUE, 0.75,0.75).next_to(joint1, DOWN).shift(UP*0.5)
    return joint1, link1, in_joint1, joint2, link2, in_joint2, joint3, link3, in_joint3, joint4, link4, in_joint4, base


class Chap5_14(OPU_Slide):
   def construct(self):
        note = "אז בואו נתחיל לתרגל באמצעות שתי דוגמאות שניתנו בספר. בדוגמה הראשונה יש לנו רובוט סקארה בעל 4 דרגות חופש. מה יהיה מימד מטריצת היעקוביאן?"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
       

        self.add(title, secondary_title, img, txt1)
        self.wait()


class Chap5_15(OPU_Slide):
   def construct(self):
        note = "ובכן ייצוג בורג של כל ג'וינט הוא ממימד 6 ויש לנו 4 כאלו אז היעקובין ממימד 6 על 4. את ייצוג הבורג של הג'וינט הראשון נחשב ישירות שכן הוא לא מושפע מהקודמים לו שלא קיימים.\
                א1 הוא 0 0 1 וי הוא 0 0 0 "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.2.png').scale(1).shift(UP*1+RIGHT*3)
       
        mask = Rectangle(color=BLACK, width=2.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.5)
        self.add(title, secondary_title, img, txt1, img1, mask)
        self.wait()



class Chap5_16(OPU_Slide):
   def construct(self):
        note = "א2 מושמע מהרוטציה של א1 ולכן יש להפעיל על וקטור הכיוון של הסיבוב אופרטור רוטציה משמאל הפועל על ציר הזד בטטא 1 מעלות.\
                  נקבל שא2 הוא 0 0 1. נבחר בק2 להיות אל1 קוס טטא1 על ציר האיקס ואל1 סינ טטא1 על ציר הוואי ולאחר המכפלה הקרטזית מינוס אומגה 2 קיו2 נקבל את התוצאה הבאה:" 
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.2.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js1.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=2.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.5)
        mask.shift(RIGHT*0.3)
        self.add(title, secondary_title, img, txt1, img1, mask, img2)
        self.wait()




class Chap5_17(OPU_Slide):
   def construct(self):
        note = "נעשה זאת גם עבור הג'וינט השלישי. "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.2.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js2.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=2.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.5)
        mask.shift(RIGHT*0.85)
        self.add(title, secondary_title, img, txt1, img1, mask, img2)
        self.wait()

class Chap5_18(OPU_Slide):
   def construct(self):
        note = "ונקבל גם פה שאומגה הוא 0 0 1 . שימו לב שקיו שלוש מחושב לפי זויות אקראיות כלשהן בג'וינטים הקודמים . לאחר מכן מתבצעת אותה המכפלה הקרטזית ומתקבל וקטור העמודה השלישי שמרכיב את היעקוביאן"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.2.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js3.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=2.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.5)
        mask.shift(RIGHT*2.2)
        self.add(title, secondary_title, img, txt1, img1, mask, img2)
        self.wait()


class Chap5_19(OPU_Slide):
   def construct(self):
        note = "הג'וינט האחרון הוא פריזמטי ולכן אין לו מהירות זויתית . את הוקטור המהירות הלינארית צריך לחשב כתלות בג'וינטים הקודמים לו. אם נחשב נראה \
                שמכין שכל הרוטציות מתבצעות סביב ציר הז הכיוון של הג'וינט הפריזמטי נשאר על ציר הזד גם הוא. \
                        קיבלנו מטריצה 6 על 4 היא מטריצת היעקוביאן לפי הפיקסד פריים של הרובוט המשורטט."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRRP chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.7.png').scale(1).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.2.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js4.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=2.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.5)
        mask.shift(RIGHT*2.2)
        self.add(title, secondary_title, img, txt1, img1, img2)
        self.wait()



class Chap5_20(OPU_Slide):
   def construct(self):
        note = "יאללה תרגיל נוסף. מה יהיה מימד היעקוביאן פה? שקף"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        # img2 = ImageMobject('../images/js11.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        # mask.shift(RIGHT*2.2)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask)
        self.wait()





class Chap5_21(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js11.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*0.5)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2)
        self.wait()





class Chap5_22(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js12.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*1.5)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2)
        self.wait()






class Chap5_23(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js12.png').scale(1).next_to(img1, DOWN)
        img3 = ImageMobject('../images/rot.png').scale(1).next_to(img2, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*1.5)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2, img3)
        self.wait()





class Chap5_24(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js13.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*2)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2)
        self.wait()




class Chap5_25(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js14.png').scale(1).next_to(img1, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*2)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2)
        self.wait()




class Chap5_26(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js14.png').scale(1).next_to(img1, DOWN)
        img3 = ImageMobject('../images/js15.png').scale(1).next_to(img2, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*3)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2, img3)
        self.wait()

class Chap5_27(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js14.png').scale(1).next_to(img1, DOWN)
        img3 = ImageMobject('../images/js16.png').scale(1).next_to(img2, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*4.2)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, mask, img2, img3)
        self.wait()


class Chap5_28(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.1: Space Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)
 
        txt1= Tex(r"Find the space Jacobian for this RRPRRR chain robot.").scale(0.4).shift(UP*1.5+LEFT*3.5)
        img = ImageMobject('../images/fig5.8.png').scale(0.9).next_to(txt1, DOWN)
        img1 = ImageMobject('../images/jacob5.3.png').scale(1).shift(UP*1+RIGHT*3)
        img2 = ImageMobject('../images/js14.png').scale(1).next_to(img1, DOWN)
        img3 = ImageMobject('../images/js17.png').scale(1).next_to(img2, DOWN)
        mask = Rectangle(color=BLACK, width=5.8, height=1.5, fill_color=BLACK, fill_opacity=1).move_to(img1).shift(RIGHT*0.7)
        mask.shift(RIGHT*4.2)
        x = Tex("$\hat{x}$").scale(0.35).shift(LEFT*6+DOWN*3)
        y = Tex("$\hat{y}$").scale(0.35).shift(LEFT*4.5+DOWN*2.5)
        self.add(title, secondary_title, img, txt1, img1 , x, y, img2, img3)
        self.wait()

class Chap5_29(OPU_Slide):
   def construct(self):
        note = "כמובן שקיימת גם גרסא שמתייחסת לבודי פריים ולא לפיקס פריים - אנחנו נפתור תרגיל מתאים אבל חשוב לומר לפני כן שהפעם \
                הגוינטים שאחרי ג'וינט מסויים משפיעים על הקונפיגורציה שלו ביחס לבודי פריים ושאת האופרטורים יש להפעיל מימין ולא משמאל כיון שהם \
                        פועלים ביחס לבודי פריים ולא לפיקס פריים."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.2: Body Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/body_def.png').scale(1).shift(UP*1.4)
        img2 = ImageMobject('../images/body_def2.png').scale(1).next_to(img1, DOWN)

        self.add(title, secondary_title, img1, img2)
        self.wait()

class Chap5_30(OPU_Slide):
   def construct(self):
        note = "ניתן לקבל יעקוביאן בבודי פריים מהיעקוביאן בפיקסד פריים וההפך. הדבר נעשה באמצעות מכפלה במטריצת האדג'וינט של הטרנספורמציה טי אס בי או טי בי אס המתאימה לפי הנוסחא ולפי אותו כלל מחיקה מוכר"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.1.4: Relationship between the Space and Body Jacobian ", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/adjoint.png').scale(1).shift(DOWN*0.5)

        self.add(title, secondary_title, img1)
        self.wait()



class Chap5_31(OPU_Slide):
   def construct(self):
        note = "הנושא הבא שנלמד בפרק הזה עוסק בסינגולריות  - כבר פגשנו במושג הזה כשדיברנו על מרחב הקונפיגורציות של רובוט. עכשיו \
                נרד לעומקו של המושג ונראה כיצד מזהים קונפיגורציה סינגולרית של רובוט אוופנציין. \
                        נעשה זאת באמצעות היעקוביאן.\
                                סינגולריות מתגלה כאשר מטריצת היעקוביאן מאבדת דרגה. \
                                        זה קורה כשבקונפיגורציה מסויימת יש תלות לינארית בין השורות או העמודות שבמטריצה.\
                                                בקונפיגורציה הזאת הרובוט מאבד את יכולת התנועה במימד או מימדים מסוימים.\
                                                         כלומר הוא דרגת חופש אחת או יותר וזה לא משנה אם הניתוח הוא לפי יעקוביאן בבסיס או בפיקסד פריים כמובן "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.3: Singularity Analysis", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/adjoint.png').scale(1).shift(DOWN*0.5)

        txt1= Tex(r"The Jacobian allows us to identify postures at which the robot's end-effector loses the ability to move instantaneously in one or more directions.").scale(0.5).shift(UP*1.2)
        txt2= Tex(r"Such a posture is called a kinematic singularity, or simply a singularity.").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"Singular postures correspond to those values of $\theta$ at which the rank of $J(\theta)$ drops below the maximum rank.").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"at such postures the tip frame loses the ability to generate instantaneous spatial velocities in in one or more dimensions.").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        txt5= Tex(r"The mathematical definition of a kinematic singularity is independent of the choice of body or space Jacobian.").scale(0.5).next_to(txt4, DOWN).align_to(txt1, LEFT)
        txt6= Tex(r"At a singularity, a robotic arm loses one or more degrees of freedom.").scale(0.5).next_to(txt5, DOWN).align_to(txt1, LEFT)
        

        self.add(title, secondary_title, txt1, txt2, txt3, txt4, txt5, txt6)
        self.wait()


class Chap5_32(OPU_Slide):
   def construct(self):
        note = "בעוד שבעיית הפ.ק מבקשת לדעת את מיקום האא בהנתן הטטות בעיה קשה יותר היא הבעיה ההפוכה - כלומר בהנתן קונפיגורציה של הא.א\
                מהם הערכים של משתני הג'וינטים? את הבעיה הזאת אנחנו נפתור במפגש הבא והיא נקראת בעית הקינמטיקה ההפוכה.\
                        אנחנו נשתמש באינברס של היעקוביאן כדי למצוא את מהירות הג'וינטים עבור מהירות אא מסויימת .\
                                כך נוכל לתכנן מסלולים עבור הרובוט שלנו מנקודה לנקודה. יכול להיות שעל מסלול מסוים תחושב קונפיגורציה סינגולרית - \
                                        מה שיגרום להתנהגות בלתי צפויה של הרובוט \ הוא יכול להתקע בקונפיגורציה מסויימת ולא לצאת ממנה. כלומר יש פה \
                                                פגיעה בביצועי הרובוט ואנחנו נמנע מלהתקרב לקונפיגורציות סינגולריות"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.3: Singularity Analysis", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/adjoint.png').scale(1).shift(DOWN*0.5)

        txt1= Tex(r"The problem of forward kinematics gives us the configuration of the EE given its joint values.").scale(0.5).shift(UP*1.2)
        txt2= Tex(r"Next chapter deals with the inverse kinemtics problem.").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"Inverse kinematics is the problem of finding the joint values for a desired EE configuration").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"Using the inverse jacobian we can also find the velocity of the joints for a desired EE velocity.").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        txt5= Tex(r"We will be able to plan and execute trajectories.").scale(0.5).next_to(txt4, DOWN).align_to(txt1, LEFT)
        txt6= Tex(r"If the trajectory passes trough a singularity the EE might get stuck or behave unpredictedly.").scale(0.5).next_to(txt5, DOWN).align_to(txt1, LEFT)
        txt7= Tex(r"Because singularities significantly deteriorate the performance of a chain robot, you must learn how to identify them and never move close to them, when planning the EE's path.").scale(0.5).next_to(txt6, DOWN).align_to(txt1, LEFT)
        

        self.add(title, secondary_title, txt1, txt2, txt3, txt4, txt5, txt6, txt7)
        self.wait()




class Chap5_34(OPU_Slide):
   def construct(self):
        note = " הוידאו הזה מראה קונפיגורציות סינגולריות בזרוע רובוטית בעלת שש דרגות חופש"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.3: Singularity Analysis", color=BLUE).next_to(title, DOWN).scale(0.4)

        self.add(title, secondary_title)
          #include video
        cap = cv2.VideoCapture("../media/videos/singularity1.mp4")

        flag, frame = cap.read()
        while not flag:
            pass
        while flag :
            flag, frame = cap.read()
            if flag:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_img = ImageMobject(frame).scale(0.8).shift(DOWN*0.6)
                self.add(frame_img)
                self.wait(0.042)
                self.remove(frame_img)
            
        cap.release()
        self.wait()

       


class Chap5_33(OPU_Slide):
   def construct(self):
        note = "בואו נחקור קצת יותר את הענין - כל מה שכתוב פה לא מופיע בספר - לפחות לא בהקשר של סינגולריות אז חשוב שתכירו את השקף הזה כי הוא יעזור לכם להבין \
                למה ואיך הרובוט בכלל מגיע לנקודה סינגולרית שכזאת.\
                        אז נניח שאנחנו רוצים להניע את האא לאורך מסלול במהירות אחידה.\
                                נפעיל את האינברס יעקוביאן ונקבל את המהירות של כל ג'וינט.\
                                        את האינברס יעקוביאן מחשבים באמצעות הנוסחה שלפנינו: כאשר מחלקים בדטרמיננטה.\
                                                בקונפיגורציה הסינגולרית היעקוביאן סינגולרי ולכן הדרמיננטה היא 0 והאינברס יעקוביאן לא מגודר .\
                                                        בעיה נוספת היא כאשר הקונפיגורציה כמעט סינגולרית - אז הדטרמיננטה כמעט מתאפסת מה שתורם למהירויות גבוהות מאד , לעיתים בלתי אפשריות ולעיתים מסוכנות. \
                                                                ולכן אנחנו נרצה להמנע אפילו מלהתקרב לקונפיגורציות סינגולריות. "
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.3: Singularity Analysis", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/adjoint.png').scale(1).shift(DOWN*0.5)

        txt1= Tex(r"Let's say we would like to move the EE along a path with constant speed.").scale(0.5).shift(UP*1.2)
        txt2= Tex(r"The joint velocities are calculated from : $\dot{\theta} = J^{-1} \dot{V}$.").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"where $J^{-1} = \frac{1}{det(J)}Adj(J)$").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"When the robot is in a singularity there is no solution for calculating $J^{-1}$").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        txt5= Tex(r"In singularity, $J$ becomes singular and $det(J) = 0$ so it is impossible to calculate $J^{-1}$.").scale(0.5).next_to(txt4, DOWN).align_to(txt1, LEFT)
        txt6= Tex(r"If the trajectory passes close to a singularity the determinant value is close to zero.").scale(0.5).next_to(txt5, DOWN).align_to(txt1, LEFT)
        txt7= Tex(r"This results in high joints velocities (division by a very small number). Such high joint velocities may be unexpected and can pose safety risks in the case of big, fast industrial robots.").scale(0.5).next_to(txt6, DOWN).align_to(txt1, LEFT)
        

        self.add(title, secondary_title, txt1, txt2, txt3, txt4, txt5, txt6, txt7)
        self.wait()


class Chap5_35(OPU_Slide):
   def construct(self):
        note = "כדי למצוא את הסינגולריות משלבים שתי גישות - הגישה החישובית שבה מגלים את הערך של הטטות שמאפס את הדטרמיננטה של היעקוביאן.\
                או שמוצאים את הערך של הטטות שגורם לתלות בין השורות או העמודות במטריצה ולכן הדרגה של היעקוביאן יורדת.\
                        או בניתוח ויזואלי לפי סט של חוקים שמתאים לרובוטים מסוימים ומושלכים על מקרים כלליים.\
                                חמש דוגמאות מוצגות בספר בוא נכיר אותן בזריזות:"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.3: Singularity Analysis", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/adjoint.png').scale(1).shift(DOWN*0.5)

        txt1= Tex(r"To find the singularity configurations we can use a mathematical approach:").scale(0.5).shift(UP*1.2)
        txt2= Tex(r"1. Calculate the $\theta$s for which the jacobian determinant zeros.").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"2. Calculate the $\theta$s for which the jacobian becomes singular (rank < 6)").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"Or by a visual inspection approach.").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        txt5= Tex(r"5 examples in the book and in the next slides.").scale(0.5).next_to(txt4, DOWN).align_to(txt1, LEFT)
        

        self.add(title, secondary_title, txt1, txt2, txt3, txt4, txt5)
        self.wait()



class Chap5_36(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.3: Singularity Analysis", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/sing1.png').scale(1.2).shift(LEFT*3.5)
        img2 = ImageMobject('../images/js4.png').scale(1.2).next_to(img1, DOWN)
        img3 = ImageMobject('../images/sing11.png').scale(1.4).shift(RIGHT*2.5)

        self.add(title, secondary_title, img1, img3)
        self.wait()



class Chap5_37(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.3: Singularity Analysis", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/sing2.png').scale(1.2).shift(LEFT*3.5)
        img2 = ImageMobject('../images/js4.png').scale(1.2).next_to(img1, DOWN)
        img3 = ImageMobject('../images/sing22.png').scale(1.4).shift(RIGHT*2.5)

        self.add(title, secondary_title, img1, img3)
        self.wait()




class Chap5_38(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.3: Singularity Analysis", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/sing3.png').scale(1.2).shift(LEFT*3.5)
        img2 = ImageMobject('../images/js4.png').scale(1.2).next_to(img1, DOWN)
        img3 = ImageMobject('../images/sing32.png').scale(1.4).shift(RIGHT*2.5)

        self.add(title, secondary_title, img1, img3)
        self.wait()



class Chap5_39(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.3: Singularity Analysis", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/sing4.png').scale(1.2).shift(LEFT*3.5+DOWN*0.3)
        img2 = ImageMobject('../images/js4.png').scale(1.2).next_to(img1, DOWN)
        img3 = ImageMobject('../images/sing41.png').scale(1.2).shift(RIGHT*3)

        self.add(title, secondary_title, img1, img3)
        self.wait()


class Chap5_40(OPU_Slide):
   def construct(self):
        note = ""
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.3: Singularity Analysis", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/sing5.png').scale(1.2).shift(DOWN*0.3)
        self.add(title, secondary_title, img1)
        self.wait()


class Chap5_41(OPU_Slide):
   def construct(self):
        note = "מניפולביליטי מוגדר להיות היכול של האא לנוע במימדים שונים.\
                אנחנו נראה שבאמצעות המניפולביליטי אליפסואיד ניתן לתאר ויזואלית את כיווני התנועה האפשריים של הרובוט.\
                        מצאתי משהו ברשת שיכול לעזור להסביר למה אני מתכוון..."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.4: Manipulability", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/eliips2.png').scale(1).shift(DOWN*2.3)
        self.add(title, secondary_title, img1)


        txt1= Tex(r"Manipulability is the robots EE ability to translate or rotate in one or more directions.").scale(0.5).shift(UP*1.4)
        txt2= Tex(r"We would like to know, if a particular robot configuration is singular or not?").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"And how close is a nonsingular configuration to a singular one?").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"We can use the manipulability ellipsoid to visualize geometrically the directions in which the EE moves with least effort or with greatest effort.").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        

        self.add(title, secondary_title, txt1, txt2, txt3, txt4)
        self.wait()



class Chap5_42(OPU_Slide):
   def construct(self):
        note = "את האליפסואיד הזה מייצרים פעמיים - כאשר פעם אחת הוא מייצג את המהירות הזויתית ובשנייה את הלינארית.\
                פשוט לוקחים 3 שורות ראשונות ואחרונות של היעקוביאן בנפרד.\
                        נייצר מטריצה איי שהיא מכפלה של היעקוביאן בעצמו - וכך נקבל מטריצה ריבועית 3 על 3 חיובית וסימטרית."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.4: Manipulability", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/ellips1.png').scale(1).shift(DOWN*2.3)
        self.add(title, secondary_title, img1)


        txt1= Tex(r"The volume of the ellipsoid is proportional to the EE manipulability.").scale(0.5).shift(UP*1.4)
        txt2= Tex(r"We can create two ellipsoids, one for describing the angular velocity and the second one is for the linear velocity.").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
        txt3= Tex(r"For $J(\theta) = \begin{bmatrix} J_w(\theta)\\J_v(\theta)\end{bmatrix}$ where $J_w$ is the first 3 rows and $J_v$ is the last 3 rows.").scale(0.5).next_to(txt2, DOWN).align_to(txt1, LEFT)
        txt4= Tex(r"The square symentric and positive matrix $A = JJ^T$ (for $J = J_w$ or $J = J_v$) is used to define the the 3 dimensional ellipsoid.").scale(0.5).next_to(txt3, DOWN).align_to(txt1, LEFT)
        

        self.add(title, secondary_title, txt1, txt2, txt3, txt4)
        self.wait()



class Chap5_43(OPU_Slide):
   def construct(self):
        note = "עבור איי נחשב את שלושת הערכים העצמיים ואת הוקטורים העצמיים ונקבל ששורש הערכים העצמיים זה אורך חצי הציר והוקטור העצמי \
                הוא המהירות - וכך בנינו את האלפסואיד."
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.4: Manipulability", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/ellips1.png').scale(1).shift(DOWN*1)
        self.add(title, secondary_title, img1)


        txt1= Tex(r"Let $v_i$ and $\lambda_i, i = 1,2,3$ be the eigenvectors and eigenvalues of $A = JJ^T$ respectively.").scale(0.5).shift(UP*1.4)
        txt2= Tex(r"Then $\sqrt{\lambda_i}$ is the length and $v_i$ is the direction of the ellipsoid semi-axis.").scale(0.5).next_to(txt1, DOWN).align_to(txt1, LEFT)
       

        self.add(title, secondary_title, txt1, txt2)
        self.wait()



class Chap5_44(OPU_Slide):
   def construct(self):
        note = "דרך אחרת שאינה ויזואלית אלא חישובית היא לחשב את שלושת המיואים:\
                מיו אחד הוא היחס בין חצי הציר הארוך ביותר לקצר ביותר - אם נקבל אחד אז הרובוט יכול לנוע לכל הכיוונים וככל שהמספר גדל כך אנחנו מתקרבים לסינגולריות.\
                        המיו השני מלמד אותנו כמעט את אותו הדבר כיון שהוא בעצם ריבוע של מיו אחד - גם פה אחד הוא אופטימלי וככל שגדלים מקרבים לסינגולריות.\
                                המיו השלישי הוא מכפלת שורשי הערכים העצמיים - ששווה לשורש הדטרמיננטה של איי - במקרה הזה ככל שהערכים גדלים כך אנחנו מתרחקים מסינגולריות.\
                                        זהו יאללה תרגילים"
        self.create_note(note)
        self.add_info()

        title = Text("Chapter 5: Velocity Kinematics and Statics").shift(UP*3).scale(0.65)
        secondary_title = Text("5.4: Manipulability", color=BLUE).next_to(title, DOWN).scale(0.4)

        img1 = ImageMobject('../images/lamb1.png').scale(1.1).shift(UP*0.7)
        img2 = ImageMobject('../images/lamb2.png').scale(1.1).next_to(img1, DOWN)
        self.add(title, secondary_title, img1, img2)
        self.wait()


