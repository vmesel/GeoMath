Figures
=======

The figures functions are made to handle figures made of points and calculate stuff like barycenter, points, Perimeter and others that we are working on!

---------------------------------
Creating a Figure
---------------------------------
.. py:function:: figure.Figure()

This is the function to start creating figures. This function is very simple to be used, you just need to type in this with a variable to make the variable become the figure!


>>> FIGUREVAR = figure.Figure()
# This will create your figure


.. py:function:: figure.addPoint(Point)

Figures are currently made of points, so if you need to make a figure have one more point, you will need to run addPoint

>>> FIGUREVAR.addPoint(point.Point(x,y))

The point that is added must be a GeoMath object, if it's not, it won't be recognized by the system.


.. py:function:: figure.addPoints([Point1, Point2, ...])

If you want to add more than one point to an existing figure, you just need to run the command below. It will add the points to the assigned figure.

>>> FIGUREVAR.addPoints([point.Point(x,y), point.Point(x,y), ...])

The points that are added must be GeoMath objects, if they are not, they won't be recognized by the system.

---------------------------------
Figure Attributes
---------------------------------

.. py:function:: figure.Barycenter()

This function is very useful, if you need to calculate the barycenter of a figure, it can be done with just one line of code like this:

>>> FIGUREVAR.Barycenter()
# This will return your figure barycenter point

---------------------------------
Functions Under Development
---------------------------------



.. py:function:: figure.Perimeter()


This function gets the perimeter of the figure that you have created with the points.

>>> FIGUREVAR.Perimeter()
# This will return your figure perimeter


.. py:function:: figure.Area()


This function calculates the area of the figure that you have created with the points.

>>> FIGUREVAR.Area()
# This will return your figure perimeter
