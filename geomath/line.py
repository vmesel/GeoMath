#Line file for the GeoMath library

from math import sqrt
import re

class Line:
    def __init__(self, PointOne=None, PointTwo=None):
        '''
        :param: PointOne - First point attached to the line
        :param: PointTwo - Second point attached to the line
        '''
        self.PointOne = PointOne
        self.PointTwo = PointTwo

    def EquationInput(self, equation):
        try:
            regx = re.compile(r'(\W?\d+)\S(\W\d+)\S(\W\d+)\=(\W?\d+)')
            values = regx.findall(equation)
            values = values[0]

            print(values)
            self.ACoefficient = float(values[0])
            self.BCoefficient = float(values[1])
            self.CCoefficient = float(values[2])
            
            return True
        except ValueError:
            return False

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

    @ACoefficient.setter
    def ACoefficient(self, newValue):
        self.ACoefficient = newValue

    @property
    def BCoefficient(self):
        '''
        Return the B coefficient(the one who is aligned with Y) in the general equation of the line
        '''
        return(self.PointTwo.x - self.PointOne.x)

    @BCoefficient.setter
    def BCoefficient(self, newValue):
        self.BCoefficient = newValue

    @property
    def CCoefficient(self):
        '''
        :return: Return the coefficient of C in the general equation of the line. Example( x + y + c = 0)
        '''
        return((self.PointOne.x * self.PointTwo.y) - (self.PointOne.y * self.PointTwo.x))

    @CCoefficient.setter
    def CCoefficient(self, newValue):
        self.CCoefficient = newValue

    @property
    def AngularCoefficient(self):
        try:
            deltaY = (self.PointTwo.y - self.PointOne.y)
            deltaX = (self.PointTwo.x - self.PointOne.x)

            return(deltaY/deltaX)
        except ZeroDivisionError:
            raise ZeroDivisionError('[%s error] Slope does not exist.' % (self.__class__.__name__))

    @AngularCoefficient.setter
    def AngularCoefficient(self, newValue):
        self.AngularCoefficient = newValue

    @property
    def LinearCoefficient(self):
        return(self.PointOne.y - (self.AngularCoefficient * self.PointOne.x))

    @LinearCoefficient.setter
    def LinearCoefficient(self, newValue):
        self.LinearCoefficient = newValue

    def __repr__(self):
        return(('%s(%s, %s)') % (self.__class__.__name__, self.PointOne, self.PointTwo))

    # HERE THE LINE ONLY ATTRIBUTES END

    def PointDistance(self, PointOne):
        A = ((self.ACoefficient * PointOne.x) + (self.BCoefficient * PointOne.y) + self.CCoefficient)
        B = sqrt((self.ACoefficient * self.ACoefficient) + (self.BCoefficient * self.BCoefficient))
        solved = A / B
        return(solved)
