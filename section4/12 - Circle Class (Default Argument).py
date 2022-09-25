"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Circle:
        
    def __init__(self, radius=5):
        self.radius = radius


my_circle = Circle()
print(my_circle.radius)

your_circle = Circle(8)
print(my_circle.radius)
