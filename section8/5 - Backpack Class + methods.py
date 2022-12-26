class Backpack:
    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print("Please provide a valid item.")

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            print("The backpack does not contain that item.")
            return 0

    def has_item(self, item):
        return item in self._items


backpack_instance = Backpack()
print(backpack_instance.items)

backpack_instance.add_item("Garrafa d'água")
print(backpack_instance.items)

backpack_instance.add_item("Saco de dormir")
print(backpack_instance.items)

has_water = backpack_instance.has_item("Garrafa d'água")
print(has_water)

backpack_instance.remove_item("Garrafa d'água")
print(backpack_instance.items)

backpack_instance.remove_item("Fogão portátil")
print(backpack_instance.items)

print(backpack_instance.has_item("Garrafa d'água"))
