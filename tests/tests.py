# Defining tests for the TravisCI and Build Checking
# Tests are run everytime a Pull Request or a Commit is pushed to the GeoMath repo
from geomath import point as p
from geomath import line as l
from geomath import figure as f
import unittest


class PointTest(unittest.TestCase):

    def test_distance(self):
        assert(p.Point(9, 8).distance(p.Point(1, 2)) == 10)

    def test_midpoint(self):
        assert(str(p.Point(9, 8).midpoint(p.Point(1, 2)) == "(5.0, 5.0)"))

    def test_quadrant(self):
        assert(p.Point(2, -8).quadrant() == 4)


# REMAKE

class LineTest(unittest.TestCase):
    def test_line_equation(self):
        p1 = p.Point(2, 2)
        p2 = p.Point(4, 4)
        line = l.Line()
        line.create(p1, p2)

        assert(type(line.equation()) == str)

    def test_ACoefficient(self):
        p1 = p.Point(2, 2.5)
        p2 = p.Point(4, 4)
        line = l.Line()
        line.create(p1, p2)

        assert(line.A == (-1.5))

    def test_BCoefficient(self):
        p1 = p.Point(2, 2.5)
        p2 = p.Point(4, 4)
        line = l.Line()
        line.create(p1, p2)

        assert(line.B == 2.0)

    def test_CCoefficient(self):
        p1 = p.Point(2, 2.5)
        p2 = p.Point(4, 4)
        line = l.Line()
        line.create(p1, p2)

        assert(line.C == (-2.0))


if __name__ == '__main__':
    unittest.main()
