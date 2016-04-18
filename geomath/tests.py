# Defining tests for the TravisCI and Build Checking
from nose import with_setup  # optional
import geocalc as gc
import unittest


class PointTest(unittest.TestCase):

    def test_two(self):
        assert(gc.Point(9, 8).distance(gc.Point(1, 2)) == 10)

    def test_three(self):
        assert(str(gc.Point(9, 8).midpoint(gc.Point(1, 2)) == "(5.0, 5.0)"))

    def test_four(self):
        assert(gc.Figure.squarearea(4) == 16)

    def test_five(self):
        assert(gc.Figure.barycenter([gc.Point(1, 2), gc.Point(2, 3), gc.Point(
            4, 5)]) == "Point(2.3333333333333335, 2.3333333333333335)")

if __name__ == '__main__':
    unittest.main()
