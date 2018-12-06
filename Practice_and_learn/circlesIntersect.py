#Given two points(centers) on the command line and two integers(radii) by standard input
#this program determines if the two circles centered at the two points intersect
import math
import sys

#returns the distance between two points
def distance(x1,x2,y1,y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

#compare the distance to the radii
def intersect(x1,y1, x2, y2):
    #input from stdin
    r1 = input("radius of circle one: ")
    r2 = input("radius of circle two: ")
    d = distance(x1,x2,y1,y2)
    if d <= (r1+r2): 
        #they intersect
        print True
    else:
        #they do not
        print False

#input from the command line
a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
d = int(sys.argv[4])

intersect(a,b,c,d)
