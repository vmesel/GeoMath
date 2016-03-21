from geocalc import *

A = [6, 2]
B = [10, 8]


List = [6,2,10,8,3,6]
print("""
   _____            __  __       _   _
  / ____|          |  \/  |     | | | |
 | |  __  ___  ___ | \  / | __ _| |_| |___
 | | |_ |/ _ \/ _ \| |\/| |/ _` | __| '_  |
 | |__| |  __/ (_) | |  | | (_| | |_| | | |
  \_____|\___|\___/|_|  |_|\__,_|\__|_| |_|

An Analytic Geometry Library for Python 3.x
Created by: Vinicius Mesel
Available at: http://www.github.com/vmesel/GeoMath

""")
print("Distance between two points: {}\n\r".format(pointsdistance(A, B, False)))
print("Barycenter: {} \n\r".format(barycenter(List)))

print
