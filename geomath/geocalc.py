"""
GeoMath - Analytical Geometry Module
Originally written by: Vinicius Mesel and Eduardo Mendes
Last Modification: 23/03/2016 #vmesel
"""
# Defining tests for the TravisCI and Build Checking
import unittest
# from nose import with_setup  # optional
from math import sqrt


class Point:
    "Object type cartesian Point"

    # Defines the Point(x, y)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Defines the output of the point
    def __repr__(self):
        return (("Point(%s, %s)") % (self.x, self.y))

    # Defines the distance between two points
    def distance(self, point_two):
        return sqrt(
            pow(point_two.x - self.x, 2) + pow(point_two.y - self.y, 2)
        )

    # Defined the midpoint between two points
    def midpoint(self, point_two):
        return(
            (self.x + point_two.x) / 2, (self.y + point_two.y) / 2
        )


class Figure:

    def squarearea(a):
        return(a**2)

    def barycenter(points):
        arrayx = []
        arrayy = []
        for point in points:
            arrayx.append(point.x)
            arrayy.append(point.y)

        XPoint = sum(arrayx) / len(arrayx)
        YPoint = sum(arrayx) / len(arrayy)

        return(("Point(%s, %s)") % (XPoint, YPoint))


class Line:

    def coef_angular(x, x0, y, y0):
        '''
        Dados dois pontos da reta (x,y) e (x_0, y_0) temos que
        o coeficiente linear é dado por
        m = \frac{\Delta y}{\Delta x} = \frac{y - y_0}{x - x_0}
        '''
        if x - x0:
            return (y - y0) / (x - x0)

    def coef_linear(a, x, y):
        '''
        Dados o coeficiente angular (m) e um ponto (x, y) da reta temos que
        o coeficiente linear da reta é dado por
        b = y - ax
        '''
        return y - a * x


class PointTest(unittest.TestCase):

    def test_two(self):
        assert(Point(9, 8).distance(Point(1, 2)) == 10)

    def test_three(self):
        assert(str(Point(9, 8).midpoint(Point(1, 2)) == "(5.0, 5.0)"))

    def test_four(self):
        assert(Figure.squarearea(4) == 16)

    def test_five(self):
        assert(Figure.barycenter([Point(1, 2), Point(2, 3), Point(
            4, 5)]) == "Point(2.3333333333333335, 2.3333333333333335)")

    def test_coef_angular1(self):
        assert(Line.coef_angular(0, 1, 0, 1) == 1)

    def test_coef_angular2(self):
        assert(Line.coef_angular(0, -1, 0, 1) == -1)

    def test_coef_linear1(self):
        assert(Line.coef_linear(1, 0, 0) == 0)

    def test_coef_linear2(self):
        assert(Line.coef_linear(-1, 0, 0) == 0)


if __name__ == '__main__':
    unittest.main()
