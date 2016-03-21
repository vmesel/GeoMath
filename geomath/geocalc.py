"""
GeoMath Calculations Module
Originally written by: Vinicius Mesel
Last Modification: 03/21/2016
"""
import math

# Distance of Two Points A(Xa, Ya) and B(Xb, Yb)
def pointsdistance(A, B, round):
    x = A[0]
    y = A[1]
    z = B[0]
    w = B[1]
    Rounding = round
    # X = X0 and Z = X1
    def xDistanceCalc(x,z): return (z - x)**2
    # Y = Y0 and W = Y1
    def yDistanceCalc (y,w): return (w - y)**2
    #def DistanceCalc(xResult, yResult): return()
    RealDistance = math.sqrt(yDistanceCalc (y,w) + xDistanceCalc(x,z))
    if Rounding == True:
        RealDistance = RealDistance*100
        return(math.ceil(RealDistance)/100)

    return RealDistance

def barycenter(PointsList):
    return(PointsList)
