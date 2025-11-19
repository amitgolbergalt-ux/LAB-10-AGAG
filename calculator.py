"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
import math

def square_root(a):
    if a<0:
        raise ValueError
    return math.sqrt(a)
def hypotenuse(a,b):
    return math.sqrt(a**2 + b**2)
def add(a, b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if a == 0:
        raise ZeroDivisionError
    return a/b
def logarithm(a,b):
    if b <= 0:
        raise ValueError
    return math.log(b,a)
def exponent(a,b):
    return a**b


