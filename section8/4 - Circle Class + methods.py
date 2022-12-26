class Circle:
    def __init__(self, radius):
        self.radius = radius

    def find_diameter(self):

        return self.radius * 2


circle_instance = Circle(5)

diameter = circle_instance.find_diameter()
print(diameter)
