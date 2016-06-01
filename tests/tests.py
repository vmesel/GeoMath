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
        assert(str(p.Point(9, 8).midpoint(p.Point(1, 2))) == "Point(5.0, 5.0)")

    def test_quadrant(self):
        assert(p.Point(2, -8).quadrant() == 4)


# REMAKE

class LineTest(unittest.TestCase):
    def test_instance_two_points(self):
        p1 = p.Point(2, 2)
        p2 = p.Point(4, 4)
        line = l.Line()
        line.create(p1, p2)

        assert(str(line) == "-2.0x+2.0y+0=0")

    def test_instance_equation(self):
        line = l.Line()
        line.create_via_equation("-8x+6y-8=0")
        assert(line.equation() == "-8x+6y-8=0")

        #assert(str(line) == "A: -8 B: +6 C: -8")

    def test_instance_one_point_and_slope(self):
        p1 = p.Point(4, 4.5)
        line = l.Line()
        line.create_via_slope(p1, 1)


        assert(line.equation() == "y=1x+0.5")

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

        assert(float(line.A) == (-1.5))

    def test_b_coefficient(self):
        p1 = p.Point(2, 2.5)
        p2 = p.Point(4, 4)
        line = l.Line()
        line.create(p1, p2)

        assert(float(line.B) == 2.0)

    def test_c_coefficient(self):
        p1 = p.Point(2, 2.5)
        p2 = p.Point(4, 4)
        line = l.Line()
        line.create(p1, p2)

        assert(float(line.C) == (-2.0))

    def test_angular_coefficient(self):
        p1 = p.Point(2, 2.5)
        p2 = p.Point(4, 4)
        line = l.Line()
        line.create(p1, p2)

        assert(float(line.Angular) == (0.75))

    def test_linear_coefficient(self):
        p1 = p.Point(2, 2.5)
        p2 = p.Point(4, 4)
        line = l.Line()
        line.create(p1, p2)

        assert(float(line.Linear) == (1.0))


if __name__ == '__main__':
    unittest.main()
