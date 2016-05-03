from math import sqrt
class Point:
    "Point Object in GeoMath library"

    # Defines the Point(x, y)
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # Midpoint between "self" and "other".
    def midpoint(self, pointtwo):
        '''
        :param: pointtwo - Point subclass
        :return: Point subclass
        '''
        Xm = ((self.x + pointtwo.x)/2)
        Ym = ((self.y + pointtwo.y)/2)

        return(Point(Xm, Ym))

    # Euclidean distance between "self" and "other".
    def distance(self, pointtwo=None):
        '''
        If other is not specified, the origin point is used.

        :param: other - Point subclass
        :return: float
        '''
        if other is None:
            other = self.__class__()

        Xd = pow(pointtwo.x - self.x, 2)
        Yd = pow(pointtwo.y - self.y, 2)

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
