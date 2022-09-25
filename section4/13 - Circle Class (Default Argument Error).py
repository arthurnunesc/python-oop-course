"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Circle:

    def __init__(self, radius=5, color): # This throws an error
        self.radius = radius
        self.color = color


my_circle = Circle(7, "Blue")
print(my_circle.radius)
print(my_circle.color)
