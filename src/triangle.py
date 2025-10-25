# src/triangle.py
"""
Triangle utility module for Pytest demonstration.

This file contains basic geometry functions for working with triangles:
- validation (is_triangle),
- area and perimeter calculation.

Intended as an educational example for unit testing with pytest.
"""


import math


def is_triangle(a, b, c):
    """Checks if a triangle is possible."""
    if not all(isinstance(x, (int, float)) and math.isfinite(x) for x in (a, b, c)):
        return False
    
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    max_value = max(a, b, c)
    if max_value >= a + b + c - max_value:
        return False
    
    return True


def triangle_area(a, b, c):
    """Returns the area of a valid triangle, otherwise 0."""
    if is_triangle(a, b, c):
        circ = (a + b + c) / 2.0
        aera = math.sqrt(circ * (circ - a) * (circ - b) * (circ - c))
        return aera
    
    return 0


def triangle_perimeter(a, b, c):
    """Returns the perimeter of a valid triangle, otherwise 0."""
    if is_triangle(a, b, c):
        return a + b + c 
    
    return 0