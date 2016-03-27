"""
GeoMath - Analytical Geometry Module
Originally written by: Vinicius Mesel and Eduardo Mendes
Last Modification: 24/03/2016 #z4r4tu5tr4
"""

from math import sqrt

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
	@property
	def distance(self, point_two):
		return sqrt(
				pow(point_two.x - self.x, 2) + pow(point_two.y - self.y, 2)
				)

	#Defined the midpoint between two points
	@property
	def midpoint(self, point_two):
		return(
		(self.x + point_two.x)/2 , (self.y + point_two.y)/2
		)

class Line:
	def __init__(self, point1, point2):
		self.point1 = point1
		self.point2 = point2

	def __repr__(self):
		return (("L(%s,%s)") % (self.point1,self.point2))
	@property
	def length(self):
		return self.point1.distance(self.point2)

class Figure:
	pass

class Rectangle(Figure):

	def __init__(self, point1, point2):
		self.point1 = point1
		self.point2 = point2

	def __repr__(self):
		return (("R(%s,%s)") % (self.point1,self.point2))

	#----- immutable properties
	@property
	def width(self):
		return self.point2.x - self.point1.x

	@property
	def height(self):
		return self.point2.y - self.point1.y

	@property
	def area(self):
		return self.height * self.width

class Square(Figure):

	def __init__(self, point1, point2):
		self.point1 = point1
		self.point2 = point2

	def __repr__(self):
		return (("R(%s,%s)") % (self.point1,self.point2))

	#----- immutable properties
	@property
	def side(self):
		return self.point2.y - self.point1.y

	@property
	def area(self):
		return self.side * self.side
"""
	def barycenter(points):
		i = 0
		arrayx = []
		arrayy = []
		for point in points:
			arrayx.append(point.x)
			arrayy.append(point.y)

		XPoint = sum(arrayx)/len(arrayx)
		YPoint = sum(arrayx)/len(arrayy)

		return(("Point(%s, %s)") % (XPoint, YPoint))
"""
