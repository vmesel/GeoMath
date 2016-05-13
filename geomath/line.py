#Line file for the GeoMath library
from math import sqrt, atan, degrees
from geomath import point as p
import re

class Line:
    def __init__(self):
        """
        These are the initial line parameters
        """
        self.PointOne = 0
        self.PointTwo = 0
        self.Angulation = 0
        self.Angular = 0
        self.Linear = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.createdby = None

    def create(self,PointOne, PointTwo):
        """
        This function is for getting a line created by two points
        """
        self.PointOne = PointOne
        self.PointTwo = PointTwo
        self.createdby = "points"
        self.A = float(self.PointOne.y - self.PointTwo.y)
        self.B = float(self.PointTwo.x - self.PointOne.x)
        self.C = ((self.PointOne.x * self.PointTwo.y) - (self.PointOne.y * self.PointTwo.x))

    def create_via_equation(self, equation):
        """
        This function is for getting a line created by a line equation
        """
        self.createdby = "equation"
        regx = re.compile(r'(\W?\d+)\S(\W\d+)\S(\W\d+)\=(\W?\d+)')
        values = regx.findall(equation)
        values = values[0]
        self.A = values[0]
        self.B = values[1]
        self.C = values[2]
        self.Angular = (float(values[0]) / float(values[1]))
        self.Angulation = degrees(atan(float(self.Angular)))
        self.PointOne = p.Point(float(self.C) / float(self.A),0)
        self.PointTwo = p.Point(0, float(self.C) / float(self.B))


    def equation(self):
        return("{}x{}y{}=0".format(self.A, self.B, self.C))

    def get_angle(self):
        return(self.Angulation)

    def __repr__(self):
        if self.createdby == "equation":
            return("A: {} B: {} C: {}".format(self.A, self.B, self.C))
        elif self.createdby == "points":
            return("Line({},{})".format(self.PointOne, self.PointTwo))

    # HERE THE LINE ONLY ATTRIBUTES END

    def point_distance(self, PointTwo):
        EquationA = ((float(self.A) * float(PointTwo.x)) + (float(self.B) * float(PointTwo.y)) + float(self.C))
        if EquationA == 0:
            raise ValueError('Point is inside the line!')
        EquationB = sqrt((float(self.A) * float(self.A)) + (float(self.B) * float(self.B)))
        return((float(EquationA) / float(EquationB)))


    def comparisor(self, LineTwo):
        angLineTwo = LineTwo.Angular
        if self.Angular == angLineTwo:
            return("Paralell Lines")
        elif self.Angular is not angLineTwo:
            return("Function under development")
            #We need to detect the other types of lines

    def point_alignment(self, PointThree):
        #Function under development
        pass
