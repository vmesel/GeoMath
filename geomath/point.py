# Point file for the GeoMath library
from math import sqrt
class Point:
    "Point Object in GeoMath library"

    # Defines the Point(x, y)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Midpoint between "self" and "PointTwo".
    def midpoint(self, PointTwo):
        '''
        :param: PointTwo - Point subclass
        :return: Point subclass
        '''
        Xm = ((self.x + PointTwo.x)/2)
        Ym = ((self.y + PointTwo.y)/2)

        return(Point(Xm, Ym))

    # Euclidean distance between "self" and "PointTwo".
    def distance(self, PointTwo=None):
        '''
        If other is not specified, the origin point is used.

        :param: other - Point subclass
        :return: float
        '''
        if PointTwo is None:
            PointTwo = self.__class__()

        Xd = pow(PointTwo.x - self.x, 2)
        Yd = pow(PointTwo.y - self.y, 2)

        return(sqrt(Xd + Yd))

    # The quadrant of point  "self".
    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return(1)
        elif self.x < 0 and self.y > 0:
            return(2)
        elif self.x < 0 and self.y < 0:
            return(3)
        elif self.x > 0 and self.y < 0:
            return(4)
        else:
            return(0)

    # Defines the output of the point
    def __repr__(self):
        return(("%s(%s, %s)") % (self.__class__.__name__, self.x, self.y))
