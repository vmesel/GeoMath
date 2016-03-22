"""
GeoMath Calculations Module
Originally written by: Vinicius Mesel and Eduardo Mendes
Last Modification: 22/03/2016 #Z4r4tu5tr4
"""

from math import sqrt

"""
How to use the Point Class
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
ex midpoint:
	>>> point.midpoint(point2)
		#out (1.5, 1.5)
"""

class Point:
	"Object type cartesian Point"

	#Defines the Point(x, y)
	def __init__(self, x,y):
		self.x = x
		self.y = y

	#Defines the output of the point
	def __repr__(self):
		return (("Point(%s, %s)") % (self.x, self.y))

	#Defines the distance between two points
	def distance(self, point_two):
		return sqrt(
				pow(point_two.x - self.x, 2) + pow(point_two.y - self.y, 2)
				)

	#Defined the midpoint between two points
	def midpoint(self, point_two):
		return(
		(self.x + point_two.x)/2 , (self.y + point_two.y)/2
		)

class Area:
	def squarearea(a):
		return(a**2)
