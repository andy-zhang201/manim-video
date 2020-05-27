from manimlib.imports import *

class firstProject(Scene):
    def construct(self):
        t1 = TextMobject("text1","text2","text3")
        t1[1].shift(RIGHT)
        t1[2].shift(RIGHT*2)

        #Write the text
        self.play(Write(t1))

        #Move the txt & change its color.
        for i in range(0,3):
            self.play(
                t1[i].set_color,BLUE,
                t1[i].shift, RIGHT*2+UP*2,
                run_time = 1
            )

#Simply draws a basic parabola. This scene aims to make the code as simple as possible.
class simpleGraph1(GraphScene):
    #Using the default config library
    CONFIG = {}

    #Drawing a parabola is simple.
    def construct(self):
        #All you need is four things:

        #Set up the axes (If not it throws an AssertionError (line 151 in graph_scene.py))
        self.setup_axes(animate = True) 

        #Define a function using numpy or lambda.
        self.func = lambda x: x**2
        
        #Call .get_graph on the function. Set necessary parameters
        func_graph = self.get_graph(self.func,
        #These optional parameters set the minimum and max x-values of the function.
        x_min = 0,
        x_max = 7)

        #Finally, add the graph to the movie
        self.play(ShowCreation(func_graph))
        self.wait()


#Someone Else's code
class simpleGraph2(GraphScene):
    CONFIG = {
        "x_min" : -10,
        "x_max" : 10,
        "y_min" : -1.5,
        "y_max" : 1.5,
        "graph_origin" : ORIGIN ,
        "function_color" : RED ,
        "axes_color" : GREEN,
        "x_labeled_nums" :range(-10,12,2),
        
        }
    def construct(self):
        self.setup_axes(animate=True)
        #.get_graph needs a pointer to a function, so don't put () after func_to_graph
        func_graph=self.get_graph(self.func_to_graph,self.function_color)
        func_graph2=self.get_graph(self.func_to_graph2)
        vert_line = self.get_vertical_line_to_graph(TAU,func_graph,color=YELLOW)
        graph_lab = self.get_graph_label(func_graph, label = "\\cos(x)")
        graph_lab2=self.get_graph_label(func_graph2,label = "\\sin(x)", x_val=-10, direction=UP/2)
        two_pi = TexMobject("x = 2 \\pi")
        label_coord = self.input_to_graph_point(TAU,func_graph)
        two_pi.next_to(label_coord,RIGHT+UP)
    
        self.play(ShowCreation(func_graph),ShowCreation(func_graph2))
        self.play(ShowCreation(vert_line), ShowCreation(graph_lab), ShowCreation(graph_lab2),ShowCreation(two_pi))

    def func_to_graph(self,x):
        return np.cos(x)
    
    def func_to_graph2(self,x):
        return np.sin(x)

#Explores the Config dictionary to make the graph look better
class simpleGraph3(GraphScene):
    #Using the config library, we can change the class Attributes of GraphScene
    CONFIG = {
        #Uppermost number on the y-axis
        "y_max" : 50,
        #number at the origin. Cannot be higher than y_max
        "y_min" : 0,
        #Same logic as y_max/min
        "x_max" : 7,
        "x_min" : 0,

        #Small tick frequency. Not labelled.
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
        #Creates a large tick at each number. Pass in a list
        "y_labeled_nums": range(0,51,10), #Try putting k=3
        "x_labeled_nums": list(np.arange(0, 7.0+0.5, 0.5)),

        #colours
        "axes_color" : BLUE,
        "function_color": RED,

        #Number of decimal palces on the x-label.
        "x_label_decimal":1,
        #Location of the origin.
        "graph_origin": 3 * DOWN + 6 * LEFT,
        #Relative Position of the labels next to the tick marks
        "x_label_direction":DOWN,
        "y_label_direction":LEFT,
        #Pass strings, labels the x_axis
        "x_axis_label": "The X axis",
        "x_axis_width":10
    }

    def construct(self):
        #Setup the axes
        self.setup_axes(animate=True)
        #Declare a function
        self.function = lambda x: x**2
        #Call .get_graph() to create the graph
        plot1 = self.get_graph(self.function, x_min = 0, x_max = 7)

        #Animates the graph
        self.play(ShowCreation(plot1))
    
