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
        "Perimeter Property for Figure Object in GeoMath library"
        n = len(self.polygonPoints)
        p = 0.0
        for i in range(n):
            j = (i + 1) % n
            p += abs(self.polygonPoints[i].distance(self.polygonPoints[j]))
        return(p)

    def barycenter(points):
        "Barycenter Property for Figure Object in GeoMath library"

        i = 0
        arrayx = []
        arrayy = []
        for point in points:
            arrayx.append(point.x)
            arrayy.append(point.y)

        XPoint = sum(arrayx) / len(arrayx)
        YPoint = sum(arrayx) / len(arrayy)

        return(("Point(%s, %s)") % (XPoint, YPoint))

    def area(self):
        _points = self.polygonPoints
        if len(_points) == 3:
            # Triangle
            # Calculate the area with matrix
            pass
        elif len(_points) == 4:
            # Square or rectangle
            pass
        elif len(_points) > 4:
            # Polygon
            pass

    def __repr__(self):
        points = ""
        for point in self.polygonPoints:
            pontos = pontos + str(point) + " "
        figureString = "Figure Points: " + points
        return(figureString)

class Circumference():
    def __init__(self):
        self.centerPoint = None
        self.radius = 0
        self.area = 0
        self.perimeter = 0
