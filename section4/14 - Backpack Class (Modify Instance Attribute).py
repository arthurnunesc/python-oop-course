"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""

class Backpack:

    def __init__(self, color):
        self.items = []
        self.color = color


my_backpack = Backpack("Blue")
your_backpack = Backpack("Red")

print(my_backpack.color)
print(your_backpack.color)

print("Changing Color...")
my_backpack.color = "Green"

print(my_backpack.color)
print(your_backpack.color)
