#This program uses Binets Fibonacci Number Formula to calculate the nth fibonacci value
import math

#return fib(n) using Binets
def formula(n):
    root5 = math.sqrt(5)
    pos = (1 + root5)**n
    neg = (1 - root5)**n
    top = pos - neg
    bottom = (2**n) * root5
    return int(top/bottom)

#input from stdin
n = input("Enter Fib Degree: ")

#function call 
print formula(n)
