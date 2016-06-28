# Point file for the GeoMath library
from math import sqrt
from geomath.general import General as g


class Point:

    # Defines the Point(x, y)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Midpoint between "self" and "PointTwo".
    def midpoint(self, PointTwo):
        '''
        :param: PointTwo - Point subclass
        :return: Point - subclass
        '''
        Xm = ((self.x + PointTwo.x)/2)
        Ym = ((self.y + PointTwo.y)/2)

        return(Point(Xm, Ym))

    # Euclidean distance between "self" and "PointTwo".
    def distance(self, PointTwo=None):
        '''
        :param: PointTwo - Point subclass
        :return: float - Distance
        '''
        if PointTwo is None:
            PointTwo = self.__class__()

        Xd = pow(PointTwo.x - self.x, 2)
        Yd = pow(PointTwo.y - self.y, 2)

        return(sqrt(Xd + Yd))

    # The quadrant of point  "self".
    def quadrant(self):
        '''
        :return: int - Quadrant
        '''
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
        if type(self.x) == "float":
            return(("%s(%s, %s)") % (self.__class__.__name__, g.fix_float(self.x), g.fix_float(self.y)))
        return(("%s(%s, %s)") % (self.__class__.__name__, (self.x), (self.y)))
