# GeoMath [![Build Status](https://travis-ci.org/vmesel/GeoMath.svg?branch=master)](https://travis-ci.org/vmesel/GeoMath)[![PyPI version] (https://badge.fury.io/py/geomath.svg)](https://badge.fury.io/py/geomath) [![Coverage Status](https://coveralls.io/repos/github/vmesel/GeoMath/badge.svg?branch=master)](https://coveralls.io/github/vmesel/GeoMath?branch=master) [![Stories in Ready](https://badge.waffle.io/vmesel/GeoMath.svg?label=ready&title=Ready)](http://waffle.io/vmesel/GeoMath)

Library that enables Python Users to use concepts of Analytical Geometry!

Classes available for usage:

  * Point
    * Point(a,b)
    * distance(self,point_two)
    * midpoint(self,point_two)
    * quadrant(self)
  * Figure
    * AddPoint(s)
    * Perimeter
    * Barycenter
  * Line
    * Line(PointA, PointB)
    * lineEquation(self)
    * isVertical(self)
    * isHorizontal(self)



Classes that we are working on:
 - Three Points alignment (This function require Sarrus Law, we will try to make this as default as possible)
 - Distance from a line to a point!

If you want to contribute, fork it into a REPO and help us develop this tool for everyone, or write an Issue so we can work on it!
