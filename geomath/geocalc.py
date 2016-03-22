"""
GeoMath Calculations Module
Originally written by: Vinicius Mesel
Fist Modification: 03/21/2016
Last Modification: 22/02/2016 #Z4r4tu5tr4
"""

from math import sqrt

"""
ex distance:
	>>> point = Point(1,2)
	>>> point2 = Point(2,1)
	>>> point.distance(point2)
			#out: 1.4142135623730951
ex representation:
	>>> point = Point(1,2)
	>>> print(point)
		#out Point(1,2)

ex introspection:
	>>> type(point)
		#out Point
"""

class Point:
	"Object type cartesian Point"
	def __init__(self, x,y):
		self.x = x
		self.y = y

	def __repr__(self):
		return (("Point(%s, %s)") % ( self.x, self.y))
	
	def distance(self, point_two):
		return sqrt(
				pow(point_two.x - self.x, 2) + pow(point_two.y - self.y, 2) )
