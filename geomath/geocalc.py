"""
GeoMath - Analytical Geometry Module
Originally written by: Vinicius Mesel and Eduardo Mendes
Last Modification: 18/04/2016 #vmesel
"""
from math import sqrt

class Point:
    "Point Object in GeoMath library"

    # Defines the Point(x, y)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Defines the output of the point
    def __repr__(self):
        return (("Point(%s, %s)") % (self.x, self.y))

class Line:
    "Line Object in GeoMath library"
    # Defines the distance between two points

    def lineEquation(points):
        if len(points) == 1:
            # Apply Angular coeficient for discovering line
            pass
        elif len(points) == 2:
            # Apply Sarrus Law
            pass

    # Define the distance between two points
    def distance(point_one, point_two):
        return sqrt(
            pow(point_two.x - point_one.x, 2) + pow(point_two.y - point_one.y, 2)
        )

    # Defined the midpoint between two points
    def midpoint(point_one, point_two):
        return(
            (point_one.x + point_two.x) / 2, (point_one.y + point_two.y) / 2
        )


class Figure:
    "Figure Object in GeoMath library"
    # Perimeter formula for getting the figure perimeter
    def perimeter(points):
        "Perimeter Property for Figure Object in GeoMath library"
        perimeter = 0.0
        points = self.points() + [self.points[0]]
        for i in range(len(self.points)):
            perimeter += distance(points[i], points[i+1])

        return perimeter


    # Calculating figure barycenter
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
