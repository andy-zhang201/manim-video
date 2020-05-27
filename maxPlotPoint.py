from manimlib.imports import *


class PhasePortrait(GraphScene):
    Domain = list(np.arange(-1,1.2,0.2))
    #Delete 0 from the Domain.
    del Domain[5]
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
        "y_labeled_nums": list(np.arange(-1,1.2,0.2)), 
        "x_labeled_nums": list(np.arange(-4, 4+1, 1)), #Add +0.5 to include 4

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
        self.wait()
        self.play(Transform(DiffEq,phaseEq))
        # Transform diffeq into f(y)
        self.play(
            DiffEq.shift,UP*3+RIGHT*4,
            DiffEq.set_color, GREEN
        )

        self.setup_axes(animate=False)

        #Get graph+ Coordinates
        self.function = lambda x: (1-x/3)*x
        plot1 = self.get_graph(self.function, x_min = -1, x_max = 3.9, color = GREEN)
        
        #Coordinate label
        label_coord = self.input_to_graph_point(1.5,plot1)
    
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

        eqText = TextMobject(
            "Equilibrium Points"
        )
        # Stores the vectors to points on plot1 given x coordinates 0 and 3. 
        coord1= self.input_to_graph_point(0,plot1)
        coord2 = self.input_to_graph_point(3,plot1)
        coord3 = self.input_to_graph_point(1.5,plot1)

        #Moves the intercept eq into position.
        interceptEq.shift(DOWN*2 + RIGHT*2)
        eqText.next_to(interceptEq,DOWN)
        #Write intercept eq
        self.play(Write(interceptEq),Write(eqText))
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

        # maxPoint =  Circle(color=RED, fill_color=RED, fill_opacity=1,radius = 0.1)
        # maxPoint.shift(coord3)
        # self.play(GrowFromCenter(maxPoint))

        self.wait(2)
        





