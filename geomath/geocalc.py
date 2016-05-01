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

    # Midpoint between "self" and "pointTwo".
    def midpoint(self, pointTwo):
        '''
        :param: pointTwo - Point subclass
        :return: Point subclass
        '''
        Xm = ((self.x + pointTwo.x)/2)
        Ym = ((self.y + pointTwo.y)/2)

        return(Point(Xm, Ym))

    # Euclidean distance between "self" and "pointTwo".
    def distance(self, pointTwo=None):
        '''
        If pointTwo is not specified, the origin point is used.

        :param: pointTwo - Point subclass
        :return: float
        '''
        if pointTwo is None:
            pointTwo = self.__class__()

        Xd = pow(pointTwo.x - self.x, 2)
        Yd = pow(pointTwo.y - self.y, 2)

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
    
    def __init__(self, pointOne=None, pointTwo=None):
        '''
        :param: pointOne - Point subclass
        :param: pointTwo - Point subclass
        '''
        self.pointOne = pointOne
        self.pointTwo = pointTwo

    def lineEquation(self, option=None):
        '''
        If no option to return dict with the two equations
        
        :param: option - String identification to type of equation
        :return: Return the general and simplified equation converted to dict or string if declared option.
        '''
        GeneralAns = str(self.equationX)+'x+'+str(self.equationY)+'y+'+str(self.equationB)+'=0'
        SimplifiedAns = 'y='+str(self.angularCoefficient)+'x+'+str(self.linearCoefficient)

        if self.equationY < 0 and self.equationB > 0:
            GeneralAns = str(self.equationX)+'x+('+str(self.equationY)+'y)+'+str(self.equationB)+'=0'

        if self.equationB < 0:
            GeneralAns = str(self.equationX)+'x+'+str(self.equationY)+'y'+str(self.equationB)+'=0'

        if self.linearCoefficient < 0:
            SimplifiedAns = 'y='+str(self.angularCoefficient)+'x'+str(self.linearCoefficient)

        if type(option) is str and option == 'general':
            return(GeneralAns)

        if type(option) is str and option == 'simplified' or option == 'reduced':
            return(SimplifiedAns)

        return({
            'general': GeneralAns,
            'simplified': SimplifiedAns
        })

    @property
    def equationX(self):
        '''
        :return: Return the coefficient of x in the general equation of the line
        '''
        return(self.pointOne.y - self.pointTwo.y)

    @property
    def equationY(self):
        '''
        :return: Return the coefficient of y in the general equation of the line
        '''
        return(self.pointTwo.x - self.pointOne.x)

    @property
    def equationB(self):
        '''
        :return: Return the coefficient of b in the general equation of the line. Example( x + y + b = 0)
        '''
        return((self.pointOne.x * self.pointTwo.y) - (self.pointOne.y * self.pointTwo.x))

    # Contribution by Regis da Silva(rg3915) and factored by Wellington dos Santos (Wellington475)
    @property
    def angularCoefficient(self):
        try:
            deltY = (self.pointTwo.y - self.pointOne.y)
            deltX = (self.pointTwo.x - self.pointOne.x)
            
            return(deltY/deltX)
        except ZeroDivisionError:
            raise ZeroDivisionError('[%s error] Slope does not exist (the line is vertical).' % (self.__class__.__name__))

    @property
    def linearCoefficient(self):
        return(self.pointOne.y - (self.angularCoefficient * self.pointOne.x))

    def isVertical(self):
        return(self.pointOne.x == self.pointTwo.x)

    def isHorizontal(self):
        return(self.pointOne.y == self.pointTwo.y)

    def __repr__(self):
        return(('%s(%s, %s)') % (self.__class__.__name__, self.pointOne, self.pointTwo))


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
