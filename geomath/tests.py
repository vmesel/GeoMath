from geocalc import Point, Area
from nose import with_setup # optional

def testing():
    assert Point(1,2) == "Point(1,2)"
    assert Point(9,8).distance(Point(1,2)) == 10.0
    assert Point(9,8).midpoint(Point(1,2)) == "(5.0, 5.0)"
    assert Area.squarearea(4) == 16
