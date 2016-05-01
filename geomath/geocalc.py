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
        self.x = float(x)
        self.y = float(y)

    # Midpoint between "self" and "other".
    def midpoint(self, other):
        '''
        :param: other - Point subclass
        :return: Point subclass
        '''
        Xm = ((self.x + other.x)/2)
        Ym = ((self.y + other.y)/2)

        return(Point(Xm, Ym))

    # Euclidean distance between "self" and "other".
    def distance(self, other=None):
        '''
        If other is not specified, the origin point is used.

        :param: other - Point subclass
        :return: float
        '''
        if other is None:
            other = self.__class__()

        Xd = pow(other.x - self.x, 2)
        Yd = pow(other.y - self.y, 2)

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

class Line:
    "Line Object in GeoMath library"
    
    def __init__(self, A=None, B=None):
        '''
        :param: A - Point subclass
        :param: B - Point subclass
        '''
        self.A = A
        self.B = B

    def lineEquation(self):
        '''
        :return: Return the general and simplified equation converted to dict
        '''
        respGeneral = str(self.equationX)+'x+'+str(self.equationY)+'y+'+str(self.equationB)+'=0'
        respSimplified = 'y='+str(self.angularCoefficient)+'x+'+str(self.linearCoefficient)

        if self.equationB < 0:
            respStr = str(self.equationX)+'x+'+str(self.equationX)+'y'+str(self.equationB)+'=0'

        if self.linearCoefficient < 0:
            respSimplified = 'y='+str(self.angularCoefficient)+'x'+str(self.linearCoefficient)

        return({
        'general': respGeneral,
        'simplified': respSimplified
        })

    @property
    def equationX(self):
        '''
        :return: Return the coefficient of x in the general equation of the line
        '''
        return(self.A.y - self.B.y)

    @property
    def equationY(self):
        '''
        :return: Return the coefficient of y in the general equation of the line
        '''
        return(self.B.x - self.A.x)

    @property
    def equationB(self):
        '''
        :return: Return the coefficient of b in the general equation of the line. Example( x + y + b = 0)
        '''
        return((self.A.x * self.B.y) - (self.A.y * self.B.x))

    # Contribution by Regis da Silva(rg3915) and factored by Wellington dos Santos (Wellington475)
    @property
    def angularCoefficient(self):
        try:
            deltY = (self.B.y - self.A.y)
            deltX = (self.B.x - self.A.x)
            
            return(deltY/deltX)
        except ZeroDivisionError:
            raise ZeroDivisionError('[%s error] Slope does not exist (the line is vertical).' % (self.__class__.__name__))

    @property
    def linearCoefficient(self):
        return(self.A.y - (self.angularCoefficient * self.A.x))

    def __repr__(self):
        return(('%s(%s, %s)') % (self.__class__.__name__, self.A, self.B))


class Figure:
    "Figure Object in GeoMath library"
    def __init__(self):
        self.points = []

    def addPoint(self, point):
        self.points.append((point))

    def addPoints(self, point):
        for p in point:
            self.points.append((p))

    # Perimeter formula for getting the figure perimeter
    def perimeter(self):
        "Perimeter Property for Figure Object in GeoMath library"
        perimeter = 0.0
        if len(self.points) >= 3:
            points = self.points + [self.points[0]]
            for i in range(len(self.points)):
                perimeter += Line.distance(points[i], points[i+1])
            return(perimeter)
        else:
            return("You need at least 3 points to calculate the Perimeter property!")


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
