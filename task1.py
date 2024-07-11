"""
Task 1
"""
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __eq__(self, other):
        return self.radius == other.radius
    def __gt__(self, other):
        return self.radius > other.radius
    def __lt__(self, other):
        return self.radius < other.radius
    def __ge__(self, other):
        return self.radius >= other.radius
    def __le__(self, other):
        return self.radius <= other.radius
    def __add__(self, value):
        return Circle(self.radius + value)
    def __sub__(self, value):
        return Circle(self.radius - value)
    def __iadd__(self, value):
        self.radius += value
        return self
    def __isub__(self, value):
        self.radius -= value
        return self
    def __str__(self):
        return f"Circle with radius {self.radius}"
    
if __name__ == "__main__":
    circle1 = Circle(5)
    circle2 = Circle(3)
# -------------------------
    print(circle1 == circle2)
    print(circle1 > circle2)
    print(circle1 < circle2)
# --------------------------
    circle3 = Circle(7)
    circle4 = Circle(7)
# --------------------------
    print(circle3 == circle4)
    print(circle3 >= circle4)
    print(circle3 <= circle4)
# --------------------------
    circle5 = Circle(10)
    circle5 += 2
    print(circle5)
# --------------------------
    circle6 = Circle(8)
    circle6 -= 3
    print(circle6)
