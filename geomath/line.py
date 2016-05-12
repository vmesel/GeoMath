from math import sqrt
class Line:
    def __init__(self, PointOne, PointTwo):
        '''
        :param: PointOne - First point attached to the line
        :param: PointTwo - Second point attached to the line
        '''
        self.PointOne = PointOne
        self.PointTwo = PointTwo

    def EquationInput(equation):
        pass
            # This is the equation input for working with the line equation

    def Equation(self):
        if self.CCoefficient == 0:
            respGeneral = str(self.ACoefficient)+'x + '+str(self.BCoefficient)+'y = 0'
        else:
            respGeneral = str(self.ACoefficient)+'x + '+str(self.BCoefficient)+'y + '+str(self.CCoefficient)+' = 0'

        return(respGeneral)

    @property
    def ACoefficient(self):
        '''
        Return the A coefficient(the one in the X right side) in the general equation of the line
        '''
        return(self.PointOne.y - self.PointTwo.y)

    @property
    def BCoefficient(self):
        '''
        Return the B coefficient(the one who is aligned with Y) in the general equation of the line
        '''
        return(self.PointTwo.x - self.PointOne.x)

    @property
    def CCoefficient(self):
        '''
        :return: Return the coefficient of b in the general equation of the line. Example( x + y + b = 0)
        '''
        return((self.PointOne.x * self.PointTwo.y) - (self.PointOne.y * self.PointTwo.x))

    @property
    def AngularCoefficient(self):
        try:
            deltaY = (self.PointTwo.y - self.PointOne.y)
            deltaX = (self.PointTwo.x - self.PointOne.x)

            return(deltaY/deltaX)
        except ZeroDivisionError:
            raise ZeroDivisionError('[%s error] Slope does not exist.' % (self.__class__.__name__))

    @property
    def LinearCoefficient(self):
        return(self.PointOne.y - (self.angularCoefficient * self.PointOne.x))

    def __repr__(self):
        return(('%s(%s, %s)') % (self.__class__.__name__, self.PointOne, self.PointTwo))

    # HERE THE LINE ONLY ATTRIBUTES END

    def PointDistance(self, PointOne):
        A = ((self.ACoefficient * PointOne.x) + (self.BCoefficient * PointOne.y) + self.CCoefficient)
        B = sqrt((self.ACoefficient * self.ACoefficient) + (self.BCoefficient * self.BCoefficient))
        solved = A / B
        return(solved)
