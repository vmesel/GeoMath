from math import sqrt
class Line:
    "Line Object in GeoMath library"

    def __init__(self, PointOne=None, PointTwo=None):
        '''
        :param: PointOne - First point attached to make the line
        :param: PointTwo - Second point attached to make the line
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
        #return(respGeneral)

    @property
    def equationX(self):
        '''
        :return: Return the coefficient of x in the general equation of the line
        '''
        return(self.PointOne.y - self.PointTwo.y)

    @property
    def equationY(self):
        '''
        :return: Return the coefficient of y in the general equation of the line
        '''
        return(self.PointTwo.x - self.PointOne.x)

    @property
    def equationB(self):
        '''
        :return: Return the coefficient of b in the general equation of the line. Example( x + y + b = 0)
        '''
        return((self.PointOne.x * self.PointTwo.y) - (self.PointOne.y * self.PointTwo.x))

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
        return(self.PointOne.y - (self.angularCoefficient * self.PointOne.x))

    def isVertical(self):
        return(self.PointOne.x == self.PointTwo.x)

    def isHorizontal(self):
        return(self.PointOne.y == self.PointTwo.y)

    def __repr__(self):
        return(('%s(%s, %s)') % (self.__class__.__name__, self.PointOne, self.PointTwo))


    # Create the line and one point distance here! Make it useful!
    def LinePointDistance(self, PointOne):
        equationA = ((self.equationX * PointOne.x) + (self.equationY * PointOne.y) + self.equationB)
        #equationB = sqrt((self.equationX * self.equationX) + (self.equationY * self.equationY))
        #equation = equationA / equationB
        return(equationA)
