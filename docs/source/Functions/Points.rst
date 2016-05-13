Point
======

The point attributes are very simple, we have some of them that involves two points, but they are quite simple to use like we describe here below:

---------------------------------
Setting Up a Point
---------------------------------

.. py:function:: point.Point(x,y)

This is the function to start creating points to make your life easier and happier. This function is very simple to be used, you just need to type in:


>>> PointOne = point.Point(x,y) # where x and y are the coordinates of your point
# This will return a point

-----------------------------------
Point attributes with other Points
-----------------------------------

.. py:function:: point.midpoint(OtherPoint)

This is the function that you will want to use when you need to calculate the midpoint from two points, so to use it, you first instantiate the first point and them:


>>> MidPoint = POINTVariable.point.midpoint(OtherPoint)
# This will return the MidPoint between POINTVariable and OtherPoint

.. py:function:: point.distance(OtherPoint)

If you need to calculate the distance between two points, you don't need to do any difficult calculations for that, you just need to call the function like this:


>>> Distance = POINTVariable.distance(OtherPoint)
# This will return the distance between POINTVariable and OtherPoint

---------------------------------
Point Attributes
---------------------------------

.. py:function:: point.quadrant()

If you need to know in which quadrant your point is located at, we already solved this problem for you, you just need to use point.quadrant and it will return a int that represents the quadrant:


>>> Distance = POINTVariable.point.quadrant()
# This will return the quadrant from POINTVariable
