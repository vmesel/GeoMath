from math import sqrt

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
