#Line file for the GeoMath library
from math import sqrt
import re

class Line:
    def __init__(self):
        self.PointOne = 0
        self.PointTwo = 0
        self.Angular = 0
        self.A = 0
        self.B = 0
        self.C = 0
        self.createdby = None

    def Create(self,PointOne, PointTwo):
        self.PointOne = PointOne
        self.PointTwo = PointTwo
        self.createdby = "points"

    def CreateViaEquation(self, equation):
        self.createdby = "equation"
        regx = re.compile(r'(\W?\d+)\S(\W\d+)\S(\W\d+)\=(\W?\d+)')
        values = regx.findall(equation)
        values = values[0]
        self.A = values[0]
        self.B = values[1]
        self.C = values[2]
        self.Angular = (float(values[0]) / float(values[1]))

    def Equation(self):
        if self.createdby == "equation":
            return("{}x{}y{}=0".format(self.A, self.B, self.C))
        elif self.createdby == "points":
            self.A = (self.PointOne.y - self.PointTwo.y)
            self.B = (self.PointTwo.x - self.PointOne.x)
            self.C = ((self.PointOne.x * self.PointTwo.y) - (self.PointOne.y * self.PointTwo.x))
            return("{}x{}y{}=0".format(self.A, self.B, self.C)) # Fix the return of the equation!

    def CoordinatedPoints(self):
        #Here we should calculate two points that are (x,0) and (0,y)
        pass


    def __repr__(self):
        if self.createdby == "equation":
            return("A: {} B: {} C: {}".format(self.A, self.B, self.C))
        elif self.createdby == "points":
            return("Line({},{})".format(self.PointOne, self.PointTwo))

    # HERE THE LINE ONLY ATTRIBUTES END

    def PointDistance(self, PointTwo):
        EquationA = ((float(self.A) * float(PointTwo.x)) + (float(self.B) * float(PointTwo.y)) + float(self.C))
        if EquationA == 0:
            raise ValueError('Point is inside the line!')
        EquationB = sqrt((float(self.A) * float(self.A)) + (float(self.B) * float(self.B)))
        return((float(EquationA) / float(EquationB)))