#Adding graph labels
class simpleGraph4(GraphScene):
    #Using the config library, we can change the class Attributes of GraphScene
    CONFIG = {
        #Uppermost number on the y-axis
        "y_max" : 50,
        #number at the origin. Cannot be higher than y_max
        "y_min" : 0,
        #Same logic as y_max/min
        "x_max" : 7,
        "x_min" : 0,

        #Small tick frequency. Not labelled.
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
        #Creates a large tick at each number. Pass in a list
        "y_labeled_nums": range(0,51,10), #Try putting k=3
        "x_labeled_nums": list(np.arange(0, 7.0+0.5, 0.5)),

        #colours
        "axes_color" : BLUE,
        "function_color": RED,

        #Number of decimal palces on the x-label.
        "x_label_decimal":1,
        #Location of the origin.
        "graph_origin": 3 * DOWN + 6 * LEFT,
        #Relative Position of the labels next to the tick marks
        "x_label_direction":DOWN,
        "y_label_direction":LEFT,
        #Pass strings, labels the x_axis
        "x_axis_label": "The X axis",
        "x_axis_width":10
    }

    def construct(self):
        self.setup_axes(animate=True)
        self.function = lambda x: x**2
        plot1 = self.get_graph(self.function, x_min = 0, x_max = 7, color = YELLOW)
        
        #Creates the label for a graph
        graph_lab = self.get_graph_label(plot1, label = "f(x)=x^2")

        #Animates the graph as well as the label
        self.play(ShowCreation(plot1),ShowCreation(graph_lab))
    
#Vertline and Label_coord
class simpleGraph5(GraphScene):
    #Using the config library, we can change the class Attributes of GraphScene
    CONFIG = {
        #Uppermost number on the y-axis
        "y_max" : 50,
        #number at the origin. Cannot be higher than y_max
        "y_min" : 0,
        #Same logic as y_max/min
        "x_max" : 7,
        "x_min" : 0,

        #Small tick frequency. Not labelled.
        "y_tick_frequency" : 5, 
        "x_tick_frequency" : 0.5, 
        #Creates a large tick at each number. Pass in a list
        "y_labeled_nums": range(0,51,10), #Try putting k=3
        "x_labeled_nums": list(np.arange(0, 7.0+0.5, 0.5)),

        #colours
        "axes_color" : BLUE,
        "function_color": RED,

        #Number of decimal palces on the x-label.
        "x_label_decimal":1,
        #Location of the origin.
        "graph_origin": 3 * DOWN + 6 * LEFT,
        #Relative Position of the labels next to the tick marks
        "x_label_direction":DOWN,
        "y_label_direction":LEFT,
        #Pass strings, labels the x_axis
        "x_axis_label": "The X axis",
        "x_axis_width":10
    }

    def construct(self):
        self.setup_axes(animate=True)
        self.function = lambda x: x**2
        plot1 = self.get_graph(self.function, x_min = 0, x_max = 7, color = BLUE)
        
        #Creates the label for a graph
        graph_lab = self.get_graph_label(plot1, label = "f(x)=x^2")

        #Creates a vertical line
        vert_line = self.get_vertical_line_to_graph(4.5,plot1,color=GREEN)

        #Coordinate label
        label_coord = self.input_to_graph_point(4.5,plot1)
        four=TexMobject("(4.5,20.25)",color=MAROON) #MAROON = MAROON_C in constants.py
        four.next_to(label_coord,UP)
        
        hello = TextMobject("hello")
        hello.next_to(graph_lab,DOWN)

        #Animates the graph as well as the label
        self.wait()        
        self.play(ShowCreation(plot1))
        self.wait()
        self.play(ShowCreation(graph_lab))
        self.wait()
        self.play(ShowCreation(vert_line),ShowCreation(four),ShowCreation(hello))
        self.wait()
    
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
        arrow3coord1 = ORIGIN
        arrow3coord2 = np.array([-4.5,0,0])

        arrow4coord1 = ORIGIN
        arrow4coord2 = self.input_to_graph_point(3,plot1)

        arrow5coord1 = np.array([6.5,0,0])
        arrow5coord2 = self.input_to_graph_point(3,plot1)
        #Phase Arrows
        arrow3 = Arrow(arrow3coord1,arrow3coord2,stroke_width=40,buff=0.2)
        arrow3.set_color(PURPLE)

        #Check vectorized_mobject.py for list of configurables.
        arrow4 = Arrow(arrow4coord1,arrow4coord2,stroke_width=40, buff=0.2)
        arrow4.set_color(PURPLE)

        arrow5 = Arrow(arrow5coord1,arrow5coord2,stroke_width = 50, buff=0.2)
        arrow5.set_color(PURPLE)

        self.play(GrowArrow(arrow3),GrowArrow(arrow4),GrowArrow(arrow5))
        self.wait()

        stabText = TextMobject(
            "Stable",
            "Unstable",
        )
        stabText[0].next_to(arrow5coord2,UP*2+RIGHT)
        stabText[1].next_to(arrow3coord1,UP*2+LEFT)
        
        self.play(Write(stabText))
        self.wait(2)
        





