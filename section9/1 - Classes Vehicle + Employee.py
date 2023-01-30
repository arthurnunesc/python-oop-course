class Vehicle:
    def __init__(self, color, license_plate, is_electric):
        self.color = color
        self.license_plate = license_plate
        self.is_electric = is_electric

    def show_license_plate(self):
        print(self.license_plate)

    def show_info(self):
        print("Vehicle info:")
        print(f"Color: {self.color}")
        print(f"License Plate: {self.license_plate}")
        print(f"Electric: {self.is_electric}")


class Employee:
    def __init__(self, name, vehicle):
        self.name = name
        self.vehicle = vehicle

    def show_vehicle_info(self):
        self.vehicle.show_info()


vehicle_instance = Vehicle("Red", "XD56790", True)
employee_instance = Employee("Jonas", vehicle_instance)

print(employee_instance.name)
employee_instance.show_vehicle_info()
print(employee_instance.vehicle.color)
