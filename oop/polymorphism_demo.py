# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method meant to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize rectangle dimensions."""
        self.length = length
        self.width = width

    def area(self):
        """Override area() to compute rectangle area."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize circle radius."""
        self.radius = radius

    def area(self):
        """Override area() to compute circle area."""
        return math.pi * (self.radius ** 2)
