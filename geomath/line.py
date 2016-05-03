from math import sqrt
class Line:
    "Line Object in GeoMath library"

    def __init__(self, PointOne=None, PointTwo=None):
        '''
        :param: PointOne - First point attached to make the line
        :param: B - Second point attached to make the line
        '''
        self.PointOne = PointOne
        self.PointTwo = PointTwo

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

    @property
    def angularCoefficient(self):
        try:
            deltaY = (self.PointTwo.y - self.PointOne.y)
            deltaX = (self.PointTwo.x - self.PointOne.x)

            return(deltaY/deltaX)
        except ZeroDivisionError:
            raise ZeroDivisionError('[%s error] Slope does not exist (the line is vertical).' % (self.__class__.__name__))

    @property
    def linearCoefficient(self):
        return(self.A.y - (self.angularCoefficient * self.A.x))

    def isVertical(self):
        return(self.A.x == self.B.x)

    def isHorizontal(self):
        return(self.A.y == self.B.y)

    def __repr__(self):
        return(('%s(%s, %s)') % (self.__class__.__name__, self.A, self.B))


    # Create the line and one point distance here def LinePointDistance(point):
