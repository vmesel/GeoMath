#Line file for the GeoMath library
from math import sqrt, atan, degrees
from geomath import point as p
import re

class Line:
    def __init__(self, *args, **kwargs):
        #These are the initial line parameters
        self.PointOne = 0
        self.PointTwo = 0
        self.Angulation = 0
        self.Angular = 0
        self.Linear = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.createdby = None

    def create(self, PointOne, PointTwo):
        """
        This function is for getting a line created by two points
        """
        self.createdby = "points"
        self.PointOne = PointOne
        self.PointTwo = PointTwo
        self.A = float(self.PointOne.y - self.PointTwo.y)
        self.B = float(self.PointTwo.x - self.PointOne.x)
        self.Angular = float(((self.PointTwo.y - self.PointOne.y) / (self.PointTwo.x - self.PointOne.x)))
        self.Angulation = degrees(atan(float(self.Angular)))
        self.Linear = float(self.PointOne.y - (self.Angular * self.PointOne.x))
        if self.B > 0 or self.B == 0:
            self.B = "+" + str(self.B)
        self.C = ((self.PointOne.x * self.PointTwo.y) - (self.PointOne.y * self.PointTwo.x))
        if self.C > 0 or self.C == 0:
            self.C = "+" + str(self.C)

    def create_via_equation(self, equation):
        """
        This function is for getting a line created by a line equation
        """
        self.createdby = "equation"
        regex = re.compile(r'([\+\-]?\d*.?\d*x)\s*([\+\-]?\d*.?\d*y)\s*([\+\-]\d*)\s*\=\s*([\+\-]?\d*)')
        values = regex.findall(equation)
        values = values[0]
        self.A = "+1" if values[0] == 'x' or values[0] == '+x' else "-1" if values[0] == '-x' else values[0][:-1]
        self.B = "+1" if values[1] == '+y' else "-1" if values[1] == '-y' else values[1][:-1]
        self.C = values[2]
        self.Angular = (float(self.A) / float(self.B))
        self.Angulation = degrees(atan(float(self.Angular)))
        self.PointOne = p.Point(float(self.C) / float(self.A),0)
        self.PointTwo = p.Point(0, float(self.C) / float(self.B))

    def create_via_slope(self, PointOne, slope):
        """
        This function is to get a line created by a point and a slope
        """
        self.createdby = "slope"
        self.PointOne = PointOne
        self.Angular = slope
        self.Angulation = degrees(atan(float(self.Angular)))
        self.Linear = self.PointOne.y-(self.Angular*self.PointOne.x)
        if self.Linear > 0 or self.Linear == 0:
            self.Linear = "+" + str(self.Linear)

    def equation(self):
        if self.createdby == "equation" or self.createdby == "points":
            return("{}x{}y{}=0".format(self.A, self.B, self.C))
        elif self.createdby == "slope":
            return("y={}x{}".format(self.Angular, self.Linear))

    def get_angle(self):
        if self.createdby == "equation" or self.createdby == "points":
            return("{}x{}y{}=0".format(self.A, self.B, self.C))
        elif self.createdby == "slope":
            return("y={}x{}".format(self.Angular, self.Linear))

    def __repr__(self):
        if self.createdby == "equation" or self.createdby == "points":
            return("{}x{}y{}=0".format(self.A, self.B, self.C))
        elif self.createdby == "slope":
            return("y={}x{}".format(self.Angular, self.Linear))

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
            # We need to detect the other types of lines
            # If angular and linear coefficient are different, they are different
