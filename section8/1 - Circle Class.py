class Circle:
    def __init__(self, radius):
        self.radius = radius

    def find_diameter(self):
        print(f"Diameter: {self.radius * 2}")
        return self.radius * 2


circle_instance = Circle(5)

circle_instance.find_diameter()
