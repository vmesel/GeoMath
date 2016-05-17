#Figure file for the GeoMath library
from math import sqrt

class Figure:
    "Figure Object in GeoMath library"

    def __init__(self, figureType=None):
        self.polygonPoints = []

    def add_point(self, point):
        self.polygonPoints.append((point))

    def add_points(self, point):
        for p in point:
            self.polygonPoints.append((p))

    def area(self):
        """
        Area Class based on a StackOverflow post
        """
        n = len(self.polygonPoints) # of corners
        a = 0.0
        for i in range(n):
            j = (i + 1) % n
            a += abs(self.polygonPoints[i].x * self.polygonPoints[j].y - self.polygonPoints[j].x * self.polygonPoints[i].y)
        result = a / 2.0
        return result

    def perimeter(self):
        """
        Perimeter Property for Figure Object in GeoMath library
        """
        n = len(self.polygonPoints)
        p = 0.0
        for i in range(n):
            j = (i + 1) % n
            p += abs(self.polygonPoints[i].distance(self.polygonPoints[j]))
        return(p)

    def barycenter(points):
        """
        Barycenter Property for Figure Object in GeoMath library
        """
        i = 0
        arrayx = []
        arrayy = []
        for point in points:
            arrayx.append(point.x)
            arrayy.append(point.y)
        XPoint = sum(arrayx) / len(arrayx)
        YPoint = sum(arrayx) / len(arrayy)
        return(("Point(%s, %s)") % (XPoint, YPoint))

    def __repr__(self):
        points = ""
        for point in self.polygonPoints:
            pontos = pontos + str(point) + " "
        figureString = "Figure Points: " + points
        return(figureString)

class Circumference():
    def __init__(self):
        self.centerPoint = None
        self.outsidePoint = None
        self.Eq = None
        self.Rad = 0
        self.A = 0
        self.Per = 0
        self.createdby = None

    def create_points(self, centerPoint, outsidePoint):
        from .point import Point
        import math
        self.centerPoint = centerPoint
        self.outsidePoint = outsidePoint
        self.Rad = centerPoint.distance(outsidePoint)
        self.createdby = "points"
        self.Eq = "({}-{})ˆ2 + ({}-{})^2={}ˆ2".format(outsidePoint.x, centerPoint.x, outsidePoint.y, centerPoint.y, self.Rad)
        self.A = float(self.Rad) ** float(2) * math.pi #math.pi * (float(self.radius) ** float(2))
        self.Per = 2 * math.pi * self.Rad

    def create_equation(self, equation):
        self.Eq = equation
        self.createdby = "equation"

    def area(self):
        return(self.A)

    def perimeter(self):
        return(self.Per)

    def equation(self):
        if self.createdby == "equation":
            return(self.Eq)
        return(self.Eq)

    def radius(self):
        return(self.Rad)
