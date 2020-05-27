from manimlib.imports import *

class doodling1(GraphScene):
    Domain = list(np.arange(-3,3+1,1))
    #Not working
    del Domain[2]

    #Set maxY to be a class attribute
    maxY = 20

    
    #Using the config library, we can change the class Attributes of GraphScene

      #Using the config library, we can change the class Attributes of GraphScene
    CONFIG = {
        #Uppermost number on the y-axis
        "y_max" : maxY,
        #number at the origin. Cannot be higher than y_max
        "y_min" : -maxY,
        #Same logic as y_max/min
        "x_max" : maxY,
        "x_min" : -maxY,

        #Small tick frequency. Not labelled.
        "y_tick_frequency" : 1, 
        "x_tick_frequency" : 1, 

        #Number of decimal palces on the x-label.
        "x_label_decimal":1,
        "y_label_decimal":1,

        #Creates a large tick at each number. Pass in a list
        "y_labeled_nums": [], 
        "x_labeled_nums": [], #Add +0.5 to include 4

        #colours
        "axes_color" : BLUE,
        "function_color": RED,


        #Location of the origin.
        "graph_origin": ORIGIN,
        #Relative Position of the labels next to the tick marks
        "x_label_direction":DOWN,
        "y_label_direction":LEFT,
        #Pass strings, labels the x_axis
        "x_axis_label": "",
        "y_axis_label":"",

        #Scaling factors for the axes. Not sure what 10 does.
        #X-axis is stretched longer
        "x_axis_width":7,
        "y_axis_width":10,

        #How do I move f(y) above the uppermost tick?
        #"y_axis_label_direction":UP,

        #Removes 0 label
        "exclude_zero_label": True,

    }

    def construct(self):
        self.setup_axes(animate=False)

        #Quad 1
        for i in range(1,maxY):
            self.func = lambda x: -(maxY-i)/(i)*x+(maxY-i)
            plot1 = self.get_graph(self.func, color = GREEN, x_min = 0, x_max = (-(maxY-i))/(-(maxY-i)/(i)))
            self.play(ShowCreation(plot1),run_time = 0.2)
        
        #Quad 2
        for i in range(1,maxY):
            self.func = lambda x: (maxY-i)/(i)*x+(maxY-i)
            plot1 = self.get_graph(self.func, color = RED, x_min = (-(maxY-i))/((maxY-i)/(i)), x_max = 0)
            self.play(ShowCreation(plot1),run_time = 0.2)
        
        #Quad 3
        for i in range(1,maxY):
            self.func = lambda x: -(maxY-i)/(i)*x-(maxY-i)
            plot1 = self.get_graph(self.func, color = BLUE, x_min = ((maxY-i))/(-(maxY-i)/(i)), x_max = 0)
            self.play(ShowCreation(plot1),run_time = 0.2)

        #Quad 4
        for i in range(1,maxY):
            self.func = lambda x: (maxY-i)/(i)*x-(maxY-i)
            plot1 = self.get_graph(self.func, color = YELLOW,x_min = 0, x_max = ((maxY-i))/((maxY-i)/(i)))
            self.play(ShowCreation(plot1),run_time = 0.2)


        self.wait()


class cardioid(Scene):
    #Returns an array of evenly spaced points along the circle
    #given a number of points to be spaced out.

    def construct(self):
        base = Circle(color=WHITE, radius = 1)
    
        self.play(ShowCreation(base))

    def getPoints(numOfPoints):
        pointArray=[]
        return pointArray
    