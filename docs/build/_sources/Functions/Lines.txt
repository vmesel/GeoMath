Lines
=====


The line statement is the basic statement for the Euclidean Geometry and for everything in geometry. Figures are formed by lines, distances are the length of lines and even more.
Lines must be used to get general arguments, like angles, line equation, comparisons between to lines and etc.

-----------------
Creating the Line
-----------------
To start with a line you may want to run these commands that are below this statement.

.. py:function:: line.Line()

To start getting a line done in the GeoMath system, you must run this command! This is an object assigned function, so you must assign it to an object so it can be called

>>> LINEVAR = line.Line()


There are two ways of inputting values for a line: creating a line with 2 Points or by the Line Equation(supposing that you have it).

.. py:function:: line.create(PointOne, PointTwo)

To get a line assigning two different points to it, you must run this command. It will generate a line in the instance that is in your line.

>>> LINEVAR.create(point.Point(0,0), point.Point(4,4))

Running these commands, we will generate the equation of the line simply by solving the matrix represented by the two points and by the x and y line.

.. py:function:: line.create_via_equation(LineEquation)

These command is very useful if you have the line equation. The line equation is inserted by a string formated like this "ax-by+c=0": with the coefficients in the front and with the line

>>>  LINEVAR.create_via_equation(LineEquation)

----------------
Line Attributes
----------------

In this section, we will explain to you the attributes that the Line() class have in the project!

.. py:function:: line.equation()

This is a commmand that will enable you to get the equation of the line you have created.

>>> LINEVAR.Equation()

.. py:function:: line.get_angle()

This function gets the angulation of your line and give it in degrees

>>> LINEVAR.get_angle()

.. py:function:: line.A

This function returns the A coefficient.

>>> LINEVAR.A()

.. py:function:: line.B

This function returns the B coefficient.

>>> LINEVAR.B()

.. py:function:: line.C

This function returns the C coefficient.

>>> LINEVAR.C()

-------------------------------------
Attributes involving other functions
-------------------------------------

There are some attributed that depend on other functions, and we are going to list them here below.


.. py:function:: line.point_distance(self, Point)

This function is made to calculate the distance between a line and a point with a very simple syntax.

>>>  LINEVAR.point_distance(Point)

.. py:function:: line.comparisor(self, Line)

This function was made to compare two lines and decide if they are parallel, coincident or perpendicular.

>>>  LINEVAR.comparisor(Line)

.. py:function:: line.point_alignment(self, Point)

This function is to check the 3 point alignment, but for using it, you need to create a line and check the alignment of a point in the line.

>>>  LINEVAR.point_alignment(Point)
