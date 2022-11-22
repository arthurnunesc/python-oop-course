"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Circle:

    def __init__(self, colour, radius=5): # This throws an error
        self.radius = radius
        self.colour = colour


my_circle = Circle(7, "Blue")
print(my_circle.radius)
print(my_circle.colour)
