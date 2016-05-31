# Line file for the GeoMath library
from math import sqrt, atan, degrees
from geomath import point as p
import re


class Line:
    def __init__(self, *args, **kwargs):
        """
            Using:

            >>> line = l.Line(p.Point(2,2), p.Point(4,4))
            Line(Point(2, 2), Point(4, 4))

            >>> line = l.Line("-8x+6y-8=0")
            A: -8 B: +6 C: -8

            >>> line = l.Line(p.Point(4, 4.5), m=1)
            Angular:1.0 Linear:0.5
        """

        # These are the initial line parameters
        self.PointOne = 0
        self.PointTwo = 0
        self.Angulation = 0
        self.Angular = 0
        self.Linear = 0
        self.A = ""
        self.B = ""
        self.C = ""
        self.createdby = None

        if len(args) > 1:
            if isinstance(args[0], p.Point) and isinstance(args[1], p.Point):
                self.create(args[0], args[1])

        if len(args) == 1:
            if isinstance(args[0], p.Point) and "m" in kwargs:
                self.create_via_slope(args[0], kwargs['m'])
            
        elif type(args[0]) is str:
            self.create_via_equation(args[0])

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
        regex = re.compile(r'([\+\-]?\d*x)\s*([\+\-]\d*y)\s*([\+\-]\d*)\s*\=\s*([\+\-]?\d*)')
        values = regex.findall(equation)
        values = values[0]
        with values as V:
            self.A = "+1" if V[0] == 'x' or V[0] == '+x' else "-1" if V[0] == '-x' else V[0][:-1]
            self.B = "+1" if V[1] == '+y' else "-1" if V[1] == '-y' else V[1][:-1]
            self.C = V[2]
        self.Angular = (float(self.A) / float(self.B))
        self.Angulation = degrees(atan(float(self.Angular)))
        self.PointOne = p.Point(float(self.C) / float(self.A), 0)
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
        return(self.Angulation)

    def __repr__(self):
        if self.createdby == "equation":
            return("A: {} B: {} C: {}".format(self.A, self.B, self.C))
        elif self.createdby == "points":
            return("Line({}, {})".format(self.PointOne, self.PointTwo))
        elif self.createdby == "slope":
            return("Angular:{} Linear:{}".format(float(self.Angular), float(self.Linear)))
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
            # We need to detect the other types of lines
            # If angular and linear coefficient are different, they are different

    def point_alignment(self, PointThree):
        # [ 0, 0, 1 ]
        # [ 4, 4, 1 ]
        # [ 7, 7, 1 ]
        # This will return true or false
        pass
