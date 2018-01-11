#This program calculates the distance between two points 
import math
import sys

def dist(x1 ,x2, y1, y2):
    a = (x2 - x1)**2
    b = (y2 - y1)**2
    c = math.sqrt(a + b)
    print c

x = int(sys.argv[1])
y = int(sys.argv[2])
x_ = int(sys.argv[3])
y_ = int(sys.argv[4])

dist(x,x_,y,y_)

