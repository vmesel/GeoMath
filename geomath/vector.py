# Vector file for the GeoMath library
from math import sqrt, acos
from geomath import general as g
from geomath import point as p
# TODO: implement the ZeroVector


class Vector:
    def __init__(self, a, b=None):
        # i and j by canonical base
        self.i = 0
        self.j = 0
        if type(a) is p.Point and b is None:
            self.i = a.x
            self.j = a.y
        elif type(a) in g.numbers and type(b) in g.numbers:
            self.i = a
            self.j = b
        elif type(a) is p.Point and type(b) is p.Point:
            self.i = b.x - a.x
            self.j = b.y - a.y
        self.components = (self.i, self.j)
        self.length = sqrt(self.i**2 + self.j**2)

    def sum(self, v):
        """
        This function returns sum of a giving vector.
        :param: v - Vector subclass
        :return: Vector subclass
        """
        return Vector(self.i+v.i, self.j+v.j)

    def multiplication(self, n):
        """
        This function returns multiplication of vector by number
        :param: n - number
        :return: Vector subclass
        """
        return Vector(n*self.i, n*self.j)

    def equal(self, v):
        """
        This function returns if this vector is equal of a giving vector.
        :param: v - Vector subclass
        :return: Boolean subclass
        """
        return self.i == v.i and self.j == v.j

    def parallel(self, v):
        """
        This function returns if a vector is parallel of a giving vector.
        :param: v - Vector subclass
        :return: Boolean subclass
        """
        return self.i/v.i == self.j/v.j

    def scalar_product(self, v):
        """
        :param: v - Vector subclass
        :return: number
        """
        return (self.i*v.i + self.j*v.j)

    def angle(self, v):
        """
        This function returns the angle between this vector
         and a giving vector.
        :param: v - Vector subclass
        :return: Boolean subclass
        """
        return acos(scalar_product(self, v)/(self.length*v.length))
