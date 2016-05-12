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

        print(values)
        self.A = float(values[0])
        self.B = float(values[1])
        self.C = float(values[2])

    def __repr__(self):
        if self.createdby == "equation":
            return("A: {} B: {} C: {}".format(self.A, self.B, self.C))
        elif self.createdby == "points":
            return("Line({},{})".format(self.PointOne, self.PointTwo))

    # HERE THE LINE ONLY ATTRIBUTES END

    def PointDistance(self, PointTwo):
        A = ((self.A * PointTwo.x) + (self.B * PointTwo.y) + self.C)
        #return(A)
        B = sqrt((self.A * self.A) + (self.B * self.B))
        solved = A / B
        return(solved)
