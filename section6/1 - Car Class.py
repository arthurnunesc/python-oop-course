"""
Course: Python OOP - Object Oriented Programming for Beginners
By: Estefania Cassingena Navone
"""


class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


my_car = Car("Porsche", "911 Carrera", 2020)

print(my_car.year)
my_car.year = 5600
print(my_car.year)
