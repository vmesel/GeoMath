# Defining tests for the TravisCI and Build Checking
from geomath import point as p
from geomath import line as l
import unittest


class PointTest(unittest.TestCase):

    def test_distance(self):
        assert(p.Point(9, 8).distance(p.Point(1, 2)) == 10)

    def test_midpoint(self):
        assert(str(p.Point(9, 8).midpoint(p.Point(1, 2)) == "(5.0, 5.0)"))

    def test_quadrant(self):
        assert(p.Point(2, -8).quadrant() == 4)

    def test_distance2(self):
        p1 = p.Point(2, 1)
        p2 = p.Point(2, 4)
        assert(p.distance2(p1, p2))


class LineTest(unittest.TestCase):

    def test_line_equation(self):
        p1 = p.Point(2, 2)
        p2 = p.Point(4, 4)
        line = l.Line(p1, p2)

        assert(type(line.lineEquation()) == dict)

    def test_x_equation(self):
        p1 = p.Point(2, 2.5)
        p2 = p.Point(4, 4)
        line = l.Line(p1, p2)

        assert(line.equationX == (-1.5))

    def test_y_equation(self):
        p1 = p.Point(2, 2.5)
        p2 = p.Point(4, 4)
        line = l.Line(p1, p2)

        assert(line.equationY == 2.0)

    def test_b_equation(self):
        p1 = p.Point(2, 2.5)
        p2 = p.Point(4, 4)
        line = l.Line(p1, p2)

        assert(line.equationB == (-2.0))

    def test_is_vertical(self):
        p1 = p.Point(2, 2)
        p2 = p.Point(2, 4)
        line = l.Line(p1, p2)

        assert(line.isVertical() == True)

    def test_is_horizontal(self):
        p1 = p.Point(2, 2)
        p2 = p.Point(4, 2)
        line = l.Line(p1, p2)

        assert(line.isHorizontal() == True)

    def test_coef_angular(self):
        p1 = p.Point(2, 2)
        p2 = p.Point(4, 4)
        line = l.Line(p1, p2)

        assert(line.angularCoefficient == 1)

    def test_coef_linear(self):
        p1 = p.Point(2, 2)
        p2 = p.Point(4, 4.5)
        line = l.Line(p1, p2)

        assert(line.linearCoefficient == (-0.5))

if __name__ == '__main__':
    unittest.main()
