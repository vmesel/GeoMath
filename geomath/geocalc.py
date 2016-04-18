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
        tempPoints = []
        perimeterValues = []

        # Apply recursion for getting this property to work

        if len(points) < 3:
            return("It's not possible to get a perimeter of a line/point")
        else:
            while len(points) != 0:
                print(len(points))
                # Load a Point, if there is no point loaded
                if tempPoints == []:
                    tempPoints.append(points[0])
                    points.remove(points[0])

                # Load another point so it can be possible to make the permiter calculation
                elif len(tempPoints) == 1:
                    tempPoints.append(points[0])
                    points.remove(points[0])

                # Make the permiter calculation
                elif len(tempPoints) == 2:
                    permiterValues.append(str(Line.distance(tempPoints[0],tempPoints[1])))

                return(perimeterValues)



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
