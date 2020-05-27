from manimlib.imports import *

class PhasePortrait(GraphScene):
    Range = list(np.arange(-1,1.2,0.2))
    #Delete 0 from the Range.
    del Range[5]

    Domain = list(np.arange(-4, 4+1, 1))
    #Can't use pop since floating point approximations don't give 0 exactly
    #Using the config library, we can change the class Attributes of GraphScene

      #Using the config library, we can change the class Attributes of GraphScene
    CONFIG = {
        #Uppermost number on the y-axis
        "y_max" : 1,
        #number at the origin. Cannot be higher than y_max
        "y_min" : -1,
        #Same logic as y_max/min
        "x_max" : 4,
        "x_min" : -4,

        #Small tick frequency. Not labelled.
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 

        #Number of decimal palces on the x-label.
        "x_label_decimal":1,
        "y_label_decimal":1,

        #Creates a large tick at each number. Pass in a list
        #Pass in Range so that 0.0 is removed as a y-axis label.
        "y_labeled_nums": Range, 
        #Since exclude_zero_label is True, x labels won't have 0.0.
        "x_labeled_nums": Domain, #Add +0.5 to include 4

        #colours
        "axes_color" : BLUE,
        "function_color": RED,


        #Location of the origin.
        "graph_origin": ORIGIN,
        #Relative Position of the labels next to the tick marks
        "x_label_direction":DOWN,
        "y_label_direction":LEFT,
        #Pass strings, labels the x_axis
        "x_axis_label": "$y$",
        "x_axis_width":10,
        "y_axis_label":"$f(y)$",
        #How do I move f(y) above the uppermost tick?
        #"y_axis_label_direction":UP,

        #Removes 0 label
        "exclude_zero_label": True,

    }

    def construct(self):
        DiffEq = TexMobject(
            "\\frac{dy}{dx}",
            "=",
            "\\left(1-\\frac{y}{3}\\right)y"
        )

        phaseEq = TexMobject(
            "f(y)",
            "=",
            "\\left(1-\\frac{y}{3}\\right)y"
        )

        self.play(Write(DiffEq))
        self.play(Transform(DiffEq,phaseEq))
        # Transform diffeq into f(y)
        self.play(
            DiffEq.shift,UP*3+RIGHT*4,
            DiffEq.set_color, GREEN
        )

        self.setup_axes(animate=True)

        #Get graph+ Coordinates
        self.function = lambda x: (1-x/3)*x
        plot1 = self.get_graph(self.function, x_min = -1, x_max = 3.9, color = GREEN)
             

        #Animates the graph
        self.wait(0.5)        
        self.play(ShowCreation(plot1))
        self.wait()

        interceptEq = TexMobject(
            "{dy",
            "\\over",
            "dx}",
            "=",
            "0"
        )

        #create the text for equilibrium explanation
        eqText = TextMobject(
            "Equilibrium Points"
        )
        #Resize the text so that it fits on the graph.
        eqText.scale(0.85)

        # Get vectors to specific points on plot1, given x coordinates 0, 1.5, and 3. 
        coord1= self.input_to_graph_point(0,plot1)
        coord2 = self.input_to_graph_point(3,plot1)
        coord3 = self.input_to_graph_point(1.5,plot1)

        #Moves the intercept eq into position.
        interceptEq.shift(DOWN*2 + RIGHT*2)
        eqText.next_to(interceptEq,DOWN)
        #Write intercept eq
        self.play(Write(interceptEq),Write(eqText),run_time = 1)
        arrowBuffer = 0.5
        arrow1 = Arrow(interceptEq.get_left(),coord1,buff=arrowBuffer)
        arrow1.set_color(RED)

        arrow2 = Arrow(interceptEq.get_right(),coord2,buff=arrowBuffer)
        arrow2.set_color(RED)

        #Creating and positioning eqPoint Cricles
        eqPoint1 = Circle(color=RED, radius = 0.2)
        eqPoint1.shift(coord1)

        eqPoint2 = Circle(color=RED,radius = 0.2)
        eqPoint2.shift(coord2)

        #Animate eq point cricles and arrows same time
        self.play(ShowCreation(eqPoint1),ShowCreation(eqPoint2),GrowArrow(arrow1),GrowArrow(arrow2))

        #Fadeout arrows and text:
        self.play(FadeOut(arrow1),FadeOut(arrow2),FadeOut(eqText))

        #dy/dx<0
        leftSideEq = TexMobject(
            "\\frac{dy}{dx}",
            "<",
            "0"
        )
        middleEq = TexMobject(
            "\\frac{dy}{dx}",
            ">",
            "0"
        )
        leftSideEq.shift(LEFT*2+DOWN)
        self.play(Transform(interceptEq,leftSideEq))
        self.play(Write(middleEq.move_to(UP+RIGHT*2)))
        self.play(Write(leftSideEq.shift(RIGHT*8)))
        
        #Coordinate labels
        arrowCoords = [[ORIGIN,np.array([-4.5,0,0])],
        [ORIGIN,self.input_to_graph_point(3,plot1)],
        [np.array([6.5,0,0]),self.input_to_graph_point(3,plot1)],
        ]
      
        #Phase Arrows
        arrows=[]

        #Create the arrows
        for i in range(0,3):
            #Use Line() and .add_tip(...) to create the arrows instead of Arrow()
            #tip_length scales the tip evenly.
            arrows.append(Line(arrowCoords[i][0],arrowCoords[i][1],stroke_width=15,color=PURPLE, buff = 0.2).add_tip(tip_length=0.5))

        #Why don't these arrows also have the right stroke width?
        # arrowTest1 = Arrow(ORIGIN,np.array([1,1,0]),stroke_width=100)
        # arrowTest2 = Arrow(ORIGIN,np.array([1,-1,0]),stroke_width=100)
        # arrowTest3 = Arrow(ORIGIN,np.array([-1,1,0]),stroke_width=100)
        # arrowTest4 = Arrow(ORIGIN,np.array([-1,-1,0]),stroke_width=100)
        
        self.play(GrowArrow(arrows[0]),GrowArrow(arrows[1]),GrowArrow(arrows[2]))
        self.wait()

        #Note: I assume people know what the arrows mean.

        #############################Test ##############################
        print("Printed Object: ", self.x_axis.get_unit_size()) #Returns 0.8
        print("Printed Object2: ", self.x_axis_label) #Returns 0.8
        # self.play(GrowArrow(arrowTest1),GrowArrow(arrowTest2),GrowArrow(arrowTest3),GrowArrow(arrowTest4))
        stabText = TextMobject(
            "Stable",
            "Unstable",
        )
        stabText[0].next_to(arrowCoords[1][1],UP*2+RIGHT)
        stabText[1].next_to(arrowCoords[0][0],UP*2+LEFT)
        #These black rectangles will cover the axis labels and make it look like they are fading away.
        #Is there a way to automatically find the height and width of TextMobjects? I want to cover them with a rectangle.
        rect1 = Rectangle(height = 0.85, width = 1.5, color= BLACK,fill_color = BLACK, fill_opacity = 1)
        rect2 = Rectangle(height = 0.5, width = 2, color = BLACK,fill_color = BLACK, fill_opacity = 1)
        
        #Positioning the rectangles:
        #Rect 1 goes behind Stable
        rect1.move_to(stabText[0].get_center())
        rect2.move_to(stabText[1].get_center())
       
        #Write the rects
        self.play(ShowCreation(rect1),ShowCreation(rect2))        
        #Write the stab Text
        self.play(Write(stabText[0]),
        eqPoint2.set_color, WHITE,
        )

        self.play(
            Write(stabText[1]),
            eqPoint1.set_color,GREY,
            #FadeOut(self.x_axis_label)#Fade out the $y$ label Not working
        )

        self.wait(2)
        





