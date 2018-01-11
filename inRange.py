#This program checks if a number is in a specified range
import sys
import math

#return lower bound if x is less than lower bound
#return upper bound if x is greater than upper bound
#return x if x is in range
def range(x,b1,b2):
    upper = max(b1,b2)
    lower = min(b1,b2)
    if(x < lower):
        print lower
        return lower
    elif(x > upper):
        print upper
        return upper
    else:
        print x
        return x

#input from stdin
b1 = int(input("Enter bound one: "))
b2 = int(input("Enter bound two: "))
x = int (input("Enter value you want to check: "))

#function call
range(x,b1,b2)
