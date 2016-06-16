#Vector file for the GeoMath library
from geomath import general as g
from geomath import point as p
class Vector:
    """Vector Object in GeoMath library"""
    
    def __init__(self, a, b = None):
        # i and j by caninical base
        self.i = 0
        self.j = 0
        if type(a) is p.Point and b == None:
            self.i = a.x
            self.j = a.y
        elif type(a) in g.numbers and type(b) in g.numbers:
            self.i = a
            self.j = b
        elif type(a) is p.Point and type(b) is p.Point:
            self.i = b.x - a.x
            self.j = b.y - a.y

    def sum(self, v):
        """
        This function returns sum of a giving vector
        :param: v - Vector subclass
        :return: Vector subclass
        '''
        """
        return Vector(self.i+v.i, self.j+v.j)  # This work with points 
        
    def multiplication(self, n):
        """
        This function returns multiplication of vector by number
        :param: n - number
        :return: Vector subclass
        '''
        """
        return Vector(n*self.i, n*self.j)
        
