"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Circle:

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color


my_circle = Circle(6, "Yellow")

print(my_circle.radius)
print(my_circle.color)

my_circle.radius = 15
my_circle.color = "Black"

print(my_circle.radius)
print(my_circle.color)
